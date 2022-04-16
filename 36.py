# 36. Дан список чисел. Создать список, в который попадают числа, 
# описываемые возрастающую последовательность. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. 
# Порядок элементов менять нельзя

import random

lst = [1, 5, 2, 3, 4, 6, 1, 7]
print(lst)

print('\nВариант 1')
i = random.randrange(len(lst))
# i = 0
print(i, ' - стартовый индекс')

res_lst = []
res_lst.append(lst[i])

for i in range(i+1, len(lst)-1):
    if res_lst[-1] <= lst[i]:
        res_lst.append(lst[i])

if res_lst[-1] < lst[-1]:
    res_lst.append(lst[-1])

print(res_lst)

