# 27 Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел

st = '23 9 2 345 95 8 900 8 56 '
print(st)

st_lst = [int(i) for i in st.split()]
max_st = max(st_lst)
min_st = min(st_lst)
        
print(max_st, ' - максимальное число')
print(min_st, ' - минимальное число')