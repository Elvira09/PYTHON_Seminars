# 38. Напишите программу, удаляющую из текста все слова содержащие "абв".

text = 'проверка: забвение, зимбабве, операция, 7834, : абв, аБв, итог'
print(text)

list_text = text.split()
res_text = []

for i in range(len(list_text)):
    if 'абв' in list_text[i].lower():
        continue
    else: 
        res_text.append(list_text[i])

res_text = " ".join(res_text)
print(res_text)

