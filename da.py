#задача 3
#ввод данных
stroka = str(input("Введите строку \n :"))
#преобразование в список
stroka = list(stroka)
#перезапись с верхним регистром первого и последнего элемента списка
stroka[0] = stroka[0].title()
stroka[-1] = stroka[-1].title()
#преобразование в строку
stroka = "".join(stroka)

print(f'stroka:{stroka}')