# 36. Дан список чисел. Создать список, в который попадают числа, 
# описываемые возрастающую последовательность. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. 
# Порядок элементов менять нельзя

import random

lst=[1, 5, 2, 3, 4, 6, 1, 7]
res_lst =[]
index = random.randrange(len(lst))
# index = 7
print(index)
res_lst.append(lst[index])
if index <= len(lst)-2:
    index += 1
    for index in range(index, len(lst)-1):
        if res_lst[-1] < lst[index] < lst[index+1]:
        	res_lst.append(lst[index])
        elif res_lst[-1] < lst[index]:
            res_lst.append(lst[index])
if res_lst[-1] < lst[-1]:
    res_lst.append(lst[-1])
print(res_lst)
