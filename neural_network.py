import cv2
import numpy
import math
from setting import*

#Нейронная сеть с высокой точностью
class HESH_COMPARATOR:

    pi = 3.142857
    
    #разрешение измененного размера 
    resolution_matrix_column = RESOLUTION_MATRIX_COLUMN
    resolution_matrix_line = RESOLUTION_MATRIX_LINE
    
    def __init__(self, suspect_image, warning_image):
        self.suspect_image = suspect_image
        self.warning_image = warning_image
    
    #метод преобразования изображения
    def image_transofrmation(self, image):
        
        if type(image) == str:
            image = cv2.imread(image)
        print("type: ", type(image))
        image = image
        resolution_matrix_column = self.resolution_matrix_column
        resolution_matrix_line = self.resolution_matrix_line
        
        #перевод в оттенки серого
        ret_image, image = cv2.threshold(image, 127, 255, 1)
        
        #обрезка фотографии 
        image = cv2.resize(image, (resolution_matrix_line,resolution_matrix_column))
        return image 

    #дискретное косинусоидальное преобразование
    def dct(self, matrix):
        resolution_matrix_line = self.resolution_matrix_line
        resolution_matrix_column = self.resolution_matrix_column
        matrix_buffer = []
        for i in range(resolution_matrix_line):
            matrix_buffer.append([None for _ in range(resolution_matrix_column)])
        
        for index_line in range(resolution_matrix_line):
            for index_column in range(resolution_matrix_column):
                
                if index_line == 0:
                    ci = 1 / (resolution_matrix_line ** 0.5)

                else:
                    ci = (2 / index_line) ** 0.5
                    
                if index_column == 0:
                    cj = 1 / (resolution_matrix_column ** 0.5)

                else:
                    cj = (2 / index_column) ** 0.5
                
                
                sum = 0
                for index_line_1 in range(resolution_matrix_line):
                    for index_column_1 in range(resolution_matrix_column):
                        
                        matrix_buffer_1 = matrix[index_line_1][index_column_1] * math.cos((2 * index_line_1 + 1) * index_line * 2 * resolution_matrix_line * pi / (2 * resolution_matrix_line)) * math.cos((2 * index_column_1 + 1) * index_line * 2 * resolution_matrix_column * pi / (2 * resolution_matrix_column)) 
                        sum = sum + matrix_buffer_1
                
                matrix_buffer[index_line][index_column] = ci * cj * sum
                
        return matrix_buffer
        
    #формирование хеша
    def magick_transformation_matrix(self, drc_matrix):
        matrix_buffer = []
        bit_array = []
        #создание матрицы [8x8] со сначениями None
        for i in range(8):
            matrix_buffer.append([None for _ in range(8)])
        
        #заполнение пустой матрицы значениями матрицы[64x64] со смещением [line_number + 1][column_number + 1] для предотвращения передачи лишней информации
        for index_line in range(8):
            for index_column in range(8):
                matrix_buffer[index_line][index_column] = drc_matrix[index_line+1][index_column+1]
        
        #среднее значение матрицы
        arithmetic_mean = numpy.mean(matrix_buffer)

        #создание хеша (хеш = список всех значений матрицы) такой хеш позволяет измерять расстояние хэмминга
        for index_line_1 in range(8):
            for index_column_1 in range(8):
                #создаем бинарный хеш (значение матрицы > среднего заполняем 1 иначе 0)
                if (matrix_buffer[index_line_1][index_column_1] > arithmetic_mean).all():
                    bit_array.append(1)
                else:
                    bit_array.append(0)
        
        print(f'bit_array: {bit_array}')
        return bit_array


    #расчет расстояния хэмминга
    def hamming_distance_calculation(self, hesh_suspect_image, hesh_warning_image):
        len_hesh = len(hesh_suspect_image)
        error_count = 0

        #расстояние хэмминга расчитывается путем сравнение хеш значений 
        for index in range (len_hesh):
            if hesh_suspect_image[index] != hesh_warning_image[index]:
                error_count+=1
        print(f'len_hesh {len_hesh}')
        print(f'error_count {error_count}')
        #возврат процента совпадения
        if error_count < 5:
            probability = (10 - error_count) * 10
        else:
            probability = 0
            
        return(probability)
    
    #основная функция  
    def main_nan(self,):
        #преобразовываем входные данные
        suspect_image = self.image_transofrmation(self.suspect_image)
        warning_image = self.image_transofrmation(self.warning_image)
        #высчитываем дискретное косинусоидальную функцию
        suspect_dct_matrix = self.dct(suspect_image)
        warning_dct_matrix = self.dct(warning_image)
        #совершаем преобразования для повышение качества обнаружения объекта
        magic_suspect_dct_matrix = self.magick_transformation_matrix(suspect_dct_matrix)
        magic_warning_dct_matrix = self.magick_transformation_matrix(warning_dct_matrix)
        #получаем вероятность объекта
        probability = self.hamming_distance_calculation(magic_suspect_dct_matrix, magic_warning_dct_matrix)
        
        return probability
        
        
    
    
    
    
    
#доработать
# #нейронная сеть кластиризующая
class NEURAL_FASTER_NETWORK:
    
    
    #возвращает словарь значений ["имя объекта"(str):[вероятность(float), изображение(matrix)]
    
     
    def object_name_and_faster_probability_and_suspect_image():
        accuracy = 0
        lables = LABLES_FASTER_PROBABILITY
        object_counter = 0
        object_name = None
        suspect_image = None
        object_name_and_faster_probability_and_suspect_image = [{object_name:[accuracy, suspect_image]}]
       
        return object_name_and_faster_probability_and_suspect_image
    
    def object_finder():
        
         #работа поиска контуров
        
        object_counter = 1 #подсчет объектов
        local_object_counter = object_counter -1
        for index in range(local_object_counter):
            
            objects = [{}, object_counter]