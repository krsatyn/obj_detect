from ursina import *
from detection import Suspect_Object
from apps_construct import *
from setting import *

import time

#задавание текстуры и объекта
model_name = get_model_name()
suspect_name = get_suspect_name()
model_texture = get_model_texture()
XYZ_index = XYZ_INDEX_CAMERA

#функция изменения оси
def update():
    #вызов функции задавание коэфициентов
    if XYZ_index['stop_word'] == False:
        time.sleep(1)
        print(XYZ_index['stop_word'])
        #вид сбоку
        model_one.rotation_x = model_one.rotation_x + time.dt*XYZ_index['x']
        model_one.rotation_y = model_one.rotation_y + time.dt*XYZ_index['y']
        model_one.rotation_z = model_one.rotation_y + time.dt*XYZ_index['z']
        
        #вид спереди 
        model_two.rotation_x = model_two.rotation_x - time.dt*XYZ_index['x']
        model_two.rotation_y = model_two.rotation_y - time.dt*XYZ_index['y']
        model_two.rotation_z = model_two.rotation_y - time.dt*XYZ_index['z']
        check_image()
    else:
        #вид сбоку
        model_one.rotation_x = model_one.rotation_x + time.dt*XYZ_index['x']
        model_one.rotation_y = model_one.rotation_y + time.dt*XYZ_index['y']
        model_one.rotation_z = model_one.rotation_y + time.dt*XYZ_index['z']
        
        #вид спереди 
        model_two.rotation_x = model_two.rotation_x - time.dt*XYZ_index['x']
        model_two.rotation_y = model_two.rotation_y - time.dt*XYZ_index['y']
        model_two.rotation_z = model_two.rotation_y - time.dt*XYZ_index['z']
        check_image()
        # print("Warning")

#внутренности приложения

window.title = "MetafrastisProsdioristis"    
app = Ursina(borderless=False)

window.size = (800,600)
window.exit_button.enable = True
window.cog_button.enable = False
window.fps_counter.enable = False
window.fullscreen = False


#объекты 
model_one = Entity(model=model_name, scale=20, collider='mesh',  position=(5,0,0), texture=model_texture)
model_one.rotation_z = 90
model_one.rotation_y = 90
model_one.scale = 10

model_two = Entity(model=model_name, scale=20, collider='mesh', texture=model_texture)
model_two.scale = 10

#объекты текст
suspect_text = Text(text=f'Подаваемое изображение: {suspect_name} \nStatus:', color=color.green, x=0.3, y=-0.25)
wallpaper = Entity(model='quad', scale=(30,30), texture="assets/sky_cloud", z=10)
status_bar = XYZ_index['status_bar']

# #кнопки
# button_start = Button(text="start scanning", color=color.black, position=(-5,0,0), scale=.25)
# button_start.on_click = check_image

#подаваемое изображение 
Entity(model='quad', texture='Image_Source/Suspect/suspect.jpg', scale=4, position=(-5,0,0))

print("index", XYZ_index['status_bar'])
#конец внутренностей приложения

app.run()