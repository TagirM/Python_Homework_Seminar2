# Задача 14.
# Напишите программу, которая принимает на вход 2 числа. 
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях (не индексах).
# Position one: 1
# Position two: 3
# Number of elements:5
# -> [-5,-4,-3,-2,-1,0,1,2,3,4,5]
# -> 15

N = input('Количество элементов списка:')
while not N.isdigit():
    N = input('Количество элементов списка:')
N = int(N)
n1 = input('Position one: ')
while not n1.isdigit():
    n1 = input('Position one: ')
n1 = int(n1)
n2 = input('Position two: ')
while not n2.isdigit():
    n2 = input('Position two: ')
n2 = int(n2)
num = []
for i in range(1):
    for j in range(-N, N+1):
        num.append(j)
mult = num[n1-1] * num[n2-1]
print(f'Список -> {num}')
print(f'Произведение элементов на заданных позициях {n1} и {n2} -> {mult}')



