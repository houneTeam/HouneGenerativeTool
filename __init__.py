bl_info = {
    "name": "HouneGenerativeTool",
    "blender": (3, 6, 2),
    "category": "3D View",
    "version": (1, 0, 1),
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
import ollama

def register_properties():
    bpy.types.Scene.houne_prompt = bpy.props.StringProperty(name="Prompt")

def unregister_properties():
    del bpy.types.Scene.houne_prompt

class HouneToolsPanel(bpy.types.Panel):
    bl_label = "HouneGenerativeTool"
    bl_idname = "VIEW3D_PT_houne_tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "HouneTools"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.prop(scene, "houne_prompt", text="Prompt")
        layout.operator("wm.execute_houne_prompt", text="Generate")

class ExecuteHounePromptOperator(bpy.types.Operator):
    bl_idname = "wm.execute_houne_prompt"
    bl_label = "Execute Houne Prompt"

    def execute(self, context):
        prompt = context.scene.houne_prompt
        script_code = generate_blender_script(prompt)
        exec(script_code)
        return {'FINISHED'}

def generate_blender_script(query):
    # Добавляем системный промпт, чтобы бот понимал, что от него ожидается код на Python для Blender
    system_prompt = "You are an assistant that generates only valid Python scripts for Blender using the bpy module. Based on the user's requests, you should always return code that can be copied directly into Blender's script editor and executed without modification. Do not include any explanations, comments, or text outside of the code. If the request is unclear, try to interpret it as a task to be performed in Blender."

    response = ollama.chat(model='llama3.1', messages=[
        {
            'role': 'system',
            'content': system_prompt,
        },
        {
            'role': 'user',
            'content': query,
        },
    ])

    script_code = response['message']['content']
    return script_code.strip()

def register():
    register_properties()
    bpy.utils.register_class(HouneToolsPanel)
    bpy.utils.register_class(ExecuteHounePromptOperator)

def unregister():
    bpy.utils.unregister_class(HouneToolsPanel)
    bpy.utils.unregister_class(ExecuteHounePromptOperator)
    unregister_properties()

if __name__ == "__main__":
    register()