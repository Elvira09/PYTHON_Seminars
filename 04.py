# 4. Показать первую цифру дробной части числа

a = float(input('Введите дробное число '))
r = int((a % 1) * 10)
print(r, ' - первая цифра дробной части числа')

