# 8. Сообщить в какой четверти координатной плоскости 
# или на какой оси находится точка с координатами Х и У


x = float(input('Введите координату Х: '))
y = float(input('Введите координату Y: '))

if x > 0 and y > 0:
    print(f"Введенным координатам Х={x}, Y={y} соответствует первая четверть системы координат")
elif x < 0 and y > 0:
    print(f"Введенным координатам Х={x}, Y={y} соответствует вторая четверть системы координат")
elif x < 0 and y < 0:
    print(f"Введенным координатам Х={x}, Y={y} соответствует третья четверть системы координат")
elif x > 0  and y < 0:
	print(f"Введенным координатам Х={x}, Y={y} соответствует четвертая четверть системы координат")
elif x == 0:
	print(f"Введенным координатам Х={x}, Y={y} соответствует точка на оси Х")
elif y == 0:
	print(f"Введенным координатам Х={x}, Y={y} соответствует точка на оси Y")
else:
	print(f"Координаты введены не корректно")