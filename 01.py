# 1. По двум заданным числам проверить является ли одно квадратом второго 

number1 = int(input('Введите первое число '))
number2 = int(input('Введите второе число '))
if number1 ** 2 == number2:
	print(f'Второе число {number2} является квадратом первого {number1}')
else:
	print(f'Второе число {number2} НЕ является квадратом первого {number1}')


