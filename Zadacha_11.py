# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
n = float(input(
    'Введите вещественное число со количеством знаков после запятой не более 4: '))
myNumber = 0
i = 0
while n % 10 != 0:
    n = n*10
    i += 1
    if i > 4:  # данное условие необходимо для верного решения
        break
myNumber = int(n//10)
print(myNumber)
sumNumber = 0
while myNumber > 0:
    sumNumber = sumNumber+myNumber % 10
    myNumber = myNumber // 10
print(f'Сумма составляющих число цифр с 4 знаками после запятой равно {sumNumber}')
