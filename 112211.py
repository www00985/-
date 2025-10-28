
import math

# 1.1
# print(31,18,79)
# 1.2
# print(47,52,150)
# 1.3
# print("50\n10")
# 1.4
# print("5\n10\n21")
# 1.5
# print('1\n2')
# 1.6
# print(f"{math.pi:.3f}")
# 1.7
# print(f'{math.e:.1f}')
# 1.8
# a = int(input('введите число:'))
# print('вы ввели число:', a)
# 1.9
# d = int(input('введите число:'))
# print(d,'- вот такое число вы ввели ')
# 1.10
# k = str(input('как вас зовут?:'))
# print(k)
# 1.11
# g = str( input('введите название футбольной команды:'))
# print(g,"- это чемпион!")
# 1.12
# j = str(input('введите имя:'))
# print(f"Привет, {j}!")
# 1.13
# v = int(input("Введите целое число: "))
# print(f"Следующие за числом {v} - {v+1}.\nДля числа {v} предыдущее число - {v-1}.")
# 1.14
# x = input("Введите число 1: ")
# y = input("Введите число 2: ")
# z = input("Введите число 3: ")
# print(f" {x}  {y}  {z}")
# 1.15
# x = input("Введите число 1: ")
# y = input("Введите число 2: ")
# z = input("Введите число 3: ")
# k = input("Введите число 4: ")
# print(f"{x} {y} {z} {k}")
# 1.16
# t = input("Введите t: ")
# v = input("Введите v: ")
# x = input("Введите x: ")
# y = input("Введите y: ")
# print("5, 10\n7 см")
# print(f"100 {t}\n1949 {v}")
# print(f"{x} 25\n{x} {y}")
# 1.17
# a = input("Введите a: ")
# b = input("Введите b: ")
# x = input("Введите x: ")
# y = input("Введите y: ")
# print("2 кг\n13 17")
# print(f"{a} 1\n19 {b}")
# print(f"{x} {y}\n5 {y}")
# 2.1 a)
# a = int(input('введите значение х:'))
# y = 17*a**2-6*a+13
# print(y)
# b)
# a = int(input('введите число а:'))
# y = 3*a**2+5*a-21
# print(y)
# 2.2
# a = int(input('введите число а:'))
# f = a**2+10/ math.sqrt(a**2+1)
# print(f)
# 2.3 a)
# a = int(input('введите число а:'))
# f = math.sqrt( 2*a+math.sin(abs(3*a)))
# k= f/3.56
# print(k)
# b)
# a = int(input('введите число а:'))
# k = math.sin(3.2+math.sqrt(1+a)/abs(5*a))
# print(k)
# 2.4
# a = int(input('введите сторону квадрата:'))
# p = a*4
# print('периметр квадрата:', p)
# 2.5
# f = int(input('введите радиус окружности:'))
# d = 2*f
# print('диаметр окружности:',d)
# 2.6
# R = 6350 * 1000
# def distance_to_horizon(height):
#   height_meters = height * 1000 if isinstance(height, float) else height
#   return math.sqrt((R + height_meters) ** 2 - R ** 2)
# height_above_sea_level = 1
# distance = distance_to_horizon(height_above_sea_level)
# print(f'Расстояние до линии горизонта при высоте {height_above_sea_level:.0f} м составляет примерно {distance / 1000:.2f} км.')
# 2.7
# a = int( input(' введите длину ребра куба:'))
# v = a**3
# s = 4*a**2
# print('объем куба:',v)
# print("площадь боковой поверхности:",s)
# 2.8
# r = int( input(' введите радиус окружности:'))
# l = 2*math.pi*r
# s= math.pi*r**2
# print('длина окружности:',l)
# print("площадь круга:",s)
#2.9 a)
# x = int(input('введите значение x:'))
# y = int( input(' введите значение y:'))
# v = 2*x**3-3.44*y+2.3*x**2-7.1*y+2
# print(v)
# b)
# a = int(input('введите значение a:'))
# b = int( input(' введите значение b:'))
# v = 3.14*(a+b)**3+2.75*b**2-12.7*a-4.1
# print(v)
# 2.10 a)
# a = int ( input('введите целое число:'))
# v = a+b//2
# print('среднее арифметическое:',v)
# b)
# b = int ( input('введите целое число:'))
# g = math.sqrt(a*b)
# print('среднее геометрическое:',g)
# 2.11
# a = int(input('введите массу тела:'))
# b = int(input('введите объем тела:'))
# p=a//b
# print("плотность материала этого тела:",p)
# 2.12
# a = int(input('введите кол-во жителей:'))
# b = int(input('введите плащадь терретории гос-ва:'))
# v = a/b
# print('плотность населения в  этом государстве:',v)
# 2.13
# def solve_linear_equation(a, b):
#     if a != 0:
#         x = -b / a
#         return f'Корень уравнения: {x}'
#     else:
#         return 'Коэффициент a должен быть ненулевым'
# print(solve_linear_equation(2, 3))
# 2.14
# a = int(input('введите первый катет:'))
# b = int(input('введите второй катет:'))
# c = math.sqrt(a**2+b**2)
# print('гипотенуза равна:',c)
# 2.15
# a = int (input('введите внешний радиус:'))
# b = int(input('введите внутренний радиус:'))
# v = math.pi*(a**2-b**2)
# print('площадь кольца:',v)
# 2.16
# a = int(input('введите первый катет:'))
# b = int(input('введите второй катет:'))
# c = math.sqrt(a**2+b**2)
# p = a+b+c
# print('периметр:',p)
# 2.17
# a = int(input('введите меньшее основание равнобедренной трапеции:'))
# b= int(input('введите большее основание равнобедренной трапеции:'))
# h = int(input('введите высоту раввнобедренной трапеции:'))
# s = math.sqrt(h**2+(b-a/2)**2)
# p = a+b+2*s
# print('периметр трапеции:',p)
# 2.18
# def calculate_z_and_q(x, y):
#     numerator_z = x + (2 + y) / (x ** 2)
#     denominator_z = y + 1 / math.sqrt(x ** 2 + 10)
#     z = numerator_z / denominator_z
#     q = 7.25 * math.sin(x) - abs(y)
#     return z, q
# x = 1.0
# y = 2.0
# z, q = calculate_z_and_q(x, y)
# print(f"z = {z}")
# print(f"q = {q}")
# 2.19
# def calculate_x(a, b):
#     numerator = (2 / (a**2 + 25)) + b
#     denominator = math.sqrt(b) + (a + b) / 2
#     return numerator / denominator
# def calculate_y(a, b):
#     numerator = abs(a) + 2 * math.sin(b)
#     denominator = 5.5 * a
#     return numerator / denominator
# a = float(input("Введите значение a: "))
# b = float(input("Введите значение b: "))
# x = calculate_x(a, b)
# y = calculate_y(a, b)
# print(f"Значение x: {x}")
# print(f"Значение y: {y}")
# 2.20
# def calculate_functions(e, f, g, h):
#     a = math.sqrt(abs(e - 3 / f) ** 5 + g)
#     b = math.sin(e) + math.cos(h) ** 2
#     c = (33 * g) / (e * f - 3)
#     return a, b, c
# e = float(input("Введите значение e: "))
# f = float(input("Введите значение f: "))
# g = float(input("Введите значение g: "))
# h = float(input("Введите значение h: "))
# a, b, c = calculate_functions(e, f, g, h)
# print(f"a = {a}")
# print(f"b = {b}")
# print(f"c = {c}")
# 2.21
# def calculate_values(e, f, g, h):
#     a = (e + f / 2) / 3
#     b = abs(h**2 - g)
#     c = math.sqrt((g - h)**2 - 3 * math.sin(e))
#     return a, b, c
# e = float(input("Введите значение e: "))
# f = float(input("Введите значение f: "))
# g = float(input("Введите значение g: "))
# h = float(input("Введите значение h: "))
# a, b, c = calculate_values(e, f, g, h)
# print(f"a = {a}")
# print(f"b = {b}")
# print(f"c = {c}")
# 2.22
# def calculate_values(e, f, g, h):
#     a = (e + f / 2) / 3
#     b = abs(h ** 2 - g)
#     c = math.sqrt((g - h) ** 2 - 3 * math.sin(e))
#     return a, b, c
# e = float(input("Введите значение e: "))
# f = float(input("Введите значение f: "))
# g = float(input("Введите значение g: "))
# h = float(input("Введите значение h: "))
# a, b, c = calculate_values(e, f, g, h)
# print(f"a = {a}")
# print(f"b = {b}")
# print(f"c = {c}")
