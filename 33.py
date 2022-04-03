# 33. Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать 
# в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Введите k: '))
lst = []

for i in range(k):
    y = random.randrange(0,100)
    if y == 0:
        continue
    elif i == 0:
        lst.append(f"{y}")
    else:
        lst.append(f"{y}*x^{i}")

lst.append(f"{random.randrange(1,100)}*x^{k}")
print(lst)

data = ""
for i in range(-1, -(k+1), -1):
    if i == -1:
        data =data + lst[i]
    else:
        data =data + " + " + lst[i]

result = f"k={k} =>  {data} + {lst[0]} = 0"
print(result)

with open('Sem33_file.txt', 'w') as file:
    file.writelines(result)

