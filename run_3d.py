'''
Источник https://huggingface.co/spaces/Jbowyer/Hunyuan3D-2.1
Для активации в командной сроке набрать " pyton run_3d.py / путь к файлу"
'''

import os
import time
import shutil  
from gradio_client import Client, handle_file

# 1. Подключение
REPO_ID = "Jbowyer/Hunyuan3D-2.1" 
client = Client(REPO_ID, httpx_kwargs={"timeout": 150.0}) 

# 2. Путь к картинке
input_image = r"C:\Program Files\Blender Foundation\Blender 5.1\5.1\scripts\addons_core\ai_toolkit\super_fish.jpg"

print(f" Подключаюсь к {REPO_ID}...")

try:
    # 3. Отправка
    job = client.submit(
        image=handle_file(input_image),
        mv_image_front=None, mv_image_back=None, mv_image_left=None, mv_image_right=None,
        steps=30, guidance_scale=5.0, seed=1234, octree_resolution=256,
        check_box_rembg=True, num_chunks=8000, randomize_seed=True,
        api_name="/generation_all"
    )

    # 4. Ожидание
    while not job.done():
        status = job.status()
        print(f" Статус: {status.code} | Очередь: {status.rank}/{status.queue_size}", end="\r")
        time.sleep(2) 

    # 5. Поиск файла
    print("\n Ищу модель...")
    result = job.result()
    
    def find_glb(data):
        if isinstance(data, str) and data.endswith(".glb"): return data
        if isinstance(data, (list, tuple)):
            for item in data:
                found = find_glb(item)
                if found: return found
        if isinstance(data, dict):
            for v in data.values():
                found = find_glb(v)
                if found: return found
        return None

    model_path = find_glb(result)
    
    # 6. Сохранение на Рабочий стол
    if model_path:
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        final_dest = os.path.join(desktop, "super_fish_model.glb")
        shutil.copy(model_path, final_dest)
        print(f" Готово! Файл на Рабочем столе: {final_dest}")
    else:
        print(" Файл .glb не найден в ответе.")

except Exception as e:
    print(f"\n Ошибка: {e}")