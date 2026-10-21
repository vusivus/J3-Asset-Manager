"""Print Pathix and building material wiring without modifying the blend."""
import bpy

for material in bpy.data.materials:
    name = material.name.lower()
    if not any(word in name for word in ('facade', 'brick', 'side walk', 'road1', 'storeinterior', 'trim')):
        continue
    print('MATERIAL', material.name, flush=True)
    if not material.use_nodes:
        continue
    for node in material.node_tree.nodes:
        if node.bl_idname == 'ShaderNodeTexImage':
            image = node.image
            links = [link.from_node.name + '.' + link.from_socket.name
                     for link in node.inputs['Vector'].links]
            print('  IMAGE', node.name, image.name if image else None,
                  tuple(image.size) if image else None,
                  image.filepath if image else None,
                  'vector=', links, 'extension=', node.extension,
                  'interpolation=', node.interpolation, flush=True)
        elif node.bl_idname in ('ShaderNodeMapping', 'ShaderNodeUVMap', 'ShaderNodeTexCoord'):
            detail = ''
            if node.bl_idname == 'ShaderNodeMapping':
                detail = 'scale=' + str(tuple(node.inputs['Scale'].default_value))
            if node.bl_idname == 'ShaderNodeUVMap':
                detail = 'uv=' + node.uv_map
            print('  UVNODE', node.name, node.bl_idname, detail, flush=True)

for obj in bpy.data.objects:
    if obj.type != 'MESH':
        continue
    if any(word in obj.name.lower() for word in ('building', 'road', 'balcon', 'wall')):
        print('OBJECT', obj.name, 'uv=', [layer.name for layer in obj.data.uv_layers],
              'materials=', [slot.material.name if slot.material else None for slot in obj.material_slots], flush=True)
