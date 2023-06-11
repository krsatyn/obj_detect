import os

from setting import*

#класс для определения объекта 
class Suspect_Object:
    
    #функция выбора подозреваемого объекта
    def object_detection_selection():
        files_catalog = os.listdir(WARNING_SOURCE)
        
        print(f'Введите название подозреваемого объекта: \n {files_catalog} \n')
        suspect_object = str(input('имя:' ))
        
        
        # files_catalog = os.listdir(SUSPECT_SOURCE + '/' + suspect_object)
        
        # print(f' выбран {suspect_object} \n  {files_catalog} \n выберите объект: \n')
        # suspect_object = str(input("имя объекта: "))

        suspect_object = suspect_object.split('.')
        return suspect_object[0]