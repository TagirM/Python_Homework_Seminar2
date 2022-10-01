# Задача 15.
# Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random

from random import randint
my_list = [56, 89, 465, 34, 91, 6]
print(f'Исходный список: {my_list}')
for i in range(len(my_list)):
    my_list.insert(randint(i,len(my_list) - 1), my_list[i])
    del my_list[i]
print(f'Список после перемешивания: {my_list}')
