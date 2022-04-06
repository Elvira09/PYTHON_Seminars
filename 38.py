# 38. Напишите программу, удаляющую из текста все слова содержащие "абв".

# мой вариант
text = 'проверка: забвение, зимбабве, операция, 7834, : абв, аБв, итог'
print(text)

# мой вариант
list_text = text.split()
res_text = []

for i in range(len(list_text)):
    if 'абв' in list_text[i].lower():
        continue
    else: 
        res_text.append(list_text[i])

res_text = " ".join(res_text)
print('# мой вариант')
print(res_text)

# вариант Дмитрия Лобанова
text = list(filter(lambda x: 'абв' not in x, text.split()))
text = " ".join(text)
print('# вариант Дмитрия Лобанова')
print(text)




