import bpy
import os
from .api_client import run_3d_logic

class AIToolkitGenerate(bpy.types.Operator):
    bl_idname = "aitoolkit.generate"
    bl_label = "GENERATE"
    bl_description = "Run Hunyuan 3D generation via API"

    def execute(self, context):
        props = context.scene.ai_toolkit
        
        # Превращаем относительный путь Blender (//) в полный системный путь
        image_path = bpy.path.abspath(props.image_path)
        
        # Проверяем, выбран ли файл и существует ли он
        if not image_path or not os.path.exists(image_path):
            self.report({'ERROR'}, f"Файл изображения не найден: {image_path}")
            return {'CANCELLED'}
        
        self.report({'INFO'}, "Connecting to AI... Blender will freeze for a bit.")
        
        # Вызываем логику из api_client.py
        try:
            # Передаем путь к картинке и имя модели (промпт)
            success = run_3d_logic(image_path, props.prompt, props.space_id)
            if success:
                self.report({'INFO'}, "Model imported successfully!")
            else:
                self.report({'ERROR'}, "Generation failed or GLB not found.")
        except Exception as e:
            self.report({'ERROR'}, f"Error: {str(e)}")
            
        return {'FINISHED'}

class AIToolkitOpenManual(bpy.types.Operator):
    bl_idname = "aitoolkit.open_manual"
    bl_label = "Open Manual"

    def execute(self, context):
        # Ссылка на страницу модели Hunyuan3D
        bpy.ops.wm.url_open(url="https://huggingface.co")
        return {'FINISHED'}
