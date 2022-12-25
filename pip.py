# дайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint
from isOdd import isOdd
numbers = []
sum=0
for i in range(10):
    numbers.append(randint(-10, 10))
print(numbers)
for i in range(len(numbers)):
    if isOdd(i)==False:
        sum=sum+numbers[i]
    i+=1
print(sum)



