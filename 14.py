# 14. Подсчитать сумму цифр в вещественном числе.


number = float(input('Введите вещественное число:  '))
# number = 253.8969
str_number = str(number) 
str_number = str_number.replace('.', '') 
list_str = list(str_number) 
list_number = list(map(int, list_str)) #переводим в число каждый элемент списка #https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-map/
summ = sum(list_number)
print(summ)

