# 33. Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать 
# в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random
import itertools

k = random.randint(2,8)
print(f'{k=}')

koefs = [random.randint(1,10) for i in range(k+1)]

#1*x^3 + 7*x^2 + 2*x + 1 = 0
def polinom(k, koefs):
    x_list = ['''*x^''']*(k-1)+['''*x''']
    polinomial = [[a,b,c] for a,b,c in itertools.zip_longest(koefs, x_list,range(k,1,-1), fillvalue='')]
    for i in polinomial:
        i.append(' + ')
    result = list(itertools.chain(*polinomial))
    
    result= result[:-3]+['= 0']
    result=list(map(str,result))
    return ''.join(result)

answer = polinom(k,koefs)
print(answer)




# k = int(input('Введите k: '))
# lst = []

# for i in range(k):
#     y = random.randrange(0,100)
#     if y == 0:
#         continue
#     elif i == 0:
#         lst.append(f"{y}")
#     else:
#         lst.append(f"{y}*x^{i}")

# lst.append(f"{random.randrange(1,100)}*x^{k}")
# print(lst)

# data = ""
# for i in range(-1, -(k+1), -1):
#     if i == -1:
#         data =data + lst[i]
#     else:
#         data =data + " + " + lst[i]

# result = f"k={k} =>  {data} + {lst[0]} = 0"
# print(result)

# with open('Sem33_file.txt', 'w') as file:
#     file.writelines(result)










# def Polynomial(k):
#     str = []
#     for i in range(0, k + 1):
#         coeff = random.randint(0, 100)
#         if i >= 2:
#             str.append(f"{coeff}*x^{i} + ")
#         elif i == 1:
#             str.append(f"{coeff}*x + ")
#         elif i == 0:
#             str.append(f"{coeff} = 0")
#     stroka = str[::-1]
#     result = ''.join(stroka)
#     with open("Sem33_file.txt", "a") as data:
#         data.write(result + '\n')


# Polynomial(0)