"""Non-destructive GLB export for roads made with the Pathix add-on.

This module is installed beside Pathix's __init__.py and registered there.
"""

import os
import re
import traceback

import bpy
import numpy as np
from bpy.props import BoolProperty, EnumProperty, StringProperty
from bpy_extras.io_utils import ExportHelper


def _pathix_modifier(obj):
    if obj is None or obj.type != 'MESH' or 'pathix exist' not in obj:
        return None
    return next((m for m in obj.modifiers
                 if m.type == 'NODES' and m.node_group
                 and m.node_group.name.startswith('pathix nodes')), None)


def _safe_name(value):
    return re.sub(r'[^A-Za-z0-9_.-]+', '_', value).strip('._') or 'Pathix_Road'


def _add_output_node(group, node_type, output_name):
    output = next((node for node in group.nodes
                   if node.bl_idname == 'NodeGroupOutput' and node.is_active_output), None)
    if output is None or not output.inputs['Geometry'].is_linked:
        raise ValueError('Pathix node group has no connected Geometry output')
    previous = output.inputs['Geometry'].links[0].from_socket
    node = group.nodes.new(node_type)
    node.location = (output.location.x - 220, output.location.y)
    group.links.new(previous, node.inputs['Geometry'])
    group.links.new(node.outputs[output_name], output.inputs['Geometry'])


def _material_name(obj):
    mesh = obj.data
    if not mesh.polygons:
        return 'Empty'
    index = mesh.polygons[0].material_index
    if index < len(mesh.materials) and mesh.materials[index]:
        return mesh.materials[index].name
    return 'Unassigned'


def _prepare_bake(context, obj, created_materials):
    name = _material_name(obj)
    source = next((m for m in obj.data.materials if m and m.name == name), None)
    if source is None or not source.use_nodes:
        raise ValueError('Material %s cannot be baked' % name)
    material = source.copy()
    created_materials.append(material)
    for index, slot in enumerate(obj.data.materials):
        if slot == source:
            obj.data.materials[index] = material
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    context.view_layer.objects.active = obj
    obj.data.uv_layers.new(name='JME_Bake')
    obj.data.uv_layers.active = obj.data.uv_layers['JME_Bake']
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.uv.smart_project(island_margin=0.01)
    bpy.ops.object.mode_set(mode='OBJECT')
    return material


def _keep_only_bake_uv(obj):
    # A single UV set also keeps the baked maps in TEXCOORD_0 for jME3.
    for layer in list(obj.data.uv_layers):
        if layer.name != 'JME_Bake':
            obj.data.uv_layers.remove(layer)
    obj.data.uv_layers.active = obj.data.uv_layers['JME_Bake']


def _bake_image(material, name, resolution, bake_type, created_images, color=True):
    image = bpy.data.images.new(name, width=resolution, height=resolution, alpha=False)
    created_images.append(image)
    if not color:
        image.colorspace_settings.name = 'Non-Color'
    target = material.node_tree.nodes.new('ShaderNodeTexImage')
    target.image = image
    for node in material.node_tree.nodes:
        node.select = node == target
    material.node_tree.nodes.active = target
    options = {'type': bake_type, 'margin': 8}
    if bake_type == 'DIFFUSE':
        options['pass_filter'] = {'COLOR'}
    bpy.ops.object.bake(**options)
    return image


def _simple_baked_material(material, image, alpha=False):
    nodes = material.node_tree.nodes
    nodes.clear()
    output = nodes.new('ShaderNodeOutputMaterial')
    shader = nodes.new('ShaderNodeBsdfPrincipled')
    texture = nodes.new('ShaderNodeTexImage')
    texture.image = image
    uv = nodes.new('ShaderNodeUVMap')
    uv.uv_map = 'JME_Bake'
    material.node_tree.links.new(uv.outputs['UV'], texture.inputs['Vector'])
    material.node_tree.links.new(texture.outputs['Color'], shader.inputs['Base Color'])
    if alpha:
        material.node_tree.links.new(texture.outputs['Alpha'], shader.inputs['Alpha'])
        if hasattr(material, 'surface_render_method'):
            material.surface_render_method = 'BLENDED'
    material.node_tree.links.new(shader.outputs['BSDF'], output.inputs['Surface'])
    shader.inputs['Metallic'].default_value = 0.0
    shader.inputs['Roughness'].default_value = 0.85


def _bake_curb(context, obj, resolution, created_materials, created_images):
    material = _prepare_bake(context, obj, created_materials)
    image = _bake_image(material, obj.name + '_CurbColor', resolution,
                        'DIFFUSE', created_images)
    _simple_baked_material(material, image)
    _keep_only_bake_uv(obj)


def _bake_markings(context, obj, resolution, created_materials, created_images):
    material = _prepare_bake(context, obj, created_materials)
    tree = material.node_tree
    output = next((n for n in tree.nodes if n.bl_idname == 'ShaderNodeOutputMaterial'
                   and n.is_active_output), None)
    if output is None or not output.inputs['Surface'].is_linked:
        raise ValueError('Road marking material has no surface output')
    mix = output.inputs['Surface'].links[0].from_node
    if mix.bl_idname != 'ShaderNodeMixShader':
        raise ValueError('Road marking material has no transparency mix')
    first = mix.inputs[1].links[0].from_node
    second = mix.inputs[2].links[0].from_node
    transparent_first = first.bl_idname == 'ShaderNodeBsdfTransparent'
    shader = second if transparent_first else first
    if shader.bl_idname != 'ShaderNodeBsdfPrincipled':
        raise ValueError('Road marking shader is not Principled BSDF')

    emission = tree.nodes.new('ShaderNodeEmission')
    color_input = shader.inputs['Base Color']
    if color_input.is_linked:
        tree.links.new(color_input.links[0].from_socket, emission.inputs['Color'])
    else:
        emission.inputs['Color'].default_value = color_input.default_value
    tree.links.new(emission.outputs['Emission'], output.inputs['Surface'])
    color = _bake_image(material, obj.name + '_MarkingColor', resolution,
                        'EMIT', created_images)

    tree.links.new(mix.inputs[0].links[0].from_socket, emission.inputs['Color'])
    mask = _bake_image(material, obj.name + '_MarkingMask', resolution,
                       'EMIT', created_images, color=False)
    rgba = np.empty(resolution * resolution * 4, dtype=np.float32)
    mask_rgba = np.empty_like(rgba)
    color.pixels.foreach_get(rgba)
    mask.pixels.foreach_get(mask_rgba)
    rgba = rgba.reshape((-1, 4))
    mask_rgba = mask_rgba.reshape((-1, 4))
    rgba[:, 3] = mask_rgba[:, 0] if transparent_first else 1.0 - mask_rgba[:, 0]
    packed = bpy.data.images.new(obj.name + '_MarkingRGBA', width=resolution,
                                  height=resolution, alpha=True)
    created_images.append(packed)
    packed.pixels.foreach_set(rgba.ravel())
    packed.update()
    _simple_baked_material(material, packed, alpha=True)
    _keep_only_bake_uv(obj)


def _bake_surface_material(context, obj, resolution, created_materials, created_images):
    """Bake asphalt to portable PBR images on UV0."""
    material_name = _material_name(obj)
    if material_name != 'road1':
        return False
    if not obj.data.uv_layers:
        raise ValueError('The road has no UV map for baking')
    source_material = next((m for m in obj.data.materials if m and m.name == material_name), None)
    if source_material is None or not source_material.use_nodes:
        raise ValueError('The %s material cannot be baked' % material_name)

    material = _prepare_bake(context, obj, created_materials)
    images = {}
    for suffix, bake_type in (('Color', 'DIFFUSE'),
                              ('Roughness', 'ROUGHNESS'),
                              ('Normal', 'NORMAL')):
        images[suffix] = _bake_image(material, obj.name + '_Surface' + suffix,
                                     resolution, bake_type, created_images,
                                     color=(suffix == 'Color'))

    nodes = material.node_tree.nodes
    nodes.clear()
    output = nodes.new('ShaderNodeOutputMaterial')
    shader = nodes.new('ShaderNodeBsdfPrincipled')
    color = nodes.new('ShaderNodeTexImage')
    color.image = images['Color']
    roughness = nodes.new('ShaderNodeTexImage')
    roughness.image = images['Roughness']
    normal_texture = nodes.new('ShaderNodeTexImage')
    normal_texture.image = images['Normal']
    normal_map = nodes.new('ShaderNodeNormalMap')
    uv = nodes.new('ShaderNodeUVMap')
    uv.uv_map = 'JME_Bake'
    for texture in (color, roughness, normal_texture):
        material.node_tree.links.new(uv.outputs['UV'], texture.inputs['Vector'])
    material.node_tree.links.new(color.outputs['Color'], shader.inputs['Base Color'])
    material.node_tree.links.new(roughness.outputs['Color'], shader.inputs['Roughness'])
    material.node_tree.links.new(normal_texture.outputs['Color'], normal_map.inputs['Color'])
    material.node_tree.links.new(normal_map.outputs['Normal'], shader.inputs['Normal'])
    material.node_tree.links.new(shader.outputs['BSDF'], output.inputs['Surface'])
    shader.inputs['Metallic'].default_value = 0.0
    _keep_only_bake_uv(obj)
    return True


class PATHIX_OT_export_jme_glb(bpy.types.Operator, ExportHelper):
    """Bake selected Pathix road to GLB without changing the source object"""

    bl_idname = 'pathix.export_jme_glb'
    bl_label = 'Export GLB for jME3'
    bl_options = {'REGISTER'}

    filename_ext = '.glb'
    filter_glob: StringProperty(default='*.glb', options={'HIDDEN'})

    content: EnumProperty(
        name='Content',
        items=[
            ('ROAD', 'Road only', 'Export road geometry without lights or other generated props'),
            ('ROAD_LIGHTS', 'Road + lights', 'Include street and traffic lights, but omit trees, benches and bins'),
            ('ALL', 'Road + all props', 'Realize all generated instances into mesh geometry'),
        ],
        default='ROAD_LIGHTS',
    )
    separate_materials: BoolProperty(
        name='Separate by material',
        description='Create distinct GLB objects for road, curb, sidewalk, and markings',
        default=True,
    )
    bake_tar: BoolProperty(
        name='Bake road appearance',
        description='Bake asphalt, pavement, curb striping and road markings onto portable UV0 textures',
        default=True,
    )
    tar_resolution: EnumProperty(
        name='Road texture size',
        items=[('1024', '1024', ''), ('2048', '2048', ''), ('4096', '4096', '')],
        default='2048',
    )

    @classmethod
    def poll(cls, context):
        return context.mode == 'OBJECT' and _pathix_modifier(context.active_object) is not None

    def invoke(self, context, event):
        source = context.active_object
        if not self.filepath:
            folder = os.path.dirname(bpy.data.filepath) if bpy.data.filepath else os.path.expanduser('~')
            self.filepath = os.path.join(folder, _safe_name(source.name) + '_road.glb')
        return ExportHelper.invoke(self, context, event)

    def draw(self, context):
        layout = self.layout
        layout.prop(self, 'content')
        row = layout.row()
        row.enabled = not self.bake_tar
        row.prop(self, 'separate_materials')
        layout.prop(self, 'bake_tar')
        if self.bake_tar:
            layout.prop(self, 'tar_resolution')
            layout.label(text='Tar baking separates materials automatically.', icon='INFO')
        if self.content == 'ALL':
            layout.label(text='This can create a very large mesh.', icon='INFO')

    def execute(self, context):
        source = context.active_object
        source_modifier = _pathix_modifier(source)
        if source_modifier is None:
            self.report({'ERROR'}, 'Select a Pathix road object')
            return {'CANCELLED'}

        filepath = bpy.path.ensure_ext(self.filepath, '.glb')
        previous_selection = list(context.selected_objects)
        previous_active = context.view_layer.objects.active
        created_objects = []
        created_materials = []
        created_images = []
        local_group = None
        scene = context.scene
        old_engine = scene.render.engine
        old_samples = scene.cycles.samples

        try:
            bpy.ops.object.select_all(action='DESELECT')
            export_obj = source.copy()
            export_obj.data = source.data.copy()
            context.collection.objects.link(export_obj)
            created_objects.append(export_obj)
            export_obj.name = source.name + '_JME_Export'
            export_obj.hide_set(False)
            export_obj.select_set(True)
            context.view_layer.objects.active = export_obj

            local_group = source_modifier.node_group.copy()
            export_modifier = export_obj.modifiers[source_modifier.name]
            export_modifier.node_group = local_group
            if self.content == 'ROAD_LIGHTS':
                for socket in ('Socket_31', 'Socket_29', 'Socket_32'):
                    export_modifier.properties.inputs[socket]['value'] = True
            if self.content == 'ROAD':
                _add_output_node(local_group, 'GeometryNodeSeparateComponents', 'Mesh')
            else:
                _add_output_node(local_group, 'GeometryNodeRealizeInstances', 'Geometry')

            bpy.ops.object.convert(target='MESH')
            export_obj = context.view_layer.objects.active
            if export_obj not in created_objects:
                created_objects.append(export_obj)
            if not export_obj.data.polygons:
                raise ValueError('The selected Pathix road produced no mesh faces')

            if self.separate_materials or self.bake_tar:
                before = set(bpy.data.objects)
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.mesh.select_all(action='SELECT')
                bpy.ops.mesh.separate(type='MATERIAL')
                bpy.ops.object.mode_set(mode='OBJECT')
                created_objects.extend(obj for obj in set(bpy.data.objects) - before
                                       if obj not in created_objects)

            export_objects = [obj for obj in created_objects
                              if obj.type == 'MESH' and obj.data.polygons]
            if not export_objects:
                raise ValueError('No exportable mesh parts were produced')
            if self.separate_materials or self.bake_tar:
                for obj in export_objects:
                    obj.name = source.name + '_' + _safe_name(_material_name(obj))

            if self.bake_tar:
                scene.render.engine = 'CYCLES'
                scene.cycles.samples = 16
                for obj in export_objects:
                    name = _material_name(obj)
                    if name == 'road1':
                        _bake_surface_material(context, obj, int(self.tar_resolution),
                                               created_materials, created_images)
                    elif name == 'crub 1':
                        _bake_curb(context, obj, int(self.tar_resolution),
                                   created_materials, created_images)
                    elif name in ('road lines 1', 'CROSS_WALK'):
                        _bake_markings(context, obj, int(self.tar_resolution),
                                       created_materials, created_images)

            bpy.ops.object.select_all(action='DESELECT')
            for obj in export_objects:
                obj.select_set(True)
            context.view_layer.objects.active = export_objects[0]
            result = bpy.ops.export_scene.gltf(
                filepath=filepath,
                export_format='GLB',
                use_selection=True,
                export_apply=False,
            )
            if 'FINISHED' not in result:
                raise RuntimeError('Blender did not finish the GLB export')
            self.report({'INFO'}, 'Exported %d mesh part(s) to %s' %
                        (len(export_objects), filepath))
            return {'FINISHED'}
        except Exception as exc:
            traceback.print_exc()
            self.report({'ERROR'}, 'Pathix GLB export failed: %s' % exc)
            return {'CANCELLED'}
        finally:
            scene.render.engine = old_engine
            scene.cycles.samples = old_samples
            if context.mode != 'OBJECT':
                bpy.ops.object.mode_set(mode='OBJECT')
            for obj in created_objects:
                if obj.name in bpy.data.objects:
                    bpy.data.objects.remove(obj, do_unlink=True)
            if local_group and local_group.users == 0:
                bpy.data.node_groups.remove(local_group)
            for material in created_materials:
                if material.users == 0:
                    bpy.data.materials.remove(material)
            for image in created_images:
                if image.users == 0:
                    bpy.data.images.remove(image)
            bpy.ops.object.select_all(action='DESELECT')
            for obj in previous_selection:
                if obj.name in bpy.data.objects:
                    obj.select_set(True)
            if previous_active and previous_active.name in bpy.data.objects:
                context.view_layer.objects.active = previous_active


def register():
    bpy.utils.register_class(PATHIX_OT_export_jme_glb)


def unregister():
    bpy.utils.unregister_class(PATHIX_OT_export_jme_glb)
