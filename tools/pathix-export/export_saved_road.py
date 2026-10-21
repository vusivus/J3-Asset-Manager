"""Rebuild a portable road export from a saved blend, leaving the blend untouched."""
import importlib.util
import os
import sys
import bpy

folder = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('pathix_export_current', os.path.join(folder, 'pathix_jme_export.py'))
exporter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(exporter)
exporter.register()
roads = [obj for obj in bpy.context.scene.objects if exporter._pathix_modifier(obj)]
if len(roads) != 1:
    raise RuntimeError('Expected one Pathix road, found: ' + repr([obj.name for obj in roads]))
road = roads[0]
print('PATHIX_SOURCE', road.name, flush=True)
print('PATHIX_MATERIALS', [mat.name for mat in road.data.materials if mat], flush=True)
bpy.ops.object.select_all(action='DESELECT')
road.hide_set(False)
road.select_set(True)
bpy.context.view_layer.objects.active = road
output = os.path.join(folder, 'Carribean_Boys_Road_fixed.glb')
result = bpy.ops.pathix.export_jme_glb(filepath=output, content='ROAD_LIGHTS', bake_tar=True, tar_resolution='2048')
if 'FINISHED' not in result:
    raise RuntimeError('Road export did not finish: ' + repr(result))
print('PATHIX_EXPORTED', output, flush=True)
