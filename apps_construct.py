import numpy as np
import cv2
import random as rnd
from mss import mss
from PIL import Image
import concurrent.futures

from detection import Suspect_Object
from setting import *
from neural_network import *

warning_image = 'Image_Source/Suspect/sumka.jpg'
 
Model_Info = Suspect_Object
model_info = Model_Info.object_detection_selection()

ACCURACY_NETWORK = HESH_COMPARATOR

global XYZ_index_camera 
XYZ_index_camera  = XYZ_INDEX_CAMERA
 
#Возвращает имя модели принимая название 3D объекта
def get_model_name():
    model_name = model_info + '_obj.obj'
    return model_name

#Возвращает имя модели принимая название текстуры для 3D объекта
def get_model_texture():
    model_textute = model_info + '.png'
    return model_textute

#возвращает имя подозреваемого объекта
def get_suspect_name():
    suspect_name = model_info + '.jpg'
    return suspect_name


#постановка в очередь
def get_queue():
    queue = []
    
    #реализация заполения очереди
    
    
    
    return queue

#захват части экрана 

#отвечает за смещение правой камеры, возвращает словарь с коэфициентами для осей x,y,z или False в случае прохода условия
def get_XYZ_index_camera(input_probability):

    probability = input_probability

    
    #проверка текущей вероятности с требуемой ввероятностью (если совпало изменает коэф поворота если нет то останавливает вращение
    # вместо остановки будет подача сигнала)
    if probability < SENSITIVE_PROBABILITY:
        XYZ_index_camera['y'] = 1
        XYZ_index_camera['stop_word'] = False
        XYZ_index_camera['status_bar'] = STATUS_BAR_PROCESSING = Text(text=f'Object undefine, please wait. \n probability: {probability}', color=color.green, x=0.3, y=-0.3)
        #XYZ_index_camera['status_bar'] = STATUS_BAR_WARNING = Text(text=f'Please wait, the object has not been identified as dangerous. \n probability: {probability}', color=color.red, x=0.3, y=-0.3)
        print(f'warning {probability} ')
        return XYZ_index_camera

    else:
        #print(f'ep {probability} ')
        XYZ_index_camera['y'] = 0
        XYZ_index_camera['stop_word'] = True
        XYZ_index_camera['status_bar'] = STATUS_BAR_WARNING = Text(text=f'WARNING,PROHIBITED ITEM DETECTED. \n probability: {probability}', color=color.red, x=0.3, y=-0.3)
        print(f'warning {probability} ')
        return XYZ_index_camera

#получение информации с экрана
def get_screenshoot_input():
    #параметры для ввода
    screen_info_1 = {'left': 350, 'top': 150, 'width': 300, 'height': 300}
    screen_info_2 = {'left': 750, 'top': 150, 'width': 300, 'height': 300}
    #сама программа перехвата
    with mss() as sct:

            screenShot_1 = sct.grab(screen_info_1)        
            right_camera_image = Image.frombytes(
                'RGB', 
                (screenShot_1.width, screenShot_1.height), 
                screenShot_1.rgb, 
            )
            
            cv2.imshow('right_camera', np.array(right_camera_image))
            
            screenShot_2 = sct.grab(screen_info_2)        
            upper_camera_image = Image.frombytes(
                'RGB', 
                (screenShot_2.width, screenShot_2.height), 
                screenShot_2.rgb, 
            )
            cv2.imshow('upper_camera', np.array(upper_camera_image))
            
            image_package = {'right_camera_image':np.asarray(right_camera_image, np.uint8), 'upper_camera_image':np.asarray(upper_camera_image, np.uint8)}
            
            return image_package
            
def check_image():
    
    image_package = get_screenshoot_input()
    #распаковка получаемых изображений с 3д модели
    right_camera_image = image_package['right_camera_image']
    upper_camera_image = image_package['upper_camera_image']
    
    #получение реальной картнки
    #suspect_name = get_suspect_name()
    suspect_image = 'Image_Source/Suspect/suspect.jpg'

    #создание потоков для двух камер
    probability_class_right_camera_image = ACCURACY_NETWORK(suspect_image, right_camera_image)
    probability_class_upper_camera_image = ACCURACY_NETWORK(suspect_image, upper_camera_image )
    #
    with concurrent.futures.ThreadPoolExecutor() as camera_image:
        future_right_camera_image = camera_image.submit(probability_class_right_camera_image.main_nan)
        future_upper_camera_image = camera_image.submit(probability_class_upper_camera_image.main_nan)
        probability_right = future_right_camera_image.result()
        probability_upper = future_upper_camera_image.result()
    #
    probability = max(probability_right,probability_upper)
    #
    print(f'probability_right: {probability_right}')
    print(f'probability_upper: {probability_upper}')
    #
    probability = 0
    XYZ_index_camera = get_XYZ_index_camera(probability)
    #
    return(XYZ_index_camera)