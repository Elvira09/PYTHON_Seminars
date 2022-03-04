#  7. Проверить истинность утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат


# задаем предикаты:
X = True
Y = True
Z = False
print(f'Исходные данные: X = {X}, Y = {Y}, Z = {Z}')
r1 = not (X or Y or Z)
print(r1, ' # ¬(X ⋁ Y ⋁ Z)')
r2 = not (X) and not (Y) and not (Z)
print(r2, ' # ¬X ⋀ ¬Y ⋀ ¬Z')
if r1 == r2:
	print('True   # ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z  - Закон Де Моргана')
else:
	print('False  # ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')

