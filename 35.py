# 35. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# Найти его.

lst = '1 2 3 4 5 7 8 9'
init_data = open('Sem35_file.txt', 'w')
init_data.writelines(lst)
init_data.close()

with open('Sem35_file.txt', 'r') as file:
    data = file.read()
data = list(map(int,(data.split())))
print(data)

for  i in range(len(data)-1):
    if data[i] != data[i+1]-1:
        data.insert(i+1, data[i]+1)
print(data)
