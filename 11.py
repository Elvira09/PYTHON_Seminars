# 11. Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

n = int(input('Ввведите количество членов последовательности:  '))
temp = 1
list = [temp]

for i in range(n-1):	
	temp = list[-1]* (-3)
	list.append(temp)
print(list) 
