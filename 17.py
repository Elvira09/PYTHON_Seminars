# 17. Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

import random

def get_list(x):
    lst = []
    for i in range(x): 
        i = random.randint(-x, x+1)
        lst.append(i)
    return lst

n = int(input('Введите количество элементов списка:  '))
# кладем индексы в файл
pos = list(range(0, n, 2))
with open('Seminars/Sem17_file.txt', 'w') as data:   
    for i in str(pos):
        if i.isdigit():
 	        data.write(i + '\n')

lst = get_list(n)
print(lst, '  - исходный список')

# считываем данные/позиции из файл
with open('Seminars/Sem17_file.txt') as file:
    lines = file.read().splitlines()

lines = list(map(int, lines))
print(lines, ' - Позиции из файла')

mult = 1
for i in range(len(lst)): # i  индекс
    for j in lines: # j элемент
        if i == j:
            mult = mult * lst[i]

print(mult, ' Произведение элементов')


