# 21. Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1



str_lst = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу", "йцу"]
search_str = "йцу"

pos = []
for i, x in enumerate(str_lst):
    if x == search_str:
        pos.append(i)
if str_lst == [] or pos == [] or len(pos) == 1:
	print('-1')
# print(pos)

for j, y in enumerate(pos):
    if 0 < j < 2:
        print(y)
        
 
# spisok_1 = []
# stroka_1 = "йцу"
# count = 0
# print(spisok_1.count(stroka_1))
# if spisok_1.count(stroka_1) <2:
#     count = -1
# else:
#     for i in range(len(spisok_1)):
#         if spisok_1[i] == stroka_1:
#             count+=1
#             if count ==2:
#                 count = i
#                 break
# print(f'Искомое {stroka_1}, ответ {count}')