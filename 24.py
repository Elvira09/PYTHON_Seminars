# 24. В заданном списке вещественных чисел найдите разницу 
# между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math


lst = [40.67889, 5, 10.056731]
lst_temp = []
for i, x in enumerate(lst) :
    temp = round((x % 1), 3)
    if temp != 0: # убираем 0, если в списке присутствует целое число
        lst_temp.append(temp)
# print(lst_temp)
diff = max(lst_temp) - min(lst_temp)
print(diff)


# float_spisok = [1.1, 1.2, 3.1, 5, 10.01]
# # i=0
# # while float_spisok[i]>1:
# max = 0.000
# min = 1.000
# for i in range(len(float_spisok)):
#     float_spisok[i]=round(float_spisok[i]-int(float_spisok[i]),10)
#     if max<float_spisok[i]:
#         max = float_spisok[i]
#     if min>float_spisok[i]:
#         min = float_spisok[i]
# x=max-min
# # print(float_spisok)
# # print(max(float_spisok))
# print(max,min)
# print(type(x))
# print(x)