import bpy

def register_properties():
    bpy.types.Scene.houne_prompt = bpy.props.StringProperty(name="Prompt")

def unregister_properties():
    del bpy.types.Scene.houne_prompt
