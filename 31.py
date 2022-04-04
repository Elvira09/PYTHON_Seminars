# 31. Составить список простых множителей натурального числа N
# 20 = 5 * 2 * 2
# 120 = 2 * 2 * 2 * 5 * 3

num = int(input('Введите целое число: '))
prime_num = 2
res = []
while num > 1:
    if num % prime_num == 0:
        res.append(prime_num)
        num = num / prime_num
    else:
        prime_num += 1
print(res, ' - список простых множителей числа')
