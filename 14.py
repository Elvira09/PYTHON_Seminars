# 14. Подсчитать сумму цифр в вещественном числе.


number = float(input('Введите вещественное число:  '))
# number = 253.8969
str_number = str(number) #переводим в строку
str_number = str_number.replace('.', '') #удаляем точку
# print(str_number)
list_str = list(str_number) #переводим в список строк 
# print(list_str)
list_number = map(int, list_str)
# print(list_number)
summ = sum(list_number)
print(summ)

