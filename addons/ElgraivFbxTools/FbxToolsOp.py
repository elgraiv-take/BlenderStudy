'''
Created on 2018/09/17

@author: take
'''

import bpy

class FbxToolsExportOp(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "export_scene.fbx_ex"
    bl_label = "Export Fbx set"

    def execute(self, context):
        current=context.scene.export_set.export_set_list[context.scene.export_set.active_index]
        if len(current.save_path)<=0:
            return {'FINISHED'}
        layers=[b for b in context.scene.layers]
        for i in range(len(layers)):
            context.scene.layers[i]=True
        bpy.ops.object.select_all(action='DESELECT')
        for n in current.object_list:
            o=context.scene.objects[n.name]
            o.select=True
        bpy.ops.export_scene.fbx(filepath=current.save_path, check_existing=True, filter_glob="*.fbx", version='BIN7400', use_selection=True,apply_scale_options="FBX_SCALE_ALL", object_types={'EMPTY', 'ARMATURE', 'MESH'})

        for i in range(len(layers)):
            context.scene.layers[i]=layers[i]
        return {'FINISHED'}

class FbxToolsExportSetAddOp(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "scene.fbx_export_set_add"
    bl_label = "Add Export Set"

    def execute(self, context):
        newItem=context.scene.export_set.export_set_list.add()
        newItem.name="NewSet"
        for o in context.selected_objects:
            item=newItem.object_list.add()
            item.name=o.name
        return {'FINISHED'}

class FbxToolsExportSetRemoveOp(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "scene.fbx_export_set_remove"
    bl_label = "Remove Export Set"

    def execute(self, context):
        setList=context.scene.export_set
        delIndex=setList.active_index
        setList.export_set_list.remove(delIndex)
        return {'FINISHED'}