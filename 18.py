# 18. Реализовать алгоритм перемешивания списка. 

# ИСпользована функция, нужно ДОДЕЛАТЬ просто кодом
import random

lst = list(range(10))
print(lst, ' - исходный список')

random.shuffle(lst)
print(lst, ' - перемешаный список')

