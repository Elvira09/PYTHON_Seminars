
# Задача для 2 зала: Напишите алгоритм, 
# который берет массив и перемещает все нули в конец, 
# сохраняя порядок других элементов.

# Вариант 1
print('\nВариант 1')

lst = [0, 6, 0, 4, 0, 3, 9, 0]
print(lst, ' - исходный список')
lst_res = []
for i in lst:
	if i != 0:
		lst_res += [i]		
for i in lst:
	if i == 0:
		lst_res += [i]
print(lst_res, ' - результирующий список')

# Вариант 2
print('\nВариант 2')
for i in range(len(lst)-1, -1, -1):
    if lst[i] == 0:
        lst.append(lst[i])
        lst.pop(i)
print(lst, ' - результирующий список')