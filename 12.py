# 12. Для натурального n создать словарь индекс-значение, 
# состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


n = int(input('Ввведите количество членов словаря:  '))
start = int(input('Ввведите стартовую позицию словаря:  '))
# n = 6
# start = 3
key = list(range(start, n+1)) 
value = list(range(start * 3 + 1, (n+1) * 3 + 1, 3)) 
dictionary = {x: y for x, y in zip(key, value)} # https://docs-python.ru/tutorial/operatsii-slovarjami-dict-python/vyrazhenie-slovar/
print(dictionary) 

# for i in key:
# 	print(i)
# for i in value:
# 	print(i)