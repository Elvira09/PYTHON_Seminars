# 13. Пользователь задаёт две строки. 
# Определить количество вхождений одной строки в другой.

from itertools import count


str1 = input('Введите строку: ')
str2 = input('Введите параметр поиска для подсчета вхожденй: ')
# str1 = 'да да нет да нет да'
# str2 = 'да'
counter = str1.count(str2) 
print(counter)
# result = len(str1.split(str2)) - 1
# print(result)


