# 16. Задать список из n чисел последовательности (1+1n)n 
# и вывести на экран их сумму

# [1, 2, 3, 4, 5, 6, 7, 8]  
# [2, 6, 12, 20, 30, 42, 56, 72]   => 240



n = int(input('Ввведите количество членов последовательности:  '))
start = int(input('Ввведите стартовую позицию словаря:  '))
# n = 8
# start = -5

initial = list(range(start, start+n))
print(initial, ' - Исходная последовательность')
temp = 1
result = []

for i in range(n):	
	temp = initial[i] * (1 + initial[i])
	result.append(temp)
print(result,  ' - Результирующая последовательность')

summ = sum(result)
print(summ, ' - Сумма элементов результирующей последовательности')

