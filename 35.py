# 35. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# Найти его.


with open('Sem35_file.txt', 'r') as file:
    data = file.read()
data = list(map(int,(data.split())))
print(data)

for  i in range(len(data)-1):
    if data[i] != data[i+1]-1:
        data.insert(i+1, data[i]+1)
print(data)
