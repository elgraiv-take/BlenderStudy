bl_info = {
    "name": "Fbx Tools",
    "author": "Take@IGC-Matrices",
    "blender": (2, 79, 0),
    "location": "",
    "description": "Fbx Tools",
    "warning": "",
    "tracker_url": "",
    "category": "Import-Export"
    }

import bpy

import ElgraivFbxTools.FbxToolsPanel
import ElgraivFbxTools.FbxToolsExportSetProps
import ElgraivFbxTools.FbxToolsOp

def register():
    import imp

#     imp.reload(ElgraivFbxTools.FbxToolsPanel)
#     imp.reload(ElgraivFbxTools.FbxToolsExportSetProps)

    bpy.utils.register_module(__name__)
    bpy.types.Scene.export_set=bpy.props.PointerProperty(type=ElgraivFbxTools.FbxToolsExportSetProps.FbxExportSetProperty)


def unregister():
    del bpy.types.Scene.export_set
    bpy.utils.unregister_module(__name__)