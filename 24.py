# 24. В заданном списке вещественных чисел найдите разницу 
# между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math

# !НЕ ОТРАБОТАН вариантБ если в списке целое число - 
# воспринимает его как .00 и привлекает к итоговым расчетам


lst = [40.107, 31.245, 35.17, 5, 10.01]
lst_temp = []
for i, x in enumerate(lst) :
    temp = round((x % 1), 3)
    lst_temp.append(temp)
# print(lst_temp)
diff = max(lst_temp) - min(lst_temp)
print(diff)

