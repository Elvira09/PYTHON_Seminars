# 20. Определить, присутствует ли в заданном списке строк, некоторое число 

lst = ['2', 'no', '687', ':', 'yes', '98']
for x in lst:
    if x.isdigit():
        print(x)

print(lst.isdigit())		