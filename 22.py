# 22. Найти сумму чисел списка стоящих на нечетной позиции


# под нечетной позицией - поняла индекс элемента 
# если позиция элемнта порядковая в списке, то меняем if i % 2 != 0: на if i % 2 == 0:

lst = [3, 6, 7, 34, 23, 87, 3, 2]
summ = 0
for i, x in enumerate(lst):
    if i % 2 != 0:
        summ += x
print(summ)


