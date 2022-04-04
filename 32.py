# 32. Дана последовательность чисел. Получить список неповторяющихся 
# элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

print('Вариант 1')

lst = [1, 2, 3, 5, 1, 5, 3, 10]
lst1 = list(set(lst))
print(lst1)



# Вариант на совместном решении ДЗ
print('Вариант 2')

def number(list):
    unnumber = []
    for number in list:
        if number in unnumber:
            continue
        else:
            unnumber.append(number)
    return unnumber

print(number(lst))