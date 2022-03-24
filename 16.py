# 16. Задать список из n чисел последовательности (1+1n)n 
# и вывести на экран их сумму

# Вариант 1
print('Вариант 1')
# [3, 12, 156, 24492, 599882556]  => 599907219


n = int(input('Ввведите количество членов последовательности:  '))
start = int(input('С какого числа начинать последовательность :  '))

result = [start]
for i in range(n-1):	
	result.append(result[i] * (1 + result[i]))
print(result,  ' - Результирующая последовательность')

summ = sum(result)
print(summ, ' - Сумма элементов результирующей последовательности')



# Вариант 2
print('\nВариант 2')
# [3, 4, 5, 6, 7]  
# [12, 20, 30, 42, 56]   => 160

n = int(input('Ввведите количество членов последовательности:  '))
start = int(input('Ввведите стартовую позицию отсчета :  '))

initial = list(range(start, start+n))
# print(initial, ' - Исходная последовательность')

result = []
for i in range(n):	
	result.append(initial[i] * (1 + initial[i]))
print(result,  ' - Результирующая последовательность')

summ = sum(result)
print(summ, ' - Сумма элементов результирующей последовательности')

