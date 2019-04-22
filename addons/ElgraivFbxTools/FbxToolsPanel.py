'''
Created on 2018/09/17

@author: take
'''

import bpy

class ToolsPanel:
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "FbxTools"

class FBXTOOL_UL_export_set(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):

        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            row = layout.row(align=True)
            row.prop(item, "name", text="", emboss=False)
        elif self.layout_type == 'GRID':
            layout.alignment = 'CENTER'
            layout.label(text="", icon_value=icon)

class FBXTOOL_UL_export_item(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            row = layout.row(align=True)
            row.prop(item, "name", text="", emboss=False)
        elif self.layout_type == 'GRID':
            layout.alignment = 'CENTER'
            layout.label(text="", icon_value=icon)


class FbxToolsPanel(ToolsPanel,bpy.types.Panel):
    bl_idname="DATA_PT_fbx_"
    bl_label = "FBX Export Tools"

    def __init__(self):
        pass

    @classmethod
    def poll(cls, context):
        return True

    def draw(self, context):
        layout = self.layout
        setList=context.scene.export_set
        row = layout.row()
        col = row.column()
        col.template_list("FBXTOOL_UL_export_set", "", setList, "export_set_list", setList, "active_index", rows=1)

        col = row.column()
        sub = col.column(align=True)
        sub.operator("scene.fbx_export_set_add", icon='ZOOMIN', text="")
        sub.operator("scene.fbx_export_set_remove", icon='ZOOMOUT', text="")
        if len(setList.export_set_list)>0:
            row = layout.row()
            current=setList.export_set_list[setList.active_index]
            row.operator("export_scene.fbx_ex", text="Export")
            row = layout.row()
            row.prop(current,"name",text="Name")
            row = layout.row()
            row.prop(current,"save_path",text="Path")
            row = layout.row()
            row.template_list("FBXTOOL_UL_export_item", "", current, "object_list",current,"active_object_index")


