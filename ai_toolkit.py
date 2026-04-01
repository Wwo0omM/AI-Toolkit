bl_info = {
    "name": "AI Toolkit",
    "author": "Nelly",
    "version": (1, 0, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > AI Toolkit",
    "description": "AI tools for 3D generation",
    "category": "3D View",
}

import bpy


# =========================
# PROPERTIES
# =========================

class AIToolkitProperties(bpy.types.PropertyGroup):

    mode: bpy.props.EnumProperty(
        name="Mode",
        items=[
            ("TEXT", "Text", "Generate 3D model from text description", 'TEXT', 0),
            ("IMAGE", "Image", "Generate 3D model from image", 'IMAGE_DATA', 1)
        ],
        default="TEXT"
    )

    prompt: bpy.props.StringProperty(
        name="Prompt",
        description="Describe your model",
        default="",
        options={'TEXTEDIT_UPDATE'}
    )

    image_path: bpy.props.StringProperty(
        name="Image Path",
        subtype='FILE_PATH'
    )

    image_input_mode: bpy.props.EnumProperty(
        name="Image Input Mode",
        items=[
            ("SINGLE", "Single", "Single image input"),
            ("FOUR", "Four", "Four image inputs")
        ],
        default="SINGLE"
    )

    image_path_1: bpy.props.StringProperty(
        name="Image Path 1",
        subtype='FILE_PATH'
    )

    image_path_2: bpy.props.StringProperty(
        name="Image Path 2",
        subtype='FILE_PATH'
    )

    image_path_3: bpy.props.StringProperty(
        name="Image Path 3",
        subtype='FILE_PATH'
    )

    image_path_4: bpy.props.StringProperty(
        name="Image Path 4",
        subtype='FILE_PATH'
    )

# =========================
# GENERATE OPERATOR
# =========================

class AIToolkitGenerate(bpy.types.Operator):
    bl_idname = "aitoolkit.generate"
    bl_label = "GENERATE"

    def execute(self, context):
        props = context.scene.ai_toolkit

        if props.mode == "TEXT":
            self.report({'INFO'}, f"Prompt: {props.prompt}")
            print("TEXT:", props.prompt)

        elif props.mode == "IMAGE":
            if props.image_input_mode == 'SINGLE':
                self.report({'INFO'}, f"Image: {props.image_path}")
                print("IMAGE:", props.image_path)
            else:
                images = [props.image_path_1, props.image_path_2, props.image_path_3, props.image_path_4]
                self.report({'INFO'}, f"Images: {images}")
                print("IMAGES:", images)

        return {'FINISHED'}


# =========================
# OPEN MANUAL OPERATOR
# =========================

class AIToolkitOpenManual(bpy.types.Operator):
    bl_idname = "aitoolkit.open_manual"
    bl_label = "Open Manual"

    def execute(self, context):
        bpy.ops.wm.url_open(url="https://example.com")
        return {'FINISHED'}


# =========================
# UI PANELS
# =========================

class AIToolkitPanel(bpy.types.Panel):
    bl_label = "AI Toolkit"
    bl_idname = "VIEW3D_PT_ai_toolkit"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "AI Toolkit"

    def draw(self, context):
        layout = self.layout
        props = context.scene.ai_toolkit

        # MODE
        layout.label(text="Generation type")
        layout.prop(props, "mode", expand=True)

        layout.separator()

        # TEXT MODE
        if props.mode == "TEXT":
            box = layout.box()
            box.label(text="Prompt")

            col = box.column()
            col.prop(props, "prompt", text="", expand=True) 

        # IMAGE MODE
        elif props.mode == "IMAGE":
            box = layout.box()
            box.label(text="Image Input")
            box.prop(props, "image_input_mode", expand=True)

            if props.image_input_mode == 'SINGLE':
                box.prop(props, "image_path", text="")
            else:
                for i in range(1, 5):
                    box.prop(props, f"image_path_{i}", text=f"Image {i}")
        layout.separator()
        
        layout.operator("aitoolkit.generate", icon='PLAY')

class SettingsPanel(bpy.types.Panel):
    bl_label = "Settings"
    bl_idname = "VIEW3D_PT_settings"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "AI Toolkit"
    bl_parent_id = "VIEW3D_PT_ai_toolkit"
    bl_options = {'DEFAULT_CLOSED'}

    
    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon='SETTINGS')

    def draw(self, context):
        layout = self.layout
        layout.label(text="Settings will be here...")


class ManualPanel(bpy.types.Panel):
    bl_label = "Manual"
    bl_idname = "VIEW3D_PT_manual"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "AI Toolkit"
    bl_parent_id = "VIEW3D_PT_ai_toolkit"
    bl_options = {'DEFAULT_CLOSED'}

    
    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon='HELP')

    def draw(self, context):
        layout = self.layout

        layout.label(text="Open documentation")
        layout.operator("aitoolkit.open_manual", icon='URL')


# =========================
# REGISTER
# =========================

classes = (
    AIToolkitProperties,
    AIToolkitGenerate,
    AIToolkitPanel,
    AIToolkitOpenManual,
    SettingsPanel,
    ManualPanel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.ai_toolkit = bpy.props.PointerProperty(type=AIToolkitProperties)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.ai_toolkit


if __name__ == "__main__":
    register()