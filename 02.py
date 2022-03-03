# 2. Найти максимальное из пяти чисел

import random #подключение модуля случайных чисел random

# Вариант 1
num1 = []
for i in range(5):
    num1.append(random.randint(0, 100)) #заполнение списка 5-ю случайными числами от 0 до 100
print(num1) 
max1 = num1[0]
for i in num1:
	if i > max1:
		max1 = i
print(max1)

# Вариант 2
num2 = [random.randint(0, 100) for i in range(5)]
print(num2) 
max2 = max(num2)
print(max2)

