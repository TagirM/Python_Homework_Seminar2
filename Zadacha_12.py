# Задача 11.
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def listN(n):
    b = []
    element = 1
    for i in range(n):
        b.append(element)
        element = element*(i+2)
    return b

n = input('Введите число N: ')
while not n.isdigit():
    n = input('Введите число N: ')
n = int(n)
print(f'Набор произведений чисел от 1 до N {listN(n)}')
