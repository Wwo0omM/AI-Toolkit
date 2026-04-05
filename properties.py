import bpy

class AIToolkitProperties(bpy.types.PropertyGroup):
    prompt: bpy.props.StringProperty(
        name="Name", 
        default="MyModel"
    )
    image_path: bpy.props.StringProperty(
        name="Image Path", 
        subtype='FILE_PATH'
    )
    #  Выбор сервера для Hunyuan
    space_id: bpy.props.EnumProperty(
        name="HuggingFace Space",
        items=[
            ("Jbowyer/Hunyuan3D-2.1", "Hunyuan3D-2.1 (L40S)", "Running on L40S GPU"),
            ("tencent/Hunyuan3D-2", "Hunyuan3D-2 (Official)", "Official Tencent Space"),
        ],
        default="Jbowyer/Hunyuan3D-2.1"
    )
