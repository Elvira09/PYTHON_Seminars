# 5. Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

a = int(input('Введите  число '))
print(a)
if (a % 5 == 0 and a % 10 == 0) or (a % 15 == 0 and a % 30 != 0):
	print('Введенное число кратно 5 и 10 или 15 но не 30')
else:
	print('Введенное число НЕ кратно 5 и 10 или 15 но не 30')
