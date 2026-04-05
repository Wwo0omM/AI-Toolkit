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
import subprocess
import sys

# --- АВТО-УСТАНОВКА GRADIO ---
def install_dependencies():
    try:
        import gradio_client
    except ImportError:
        print("AI Toolkit: Installing gradio_client...")
        # Запускаем pip внутри встроенного Python в Blender
        subprocess.check_call([sys.executable, "-m", "pip", "install", "gradio_client", "--user"])

install_dependencies()

from .properties import AIToolkitProperties
from .operators import AIToolkitGenerate, AIToolkitOpenManual
from .ui import AIToolkitPanel, SettingsPanel, ManualPanel

classes = (
    AIToolkitProperties,
    AIToolkitGenerate,
    AIToolkitOpenManual,
    AIToolkitPanel,
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
