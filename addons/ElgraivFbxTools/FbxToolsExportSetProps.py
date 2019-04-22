'''
Created on 2018/09/17

@author: take
'''

import bpy

class FbxExportItem(bpy.types.PropertyGroup):
    name=name=bpy.props.StringProperty()

bpy.utils.register_class(FbxExportItem)

class FbxExportSet(bpy.types.PropertyGroup):
    name=bpy.props.StringProperty()
    save_path=bpy.props.StringProperty()
    active_object_index=bpy.props.IntProperty()
    object_list=bpy.props.CollectionProperty(type=FbxExportItem)

bpy.utils.register_class(FbxExportSet)

class FbxExportSetProperty(bpy.types.PropertyGroup):
    active_index=bpy.props.IntProperty()
    export_set_list=bpy.props.CollectionProperty(type=bpy.types.FbxExportSet)