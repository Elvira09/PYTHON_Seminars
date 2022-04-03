# 25. Написать программу преобразования десятичного числа в двоичное

# 456 => 111001000
# 255 => 11111111
# 38 => 100110

num = int(input('Введите целое число: '))

# Вариант 1
print('Вариант 1')

b_num = bin(num)
print(b_num, ' - встроенная функция')

# Вариант 2
print('\nВариант 2')

b_num = ''
while num > 0:
    b_num = str(num % 2) + b_num
    num = num // 2
print(b_num, ' - цикл')







# Дополнительно:
# перевести в десятичную

# num_bin = str(input("введите двоичное число: "))
# x = len(num_bin-1)
# num_dec = 0
# for i in num_bin:
#     num_dec += (2 * int(i)) ** x
#     x -= 1
# print(num_dec)

# # перевести в шестнадцатиричную

# print(hex(num))







