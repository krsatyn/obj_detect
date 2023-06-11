from ursina import *
#НАСТРОЙКИ ПРОЕКТА

#Зависимости 
IMAGE_SOURCE = 'Image_Source'
DATA_SETS_SOURCE = 'Image_Source/Data_Sets/pistol_set'
SUSPECT_SOURCE = 'Image_Source/Suspect/'
WARNING_SOURCE = 'Image_Source/Warning_object/Gun/'

#настройка нейронной сети
LABLES_ACCURACY_PROBABILITY = ['pistol', 'knife']
LABLES_FASTER_PROBABILITY = ['knife', 'pistol']

#настройки создания datasets
BATCH_SIZE = 256
IMAGE_SIZE = (100, 100)

#параметры проверки объектов
SENSITIVE_PROBABILITY = 60
BLUNT_PROBABILITY = 0.6
RESOLUTION_MATRIX_COLUMN = 32
RESOLUTION_MATRIX_LINE = 32


# информация об объекте
STATUS_BAR_PROCESSING = Text(text='Object undefine, please wait', color=color.green, x=0.3, y=-0.3)
STATUS_BAR_WARNING = Text(text='WARNING,PROHIBITED ITEM DETECTED', color=color.red, x=0.3, y=-0.3)

#параметры настройки коэф
X1 = 0
Y1 = 0
Z1= 0
STOP_WORD = False
XYZ_INDEX_CAMERA = {'x':X1,'y':Y1,'z':Z1, 'stop_word': STOP_WORD, 'status_bar':Text(text='Object undefine, please wait', color=color.green, x=0.3, y=-0.3)}