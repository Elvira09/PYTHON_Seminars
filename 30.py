# 30 Вычислить число Pi c заданной точностью d = 0.001

import math

def num_pi(d):
    if 0.1 >= d >= 10 ** -10:
        for_round = len(str(d))-2
        pi = math.pi
        num_pi = round(pi, for_round)
    else:
        num_pi = 'd не в заданном диапазоне'
    return num_pi

# d = int(input('введите коэффициент точности (от 10**-1 до 10**-10: '))
d = 0.001 
print(num_pi(d))

