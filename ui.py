import bpy

class AIToolkitPanel(bpy.types.Panel):
    bl_label = "AI Toolkit"
    bl_idname = "VIEW3D_PT_ai_toolkit"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "AI Toolkit"

    def draw(self, context):
        layout = self.layout
        props = context.scene.ai_toolkit
        
        box = layout.box()
        box.label(text="Input Image:", icon='IMAGE_DATA')
        box.prop(props, "image_path", text="")
        box.prop(props, "prompt", text="Model Name")
        
        layout.separator()
        layout.operator("aitoolkit.generate", icon='PLAY', text="GENERATE")

class SettingsPanel(bpy.types.Panel):
    bl_label = "Settings"
    bl_idname = "VIEW3D_PT_settings"
    bl_parent_id = "VIEW3D_PT_ai_toolkit"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon='SETTINGS')

    def draw(self, context):
        layout = self.layout
        props = context.scene.ai_toolkit
        
        # Подвкладка Hunyuan 3D (сворачиваемая через box + prop или просто box)
        sub_box = layout.box()
        sub_box.label(text="Hunyuan 3D Server", icon='WORLD')
        sub_box.prop(props, "space_id", text="")
        sub_box.label(text="Status: Running on L40S", icon='INFO')

class ManualPanel(bpy.types.Panel):
    bl_label = "Manual"
    bl_idname = "VIEW3D_PT_manual"
    bl_parent_id = "VIEW3D_PT_ai_toolkit"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon='HELP')

    def draw(self, context):
        self.layout.operator("aitoolkit.open_manual", icon='URL')
