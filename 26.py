# 26. Дано число. Составить список чисел Фибоначчи, 
# в том числе для отрицательных индексов. 
#  Т е для k = 8, список будет выглядеть так: 
# [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
    # для положительных формула: F(n) = F(n-1) + F(n-2)
    # для отрицательных формула: F(n) = F(n+2) - F(n+1)


def Fibonacci(n):
    if n <= 0:
        return Fibonacci(n + 2) - Fibonacci(n + 1)
    elif (n == 1 or n == 2):
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

n = int(input('Введите число:  '))

fib_list = []
for i in range((-n), (n+1)):
    fib_list.append(Fibonacci(i))

print(fib_list)

