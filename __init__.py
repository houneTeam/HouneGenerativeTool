bl_info = {
    "name": "HouneGenerativeTool",
    "blender": (3, 62, 0),
    "category": "3D View",
    "version": (1, 0, 0),
    "author": "HouneTeam",
    "description": "Addon that generates and executes Python scripts for Blender based on user prompts.",
    "location": "3D View > Sidebar > HouneTools",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
    "support": "COMMUNITY",
    "category": "3D View",
}

import bpy
from .ui import HouneToolsPanel
from .properties import register_properties, unregister_properties

def register():
    register_properties()
    bpy.utils.register_class(HouneToolsPanel)

def unregister():
    bpy.utils.unregister_class(HouneToolsPanel)
    unregister_properties()

if __name__ == "__main__":
    register()
