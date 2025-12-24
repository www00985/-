import math
from datetime import datetime, date

# task 4.1
def task_4_1(a, b):
    if a > b:
        bigger, smaller = a, b
    else:
        bigger, smaller = b, a
    return bigger, smaller
print(task_4_1(5, 8))
#  task 4.2
x = (int(input("Введите значение x:")))
def task_4_2(x):
    if x > 0:
        return math.sin(x)**2
    else:
        return 1 - 2 * (math.sin(x)**2)
print(f"Значение Y состовляет: {task_4_2(x)}")
# task 4.3
x = int(input("Введите значение x:"))
def task_4_3(x):
    if x > 0:
        return math.sin(x**2)
    else:
        return 1 + 2 * (math.sin(x)**2)
print(f"Значение Y состовляет: {task_4_3(x)}")
# task 4.4
x = int(input("Введите значение x:"))
y = int(input("Введите значение y:"))
def task_4_4(x, y):
    if x < 4:
        return "I"
    else:
        return "II"
print(f"Заданная точка расположена в(во) {task_4_4(x, y)} области")
# task 4.5
x = int(input("Введите значение x:"))
y = int(input("Введите значение y:"))
def task_4_5(x, y):
    if y > 3:
        return "I"
    else:
        return "II"
print(f"Заданная точка расположена в(во) {task_4_5(x, y)} области")
# task 4.6a
x = int(input("Введите значение x: "))
def task_4_6a(x):
    if x <= 2:
        return x
    else:
        return 2
print(f"Значение Y состовляет: {task_4_6a(x)}")
# task 4.6b
x = int(input("Введите значение x: "))
def task_4_6b(x):
    if x < 0:
        return 0
    elif x <= 3:
        return -x
    else:
        return -3
print(f"Значение Y состовляет: {task_4_6b(x)}")
# task 4.7
x = int(input("Введите значение x: "))
def task_4_7(x):
    k = x**2 if math.sin(x)<0 else abs(x)
    if k < x:
        return k * x
    else:
        return k + x
print(f"Значение функции состовляет: {task_4_7(x)}")
# task 4.8
x = int(input("Введите значение x: "))
def task_4_8(x):
    k = x**2 if math.sin(x) >= 0 else abs(x)
    if x < k:
        return abs(x)
    else:
        return k * x
print(f"Значение функции состовляет: {task_4_8(x)}")
# task 4.9
a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))
def task_4_9(a,b):
    if a > b:
        return a, b
    return b, a
print(f"Больщее число на 1 месте, меньшее на 2 месте{task_4_9(a,b)}")
# task 4.10
km = int(input("Введите расстояние в километрах: "))
ft = int(input("Введите расстояние в футах: "))
def task_4_10(km,ft):
    km_m = km * 1000
    ft_m = ft * 0.3048
    if km_m < ft_m:
        return "Меньше километров"
    else:
        return "Меньше футов"
print(f"{task_4_10(km,ft)}")
# task 4.11
v_km = int(input("Введите скорость в километрах в час: "))
v_m = int(input("Введите скорость в метрах в секунду: "))
def task_4_11(v_km,v_m):
    v1_ms = v_km * 1000 / 3600
    if v1_ms > v_m:
        return "Скорость в км/ч больше"
    elif v1_ms < v_m:
        return "Скорость в м/с больше"
    else:
        return "Скорости равны"
print(f"{task_4_11(v_km,v_m)}")
# task 4.12
r = int(input("Введите радиус: "))
s = int(input("Введите сторону: "))
def task_4_12(r,s):
    circle_area = math.pi * r**2
    square_area = s**2
    if circle_area > square_area:
        return "Круг больше"
    elif circle_area < square_area:
        return "Квадрат больше"
    else:
        return "Площади равны"
print(f"{task_4_12(r,s)}")
# task 4.13
mass1 = int(input("Введите массу первого тела: "))
mass2 = int(input("Введите массу второго тела: "))
volume1 = int(input("Введите объем первого тела: "))
volume2 = int(input("Введите объем второго тела: "))
def task_4_12(mass1,volume1,mass2,volume2):
    a1 = mass1 / volume1
    a2 = mass2 / volume2
    if a1 > a2:
        return "Первый материал плотнее"
    elif a1 < a2:
        return "Второй материал плотнее"
    else:
        return "Плотность материалов равна"
print(f"{task_4_12(mass1,volume1,mass2,volume2)}")
#task 4.14
r1 = int(input("Введите сопротивление первой цепи: "))
r2 = int(input("Введите сопротивление второй цепи: "))
v = int(input("Введите напряжение: "))
def task_4_14(r1,r2,v):
    total_r = r1 + r2
    current = v / total_r
    return current
print(f"Сила тока: {task_4_14(r1,r2,v)}")
# task 4.15
a = int(input("Введите значени a: "))
b = int(input("Введите значение b: "))
c = int(input("Введите значение c: "))
def task_4_15(a, b, c):
    D = b*b - 4*a*c
    if D < 0:
        return None
    elif D != 0:
        return None
    else:
        return D
print(f"{task_4_15(a,b,c)}")
# task 4.16
a = int(input("Введите значени a: "))
b = int(input("Введите значение b: "))
c = int(input("Введите значение c: "))
def task_4_16(a, b, c):
    D = b*b - 4*a*c
    if D < 0:
        return None
    sqrtD = int(math.isqrt(D))
    if sqrtD * sqrtD != D:
        return None
    if (-b + sqrtD) % (2*a) != 0 or (-b - sqrtD) % (2*a) != 0:
        return None
    x1 = (-b + sqrtD) // (2*a)
    x2 = (-b - sqrtD) // (2*a)
    return sorted([x1, x2])
print(f"{task_4_16(a,b,c,)}")
# task 4.17
a = int(input("Введите год рождения: "))
b = int(input("Введите номер месяца рождения: "))
c = int(input("Введите какой сейчас год: "))
d= int(input("Введите какой сейчас месяц: "))
def task_4_17(a,b,c,d):
    age = c - a
    if d < b:
        age -= 1
    return age
print(f"Полных лет: {task_4_17(a,b,c,d)}")
# task 4.18
a = int(input("Введите площадь круга: "))
b = int(input("Введите площадь квадрата: "))
def task_4_18(a,b):
    r = math.sqrt(a / math.pi)
    d = math.sqrt(b)
    c = (2*r <= d)
    e = (d*math.sqrt(2) <= 2*r)
    return c, e
print(f"{task_4_18(a,b)}")
# task 4.19
a = int(input("Введите площадь круга: "))
b = int(input("Введите площадь треугольника: "))
def task_4_19(a,b):
    r = math.sqrt(a / math.pi)
    d = math.sqrt(4 * b / (math.sqrt(3)))
    R_in = d * math.sqrt(3) / 6
    R_out = d * math.sqrt(3) / 3
    e = (r <= R_in)
    f = (R_out <= r)
    return e, f
print(f"{task_4_19(a,b)}")
# task 4.20
a = int(input("Введите координаты левых углов: "))
b = int(input("Введите координаты правых углов: "))
def task_4_20(a, b):
    x1 = min(a, b)
    y1 = min(a, b)
    x2 = max(a, b)
    y2 = max(a, )
    return (x1, y1, x2, y2)
print (f"{task_4_20(a,b)}")
# task 4.21
a = int(input("Введите координаты левых углов: "))
b = int(input("Введите координаты правых углов: "))
def task_4_21(a,b):
    x1 = min(a, b)
    y1 = min(a, b)
    x2 = max(a + b, b + b)
    y2 = max(a + b, b + b)
    return (x1, y1, x2, y2)
print(f"{task_4_21(a,b,)}")
# task 4.22
m = int(input("Введите значение m: "))
n = int(input("Введите значение n: "))
def task_4_22(m, n):
    if n == 0:
        return "Ошибка: деление на ноль"
    if m % n == 0:
        return m // n
    else:
        return "m на n нацело не делится"
print(f"{task_4_22(m,n)}")
# task 4.23
a = int(input("Введите значение a: "))
n = int(input("Введите значение n: "))
def task_4_23(a, n):
    return a % n == 0
print(f"{task_4_23(a,n)}")
# task 4.24(a)
n = int(input("Введите натуральное число: "))
print("Да" if n % 2 == 0 else "Нет")
# task 4.24(b)
n = int(input("Введите натуральное число: "))
print("Да" if n % 10 == 7 else "Нет")
# # task 4.25
n = int(input("Введите число: "))
print(n + 1 if n % 2 != 0 else n + 2)
# task 4.26(a)
n = int(input("Введите двузначное число: "))
a = n // 10
b = n % 10
print(1 if a > b else 2)
# task 4.26(b)
n = int(input("Введите двузначное число: "))
a = n // 10
b = n % 10
print("Да" if a == b else "Нет")
# task 4.27
n = int(input("Введите двузначное число: "))
a = n // 10
b = n % 10
print("Да" if n**2 == 4*(a**3 + b**3) else "Нет")
# task 4.28(a)
n = int(input("Введите число: "))
s = n // 10 + n % 10
print("Да" if 10 <= s <= 99 else "Нет")
# task 4.28(b)
n = int(input("Введите число: "))
s = n // 10 + n % 10
print("Да" if n > s else "Нет")
# task 4.29(a)
n = int(input("Введите число: "))
s = n // 10 + n % 10
print("Да" if s % 3 == 0 else "Нет")
# task 4.29(b)
n = int(input("Введите первое число: "))
a = int(input("Введите число a: "))
s = n // 10 + n % 10
print("Да" if s % a == 0 else "Нет")
# task 4.30
n = int(input("Введите число: "))
print("Да" if n // 100 == n % 10 else "Нет")
# task 4.31(a)
n = int(input("Введите число: "))
print("Да" if n // 100 > n % 10 else "Нет")
# task 4.31(b)
n = int(input("Введите число: "))
print("Да" if n // 100 > (n // 10) % 10 else "Нет")
# task 4.31(в)
n = int(input("Введите число: "))
print("Да" if (n // 10) % 10 > n % 10 else "Нет")
# task 4.32
n = int(input("Введите число: "))
a = n // 100
b = (n // 10) % 10
c = n % 10
print("Да" if n*n == a**3 + b**3 + c**3 else "Нет")
# task 4.33(a)
n = int(input("Введите число: "))
s = n // 100 + (n // 10) % 10 + n % 10
print("Да" if 10 <= s <= 99 else "Нет")
# task 4.33(b)
n = int(input("Введите число: "))
p = (n // 100) * ((n // 10) % 10) * (n % 10)
print("Да" if 100 <= p <= 999 else "Нет")
# task 4.33(в)
n = int(input("Введите число: "))
a = int(input("Введите число: "))
p = (n // 100) * ((n // 10) % 10) * (n % 10)
print("Да" if a > p else "Нет")
# task 4.33(г)
n = int(input("Введите число: "))
s = n // 100 + (n // 10) % 10 + n % 10
print("Да" if s % 5 == 0 else "Нет")
# task 4.33(д)
n = int(input("Введите число: "))
a = int(input("Введите число: "))
s = n // 100 + (n // 10) % 10 + n % 10
print("Да" if s % a == 0 else "Нет")
# task 4.34(a)
n = int(input("Введите число: "))
a = n // 100
b = (n // 10) % 10
c = n % 10
print("Да" if a == b == c else "Нет")
# taks 4.34(b)
n = int(input("Введите число: "))
a = n // 100
b = (n // 10) % 10
c = n % 10
print("Да" if a == b or b == c or a == c else "Нет")
# task 4.35(а)
n = int(input("Введите число: "))
print("Да" if n//1000 + (n//100)%10 == (n//10)%10 + n%10 else "Нет")
# task 4.35(b)
n = int(input("Введите число: "))
s = n//1000 + (n//100)%10 + (n//10)%10 + n%10
print("Да" if s % 3 == 0 else "Нет")
# task 4.35(в)
n = int(input("Введите число: "))
p = (n//1000)*((n//100)%10)*((n//10)%10)*(n%10)
print("Да" if p % 4 == 0 else "Нет")
# task 4.36
n = int(input("Введите натуральное число: "))
# а) чётная цифра
if n % 2 == 0:
    print("Оканчивается чётной цифрой")
else:
    print("Не оканчивается чётной цифрой")
# б) нечётная цифра
if n % 2 == 1:
    print("Оканчивается нечётной цифрой")
else:
    print("Не оканчивается нечётной цифрой")
# task 4.37
a = int(input("Введите a: "))
b = int(input("Введите b: "))
if b % a == 0:
    print("a является делителем b")
else:
    print("a не является делителем b")
if a % b == 0:
    print("b является делителем a")
else:
    print("b не является делителем a")
# task 4.38
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))
count1 = (a // c) * (b // d)
count2 = (a // d) * (b // c)
if count1 > count2:
    print("Больше при размещении вдоль длинной стороны")
elif count2 > count1:
    print("Больше при размещении вдоль короткой стороны")
else:
    print("Количество одинаково")
# task 4.39
t = float(input("Введите время в минутах: "))
cycle = t % 5
if cycle < 3:
    print("Горит зелёный")
else:
    print("Горит красный")
# task 4.40
x = float(input("Введите число: "))
if -5 < x < 3:
    print("Принадлежит интервалу")
else:
    print("Не принадлежит интервалу")
# task 4.41
n = int(input("Введите натуральное число: "))
if 10 <= n <= 99:
    print("Число двузначное")
else:
    print("Число не двузначное")
# task 4.42(a)
x = float(input("Введите x: "))
y = float(input("Введите y: "))
if x > 2 and y > 2:
    print("Точка принадлежит области I")
else:
    print("Точка не принадлежит области I")
# task 4.42(b)
x = float(input("Введите x: "))
y = float(input("Введите y: "))
if x < -2 and y < -4:
    print("Точка принадлежит области I")
else:
    print("Точка не принадлежит области I")
# task 4.43
x = float(input("Введите x: "))
y = float(input("Введите y: "))
if x > 3 and y > 2:
    print("Точка принадлежит области I")
else:
    print("Точка не принадлежит области I")
# task 4.44
x = float(input("Введите x: "))
y = float(input("Введите y: "))
if x > 5:
    print("Точка принадлежит области I")
elif x < -1:
    print("Точка принадлежит области III")
else:
    print("Точка не принадлежит областям I и III")
# task 4.45
x = float(input("Введите x: "))
if -2.4 <= x <= 5.7:
    f = x ** 2
else:
    f = 4
print("f(x) =", f)
# task 4.46
x = float(input("Введите x: "))
if 0.2 <= x <= 0.9:
    f = math.sin(x)
else:
    f = 1
print("f(x) =", f)
# task 4.47
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
# a)
if a < b < c:
    print("Выполняется: a < b < c")
else:
    print("Не выполняется: a < b < c")
# б)
if b > a > c:
    print("Выполняется: b > a > c")
else:
    print("Не выполняется: b > a > c")
# task 4.48
a = int(input("a = "))
b = int(input("b = "))
if a != 0 and b % a == 0:
    print("a — делитель b")
elif b != 0 and a % b == 0:
    print("b — делитель a")
else:
    print("Ни одно число не является делителем другого")
# task 4.49
n = abs(int(input("Введите двузначное число: ")))
d1 = n // 10
d2 = n % 10
# a)
if d1 == 3 or d2 == 3:
    print("Цифра 3 входит")
else:
    print("Цифра 3 не входит")
# б)
a = int(input("Введите цифру a: "))
if d1 == a or d2 == a:
    print("Цифра a входит")
else:
    print("Цифра a не входит")
# task 4.50
n = abs(int(input("Введите двузначное число: ")))
d1 = n // 10
d2 = n % 10
# a)
if d1 == 4 or d2 == 4 or d1 == 7 or d2 == 7:
    print("Входят цифры 4 или 7")
else:
    print("Не входят цифры 4 или 7")
# б)
if d1 in (3, 6, 9) or d2 in (3, 6, 9):
    print("Входят цифры 3, 6 или 9")
else:
    print("Не входят цифры 3, 6 или 9")
# task 4.51
n = abs(int(input("Введите трехзначное число: ")))
a = n // 100
b = (n // 10) % 10
c = n % 10
# a)
if a == 6 or b == 6 or c == 6:
    print("Цифра 6 входит")
else:
    print("Цифра 6 не входит")
# б)
p = int(input("Введите цифру p: "))
if a == p or b == p or c == p:
    print("Цифра p входит")
else:
    print("Цифра p не входит")
# task 4.52
n = abs(int(input("Введите трехзначное число: ")))
if '6' in str(n):
    print("Цифра 6 входит")
else:
    print("Цифра 6 не входит")
# task 4.53
n = abs(int(input("Введите трехзначное число: ")))
digits = [n // 100, (n // 10) % 10, n % 10]
# a)
if 4 in digits or 7 in digits:
    print("Входят цифры 4 или 7")
else:
    print("Не входят цифры 4 или 7")
# б)
if any(d in (3, 6, 9) for d in digits):
    print("Входят цифры 3, 6 или 9")
else:
    print("Не входят цифры 3, 6 или 9")
# task 4.54
n = abs(int(input("Введите четырехзначное число: ")))
digits = list(map(int, str(n)))
# a)
if 4 in digits:
    print("Цифра 4 входит")
else:
    print("Цифра 4 не входит")
# б)
b = int(input("Введите цифру b: "))
if b in digits:
    print("Цифра b входит")
else:
    print("Цифра b не входит")
# task 4.55
n = abs(int(input("Введите четырехзначное число: ")))
digits = list(map(int, str(n)))
# a)
if 2 in digits or 7 in digits:
    print("Входят цифры 2 или 7")
else:
    print("Не входят цифры 2 или 7")
# б)
if any(d in (3, 6, 9) for d in digits):
    print("Входят цифры 3, 6 или 9")
else:
    print("Не входят цифры 3, 6 или 9")
# task 4.56
n = input("Введите четырехзначное число: ")
if n == n[::-1]:
    print("Число симметричное")
else:
    print("Число несимметричное")
# task 4.57
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))
r = a % b
if r == c or r == d:
    print("Остаток равен c или d")
else:
    print("Остаток не равен ни c, ни d")
# task 4.58
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a == b or a == c or b == c:
    print("Есть равные числа")
else:
    print("Равных чисел нет")
# task 4.59
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
# a)
if a == b == c:
    print("Треугольник равносторонний")
else:
    print("Треугольник не равносторонний")
# б)
if a == b or a == c or b == c:
    print("Треугольник равнобедренный")
else:
    print("Треугольник не равнобедренный")
# task 4.60
h1 = float(input("Рост 1: "))
h2 = float(input("Рост 2: "))
h3 = float(input("Рост 3: "))
if h1 == h2 == h3:
    print("Рост одинаковый")
else:
    print("Рост различается")
# task 4.61
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
D = b ** 2 - 4 * a * c
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("Два корня:", x1, x2)
elif D == 0:
    x = -b / (2 * a)
    print("Один корень:", x)
else:
    print("Корней нет")
# task 4.62
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))
if (a <= c and b <= d) or (a <= d and b <= c):
    print("YES")
else:
    print("NO")
# task 4.63
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))
a += 2
b += 2
if (a <= c and b <= d) or (a <= d and b <= c):
    print("YES")
else:
    print("NO")
# task 4.64
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))
if d + 2 <= min(a, b):
    print("YES")
else:
    print("NO")
# task 4.65
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
x = int(input("Введите x: "))
y = int(input("Введите y: "))
brick = sorted([a, b, c])
hole = sorted([x, y])
if brick[0] <= hole[0] and brick[1] <= hole[1]:
    print("YES")
else:
    print("NO")
# task 4.66
a1 = int(input("Введите a1: "))
a2 = int(input("Введите a2: "))
a3 = int(input("Введите a3: "))
b1 = int(input("Введите b1: "))
b2 = int(input("Введите b2: "))
b3 = int(input("Введите b3: "))
suitcase = sorted([a1, a2, a3])
box = sorted([b1, b2, b3])
if all(box[i] <= suitcase[i] for i in range(3)):
    print("YES")
else:
    print("NO")
# task 4.67
n = input("Введите число: ")
if len(n) == 6 and sum(map(int, n[:3])) == sum(map(int, n[3:])):
    print("YES")
else:
    print("NO")
# task 4.68
n = int(input())
if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
    print("YES")
else:
    print("NO")
# task 4.69
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))
e = int(input("Введите e: "))
dims = [c, d, e]
max_count = 0
for i in range(3):
    x = dims[(i + 1) % 3]
    y = dims[(i + 2) % 3]
    max_count = max(max_count,
                    (a // x) * (b // y),
                    (a // y) * (b // x))
print(max_count)
# task 4.70
k = int(input("Введите номер дня: "))
day_of_week = (k - 1) % 7  # 0 — понедельник, 5 — суббота, 6 — воскресенье
if day_of_week == 5 or day_of_week == 6:
    print("WEEKEND")
else:
    print("WORKDAY")
# task 4.71
alpha = int(input("Введите угол альфа: "))
v0 = int(input("Введите начальную скорость: "))
R = int(input("Введите расстояние: "))
H = int(input("Введите высоту: "))
P = int(input("Введите высоту снаряда: "))
g = 9.8
# время, когда снаряд достигнет x = R
t = R / (v0 * math.cos(math.radians(alpha)))
# высота снаряда в этот момент
y = v0 * t * math.sin(math.radians(alpha)) - g * t * t / 2
if H <= y <= H + P:
    print("YES")
else:
    print("NO")
# task 4.72
a1 = int(input("Введите a1: "))
a2 = int(input("Введите a2: "))
b1 = int(input("Введите b1: "))
b2 = int(input("Введите b2: "))
x1 = int(input("Введите x1: "))
x2 = int(input("Введите x2: "))
y1 = int(input("Введите y1: "))
y2 = int(input("Введите y2: "))
# границы
x1_max, y1_max = x1 + a1, y1 + b1
x2_max, y2_max = x2 + a2, y2 + b2
# a) первый внутри второго
a_inside = (x1 >= x2 and y1 >= y2 and x1_max <= x2_max and y1_max <= y2_max)
# б) один внутри другого
b_inside = a_inside or (x2 >= x1 and y2 >= y1 and x2_max <= x1_max and y2_max <= y1_max)
# в) пересечение
intersect = not (x1_max <= x2 or x2_max <= x1 or y1_max <= y2 or y2_max <= y1)
print("A:", "YES" if a_inside else "NO")
print("B:", "YES" if b_inside else "NO")
print("C:", "YES" if intersect else "NO")
# task 4.73
a1 = int(input("Введите a1: "))
a2 = int(input("Введите a2: "))
b = int(input("Введите b: "))
# если нет заёма
if a1 >= b:
    c1 = a1 - b
    c2 = a2
else:
    c1 = a1 + 10 - b
    c2 = a2 - 1
print(c2, c1)
# task 4.74
a1 = int(input("Введите a1: "))
a2 = int(input("Введите a2: "))
b1 = int(input("Введите b1: "))
b2 = int(input("Введите b2: "))
if a1 >= b1:
    c1 = a1 - b1
    c2 = a2 - b2
else:
    c1 = a1 + 10 - b1
    c2 = a2 - b2 - 1
print(c2, c1)
# task 4.75
a1 = int(input("Введите a1: "))
a2 = int(input("Введите a2: "))
a3 = int(input("Введите a3: "))
b1 = int(input("Введите b1: "))
b2 = int(input("Введите b2: "))
c1 = a1 + b1
carry = c1 // 10
c1 %= 10
c2 = a2 + b2 + carry
carry = c2 // 10
c2 %= 10
c3 = a3 + carry
print(c3, c2, c1)
# task 4.76
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))
# a) ладья
print("YES" if a == c or b == d else "NO")
# б) слон
print("YES" if abs(a - c) == abs(b - d) else "NO")
# в) король
print("YES" if max(abs(a - c), abs(b - d)) == 1 else "NO")
# г) ферзь
if a == c or b == d or abs(a - c) == abs(b - d):
    print("YES")
else:
    print("NO")
# д) белая пешка
print("YES" if c == a and d == b + 1 else "NO")  #обычный ход
print("YES" if abs(c - a) == 1 and d == b + 1 else "NO")  # взятие
# е) черная пешка
print("YES" if c == a and d == b - 1 else "NO")  #обычный ход
print("YES" if abs(c - a) == 1 and d == b - 1 else "NO")  #взятие
# ж) конь
dx = abs(a - c)
dy = abs(b - d)
print("YES" if (dx == 2 and dy == 1) or (dx == 1 and dy == 2) else "NO")
# task 4.77
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))
e = int(input("Введите e: "))
f = int(input("Введите f: "))
white_piece = input("Введите белую фигуру: ")
black_piece = input("Введите черную фигуру: ")
def under_attack(x1, y1, x2, y2, piece):
    """Проверяет, бьёт ли фигура 'piece', стоящая на (x1, y1), поле (x2, y2)"""
    if piece == "ладья":
        return x1 == x2 or y1 == y2
    elif piece == "слон":
        return abs(x1 - x2) == abs(y1 - y2)
    elif piece == "ферзь":
        return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)
    elif piece == "конь":
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        return (dx == 1 and dy == 2) or (dx == 2 and dy == 1)
    elif piece == "король":
        return max(abs(x1 - x2), abs(y1 - y2)) == 1
    else:
        raise ValueError("Неизвестная фигура")
def can_move(white_piece, black_piece, a, b, c, d, e, f):
    if (a, b) == (e, f):
        return False
    if white_piece == "ладья":
        if not (a == e or b == f):
            return False
    elif white_piece == "слон":
        if abs(a - e) != abs(b - f):
            return False
    elif white_piece == "ферзь":
        if not (a == e or b == f or abs(a - e) == abs(b - f)):
            return False
    elif white_piece == "конь":
        dx = abs(a - e)
        dy = abs(b - f)
        if not ((dx == 1 and dy == 2) or (dx == 2 and dy == 1)):
            return False
    elif white_piece == "король":
        if max(abs(a - e), abs(b - f)) != 1:
            return False
    else:
        raise ValueError("Неизвестная белая фигура")
    if under_attack(c, d, e, f, black_piece):
        return False
    return True
print(f"{can_move(white_piece, black_piece, a,b,c,d,e,f)}")
# task 4.78
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))
def same_color(a, b, c, d):
    return (a + b) % 2 == (c + d) % 2
print(f"{same_color(a,b,c,d)}")
# task 4.79
a = int(input("Введите значение стороны a: "))
b = int(input("Введите значение стороны b: "))
c = int(input("Введите значение стороны c: "))
def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0
print(f"{is_triangle(a,b,c)}")
# task 4.80
a = int(input("Введите значение стороны a: "))
b = int(input("Введите значение стороны b: "))
c = int(input("Введите значение стороны c: "))
def is_right_triangle(a, b, c):
    sides = sorted([a, b, c])
    return math.isclose(sides[2]**2, sides[0]**2 + sides[1]**2)
print(f"{is_right_triangle(a,b,c)}")
# task 4.81(а)
a = int(input("Введите значение стороны a: "))
b = int(input("Введите значение стороны b: "))
c = int(input("Введите значение стороны c: "))
def classify_triangle_a(a, b, c):
    sides = sorted([a, b, c])
    a_small, b_small, c_large = sides
    a2 = a_small**2
    b2 = b_small**2
    c2 = c_large**2
    if math.isclose(c2, a2 + b2):
        return "прямоугольный"
    elif c2 < a2 + b2:
        return "остроугольный"
    else:
        return "тупоугольный"
print(f"{classify_triangle_a(a,b,c)}")
# task 4.81(б)
a = int(input("Введите значение стороны a: "))
b = int(input("Введите значение стороны b: "))
c = int(input("Введите значение стороны c: "))
def classify_triangle_b(a, b, c):
    angle_type = classify_triangle_a(a, b, c)
    if math.isclose(a, b) and math.isclose(b, c):
        side_type = "равносторонний"
    elif math.isclose(a, b) or math.isclose(b, c) or math.isclose(a, c):
        side_type = "равнобедренный"
    else:
        side_type = "разносторонний"
    return f"{angle_type}, {side_type}"
print(f"{classify_triangle_b(a,b,c)}")
# task 4.82
n = int(input("Введите возраст: "))
def age_phrase(n):
    if not 1 <= n <= 99:
        return "Возраст должен быть от 1 до 99 лет"
    if n % 10 == 1 and n != 11:
        word = "год"
    elif n % 10 in [2, 3, 4] and n not in [12, 13, 14]:
        word = "года"
    else:
        word = "лет"
    return f"мне {n} {word}"
print(f"{age_phrase(n)}")
# task 4.83
k = int(input("Введите количество грибов: "))
def mushrooms_phrase(k):
    if k <= 0:
        return "Количество грибов должно быть натуральным числом"
    last_digit = k % 10
    last_two_digits = k % 100
    if last_digit == 1 and last_two_digits != 11:
        word = "гриб"
    elif last_digit in [2, 3, 4] and last_two_digits not in [12, 13, 14]:
        word = "гриба"
    else:
        word = "грибов"
    return f"мы нашли {k} {word} в лесу"
print(f"{mushrooms_phrase(k)}")
# task 4.84
kopecks = int(input("Введите количество копеек: "))
def price_in_rubles(kopecks):
    if not 1 <= kopecks <= 9999:
        return "Стоимость должна быть от 1 до 9999 копеек"
    rubles = kopecks // 100
    kopecks_remainder = kopecks % 100
    if rubles == 0:
        ruble_word = ""
    elif rubles % 10 == 1 and rubles % 100 != 11:
        ruble_word = "рубль"
    elif rubles % 10 in [2, 3, 4] and rubles % 100 not in [12, 13, 14]:
        ruble_word = "рубля"
    else:
        ruble_word = "рублей"
    if kopecks_remainder == 0:
        if rubles == 0:
            return "0 рублей"
        return f"{rubles} {ruble_word} ровно"
    elif kopecks_remainder % 10 == 1 and kopecks_remainder % 100 != 11:
        kopek_word = "копейка"
    elif kopecks_remainder % 10 in [2, 3, 4] and kopecks_remainder % 100 not in [12, 13, 14]:
        kopek_word = "копейки"
    else:
        kopek_word = "копеек"
    if rubles == 0:
        return f"{kopecks_remainder} {kopek_word}"
    else:
        return f"{rubles} {ruble_word} {kopecks_remainder} {kopek_word}"
print(f"{price_in_rubles(kopecks)}")
# task 4.85
month = int(input("Введите число: "))
def age_in_years_months(months):
    if not 1 <= months <= 1188:
        return "Возраст должен быть от 1 до 1188 месяцев"
    years = months // 12
    months_remainder = months % 12
    if years == 0:
        year_word = ""
    elif years % 10 == 1 and years % 100 != 11:
        year_word = "год"
    elif years % 10 in [2, 3, 4] and years % 100 not in [12, 13, 14]:
        year_word = "года"
    else:
        year_word = "лет"
    if months_remainder == 0:
        if years == 0:
            return "0 лет"
        return f"{years} {year_word} ровно"
    elif months_remainder % 10 == 1 and months_remainder != 11:
        month_word = "месяц"
    elif months_remainder % 10 in [2, 3, 4] and months_remainder not in [12, 13, 14]:
        month_word = "месяца"
    else:
        month_word = "месяцев"
    if years == 0:
        return f"{months_remainder} {month_word}"
    else:
        return f"{years} {year_word} {months_remainder} {month_word}"
print(f"{age_in_years_months(month)}")
# task 4.86
birth_year = int(input("Введите год рождения: "))
birth_month = int(input("Введите месяц рождения: "))
birth_day = int(input("Введите день рождения: "))
def calculate_age(birth_year, birth_month, birth_day,
                              current_year=None, current_month=None, current_day=None):
    if current_year is None:
        today = date.today()
        current_year, current_month, current_day = today.year, today.month, today.day
    try:
        birth_date = date(birth_year, birth_month, birth_day)
        current_date = date(current_year, current_month, current_day)
    except ValueError:
        return "Некорректная дата"
    if birth_date > current_date:
        return "Дата рождения не может быть позже текущей даты"
    age = current_year - birth_year
    if (current_month, current_day) < (birth_month, birth_day):
        age -= 1
    return age
print(f"{calculate_age(birth_year,birth_month,birth_day)}")
# task 4.87
year1 = int(input("Введите year1: "))
year2 = int(input("Введите year2: "))
month1 = int(input("Введите month1: "))
month2 = int(input("Введите month2: "))
day1 = int(input("Введите day1: "))
day2 = int(input("Введите day2: "))
def who_is_older(year1, month1, day1, year2, month2, day2):
    try:
        date1 = date(year1, month1, day1)
        date2 = date(year2, month2, day2)
    except ValueError:
        return "Некорректная дата"
    if date1 < date2:
        return 1  # Первый старше
    elif date1 > date2:
        return 2  # Второй старше
    else:
        return 0  # Ровесники
print(f"{who_is_older(year1,month1,day1,year2,month2,day2)}")
# task 4.88
birth_year = int(input("Введите год рождения: "))
birth_month = int(input("Введите месяц рождения: "))
def age_in_years_months_simple(birth_year, birth_month,
                               current_year = None, current_month = None):
    if current_year is None or current_month is None:
        today = date.today()
        current_year, current_month = today.year, today.month
    if not (1 <= birth_month <= 12 and 1 <= current_month <= 12):
        return "Некорректный номер месяца"
    if birth_year > current_year or (birth_year == current_year and birth_month > current_month):
        return "Дата рождения не может быть позже текущей даты"
    total_months = (current_year - birth_year) * 12 + (current_month - birth_month)
    years = total_months // 12
    months = total_months % 12
    return years, months
print(f"{age_in_years_months_simple(birth_year, birth_year)}")
# task 4.89
a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))
c = int(input("Введите значение c: "))
d = int(input("Введите значение d: "))
n = int(input("Введите значение n: "))
m = int(input("Введите значение m: "))
def is_train_at_platform(a, b, c, d, n, m):
    arrival = a * 60 + b
    departure = c * 60 + d
    passenger = n * 60 + m
    if departure <= arrival:
        departure += 24 * 60
    if passenger < arrival:
        passenger += 24 * 60
    return arrival <= passenger < departure
print(f"{is_train_at_platform(a,b,c,d,n,m)}")
# task 4.90
n = int(input("Введите число: "))
m = int(input("Введите номер месяца: "))
def days_in_month(m, leap_year=False):
    if m == 2:
        return 29 if leap_year else 28
    elif m in [4, 6, 9, 11]:
        return 30
    else:
        return 31
    # a)
def previous_day_490(n, m):
    if n > 1:
        return n - 1, m
    else:
        prev_month = m - 1 if m > 1 else 12
        prev_day = days_in_month(prev_month, False)
        return prev_day, prev_month
    # б
def next_day_490(n, m):
    days = days_in_month(m, False)
    if n < days:
        return n + 1, m
    else:
        next_month = m + 1 if m < 12 else 1
        return 1, next_month
print(f"{previous_day_490(n,m)}")
# task 4.91
n = int(input("Введите число: "))
m = int(input("Введите месяц: "))
g = int(input("Введите год: "))
days_in_mounth = 30 or 31 or 28 or 29
def is_leap_year(g):
    return (g % 4 == 0 and g % 100 != 0) or (g % 100 == 0 and g % 400 == 0)
# а)
def previous_day_491(g, n, m, consider_leap=True):
    leap = is_leap_year(g) if consider_leap else False
    if n > 1:
        return g, n - 1, m
    else:
        if m > 1:
            prev_month = m - 1
            prev_year = g
        else:
            prev_month = 12
            prev_year = g - 1
        prev_day = days_in_mounth(prev_month, leap and prev_year == g)
        return prev_year, prev_day, prev_month
# б)
def next_day_491(g, n, m, consider_leap=True):
    leap = is_leap_year(g) if consider_leap else False
    days = days_in_mounth(m, leap)
    if n < days:
        return g, n + 1, m
    else:
        if m < 12:
            next_month = m + 1
            next_year = g
        else:
            next_month = 1
            next_year = g + 1
        return next_year, 1, next_month
print(is_leap_year(g))
print(previous_day_491(n,m,g))
# task 4.92
t = int(input("Введите число: "))
def traffic_light_color(t):
    cycle_position = t % 6
    if cycle_position < 3:
        return "зеленый"
    elif cycle_position < 4:
        return "желтый"
    else:
        return "красный"
print(f"{traffic_light_color(t)}")
# task 4.93
k = int(input("Введите номер: "))
def day_of_week_k(k, january_first=1):
    day_num = (january_first + (k - 1) % 7) % 7
    if day_num == 0:
        day_num = 7
    if day_num == 6:
        return "суббота"
    elif day_num == 7:
        return "воскресенье"
    else:
        return "рабочий день"
print(f"{day_of_week_k(k)}")
# task 4.94
k = int(input("Введите число: "))
def build_sequence_494():
    sequence = ""
    for i in range(10, 100):
        sequence += str(i)
    return sequence
def kth_digit_494(k):
    if not 1 <= k <= 180:
        return "k должно быть от 1 до 180"
    sequence = build_sequence_494()
    return int(sequence[k-1])
print(f"{kth_digit_494(k)}")
# task 4.95
n = int(input("Введите число: "))
def build_sequence_495():
    sequence = "0"
    for i in range(1, 21):
        sequence += str(i)
    return sequence
def kth_digit_495(n):
    if not 1 <= n <= 32:
        return "n должно быть от 1 до 32"
    sequence = build_sequence_495()
    return int(sequence[n-1])
print(f"{kth_digit_495(n)}")
# task 4.96
k = int(input("Введите число: "))
def build_sequence_496():
    sequence = ""
    for i in range(50, 251):
        sequence += str(i)
    return sequence
def kth_digit_496(k):
    if not 1 <= k <= 222:
        return "k должно быть от 1 до 222"
    sequence = build_sequence_496()
    return int(sequence[k-1])
print(f"{kth_digit_496(k)}")
# task 4.97
k = int(input("Введите число: "))
def build_sequence_497():
    sequence = ""
    for i in range(1, 111):
        sequence += str(i)
    return sequence
def kth_digit_497(k):
    if not 1 <= k <= 222:
        return "k должно быть от 1 до 222"
    sequence = build_sequence_497()
    return int(sequence[k-1])
print(f"{kth_digit_497(k)}")
# task 4.98
n = int(input("Введите количество квартир: "))
a = int(input("Введите номер квартиры: "))
def is_apartment_sum_even(n, a):
    sum_numbers = 0
    for i in range(n):
        sum_numbers += a + i
    return sum_numbers % 2 == 0
print(f"{is_apartment_sum_even(n,a)}")
# task 4.99
# a)
x = int(input("Введите x: "))
y = int(input("Введите y: "))
def max_two_numbers_a(x, y):
    max_val = x
    if y > x:
        max_val = y
    return max_val
print(f"{max_two_numbers_a(x,y)}")
# б)
x = int(input("Введите x: "))
y = int(input("Введите y: "))
def max_two_numbers_b(x, y):
    if x < y:
        return y
    return x
print(f"{max_two_numbers_b(x,y)}")
# task 4.100
# a)
x = int(input("Введите x: "))
y = int(input("Введите y: "))
def min_max_two_numbers_a(x, y):
    if x > y:
        max_val = x
        min_val = y
    else:
        max_val = y
        min_val = x
    return max_val, min_val
print(f"{min_max_two_numbers_a(x,y)}")
# б)
x = int(input("Введите x: "))
y = int(input("Введите y: "))
def min_max_two_numbers_b(x, y):
    if x > y:
        max_val = x
        min_val = y
        return max_val, min_val
    max_val = y
    min_val = x
    return max_val, min_val
print(f"{min_max_two_numbers_b(x,y)}")
# task 4.101
# a)
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
def max_three_numbers(a, b, c):
    max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    return max_val
print(f"{max_three_numbers(a,b,c)}")
# б)
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
def min_three_numbers(a, b, c):
    min_val = a
    if b < min_val:
        min_val = b
    if c < min_val:
        min_val = c
    return min_val
print(f"{min_three_numbers(a,b,c)}")
# task 4.102
# a)
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))
def max_four_numbers(a, b, c, d):
    max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    if d > max_val:
        max_val = d
    return max_val
print(f"{max_four_numbers(a,b,c,d)}")
# б)
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))
def min_four_numbers(a, b, c, d):
    min_val = a
    if b < min_val:
        min_val = b
    if c < min_val:
        min_val = c
    if d < min_val:
        min_val = d
    return min_val
print(f"{min_four_numbers(a,b,c,d)}")
# task 4.103
x = int(input("Введите x: "))
def absolute_value(x):
    if x < 0:
        return -x
    return x
print(f"{absolute_value(x)}")
# task 4.104
def absolute_value(x):
    return -x if x < 0 else x
# a)
x = int(input("Введите x: "))
y = int(input("Введите y: "))
def task_104a(x, y):
    abs_x = absolute_value(x)
    abs_y = absolute_value(y)
    return (abs_x + abs_y) / 2
print(f"{task_104a(x,y)}")
# б)
x = int(input("Введите x: "))
y = int(input("Введите y: "))
def task_104b(x, y):
    abs_x = absolute_value(x)
    abs_y = absolute_value(y)
    product = abs_x * abs_y
    return math.sqrt(product) if product >= 0 else None
print(f"{task_104b(x,y)}")
# task 4.105
x = int(input("Введите x: "))
y = int(input("Введите y: "))
def task_105(x, y):
    if absolute_value(x) > absolute_value(y):
        return x / 2
    return x
print(f"{task_105(x,y)}")
# task 4.106
a = int(input("Введите a: "))
b = int(input("Введите b: "))
def task_106(a, b):
    if b >= 0:
        if math.sqrt(b) < a:
            return a, b * 5
    return a, b
print(f"{task_106(a,b)}")
# task 4.107
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
def task_107(a, b, c):
    result = []
    if a % 2 == 0:
        result.append(a)
    if b % 2 == 0:
        result.append(b)
    if c % 2 == 0:
        result.append(c)
    return result
print(f"{task_107(a,b,c)}")
# task 4.108
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
def task_108(a, b, c):
    result = []
    if a >= 0:
        result.append(a ** 2)
    if b >= 0:
        result.append(b ** 2)
    if c >= 0:
        result.append(c ** 2)
    return result
print(f"{task_108(a,b,c)}")
# task 4.109
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
def task_109(a, b, c):
    result = []
    if 1.6 <= a <= 3.8:
        result.append(a)
    if 1.6 <= b <= 3.8:
        result.append(b)
    if 1.6 <= c <= 3.8:
        result.append(c)
    return result
print(f"{task_109(a,b,c)}")
# task 4.110
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))
def task_110(a, b, c, d):
    count = 0
    if a < 0:
        count += 1
    if b < 0:
        count += 1
    if c < 0:
        count += 1
    if d < 0:
        count += 1
    return count
print(f"{task_110(a,b,c,d)}")
# task 4.111
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))
def task_111(a, b, c, d):
    count = 0
    if a % 2 == 0:
        count += 1
    if b % 2 == 0:
        count += 1
    if c % 2 == 0:
        count += 1
    if d % 2 == 0:
        count += 1
    return count
print(f"{task_111(a,b,c,d)}")
# task 4.112
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
def task_112(a, b, c):
    total = 0
    if a > 0:
        total += a
    if b > 0:
        total += b
    if c > 0:
        total += c
    return total
print(f"{task_112(a,b,c)}")
# task 4.113
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))
def task_113(a, b, c, d):
    total = 0
    if a > 5:
        total += a
    if b > 5:
        total += b
    if c > 5:
        total += c
    if d > 5:
        total += d
    return total
print(f"{task_113(a,b,c,d)}")
# task 4.114
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))
def task_114(a, b, c, d):
    total = 0
    if a % 3 == 0:
        total += a
    if b % 3 == 0:
        total += b
    if c % 3 == 0:
        total += c
    if d % 3 == 0:
        total += d
    return total
print(f"{task_114(a,b,c,d)}")
# task 4.115
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))
e = int(input("Введите e: "))
f = int(input("Введите f: "))
def task_115(a, b, c, d, e, f):
    total = 0
    if a > 0:
        total += a
    if b > 0:
        total += b
    if c > 0:
        total += c
    if d > 0:
        total += d
    if e > 0:
        total += e
    if f > 0:
        total += f
    return total
print(f"{task_115(a,b,c,d,e,f)}")
# task 4.116
x = int(input("Введите x: "))
def task_116(x):
    if x < -1:
        return -1
    elif x == -1:
        return 1
    else:
        return x
print(f"{task_116(x)}")
# task 4.121
x = int(input("Введите x: "))
y = int(input("Введите y: "))
def task_121(x, y):
    if x > 0 and y > 0:
        return "I"
    elif x < 0 and y > 0:
        return "II"
    elif x < 0 and y < 0:
        return "III"
    else:
        return "IV или на границе"
print(f"{task_121(x,y)}")
# task 4.122
x = int(input("Введите x: "))
y = int(input("Введите y: "))
def task_122(x, y):
    if y > 5.0:
        return "I"
    elif 2.5 < y <= 5.0:
        return "II"
    else:  # y ≤ 2.5
        return "III"
print(f"{task_122(x,y)}")
# task 4.123
points = int(input("Введите количество очков: "))
def task_123(points):
    if points == 3:
        return "выигрыш"
    elif points == 1:
        return "ничья"
    elif points == 0:
        return "проигрыш"
    else:
        return "некорректное количество очков (должно быть 0, 1 или 3)"
print(f"{task_123(points)}")
# task 4.124
mitja_age = int(input("Введите возраст Мити: "))
vasja_age = int(input("Введите возраст Васи: "))
def task_124(mitja_age, vasja_age):
    if mitja_age > vasja_age:
        return "Митя старше Васи"
    elif mitja_age < vasja_age:
        return "Вася старше Мити"
    else:
        return "Митя и Вася одного возраста"
print(f"{task_124(mitja_age, vasja_age)}")
# task 4.125
weight = int(input("Введите вес: "))
def task_125(weight):
    if weight < 60:
        return "легкий вес"
    elif weight < 64:
        return "первый полусредний вес"
    elif weight < 69:
        return "полусредний вес"
    else:
        return "вес выше полусредней категории"
print(f"{task_125(weight)}")
# task 4.126
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
def task_126(a, b):
    if a == 0 or b == 0:
        return "Числа не должны быть нулями"
    if a % b == 0:
        return f"{b} является делителем {a}"
    elif b % a == 0:
        return f"{a} является делителем {b}"
    else:
        return "Ни одно из чисел не является делителем другого"
print(f"{task_126(a,b)}")
# task 4.127
# a)
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
def task_127_a(a, b, c):
    if a > b and a > c:
        return "первое"
    elif b > a and b > c:
        return "второе"
    else:
        return "третье"
print(f"{task_127_a(a,b,c)}")
    # б)
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
def task_127_b(a, b, c):
    if a < b and a < c:
        return "первое"
    elif b < a and b < c:
        return "второе"
    else:
        return "третье"
print(f"{task_127_b(a,b,c)}")
# c)
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
def task_127_c(a, b, c):
    if (b < a < c) or (c < a < b):
        return "первое"
    elif (a < b < c) or (c < b < a):
        return "второе"
    else:
        return "третье"
print(f"{task_127_c(a,b,c)}")
# task 4.128
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
def task_128(a, b, c):
    if a > b and a > c:
        maximum = a
    elif b > a and b > c:
        maximum = b
    else:
        maximum = c
    if a < b and a < c:
        minimum = a
    elif b < a and b < c:
        minimum = b
    else:
        minimum = c
    return maximum, minimum
print(f"{task_128(a,b,c)}")
# task 4.129
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
def task_129(a, b, c):
    if a < b and a < c:
        return b + c
    elif b < a and b < c:
        return a + c
    else:
        return a + b
print(f"{task_129(a,b,c)}")
# task 4.130
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
def task_130(a, b, c):
    if a > b and a > c:
        return b * c
    elif b > a and b > c:
        return a * c
    else:
        return a * b
print(f"{task_130(a,b,c)}")
# task 4.131
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
def find_middle_of_three(a, b, c):
    if (b <= a <= c) or (c <= a <= b):
        return a
    elif (a <= b <= c) or (c <= b <= a):
        return b
    else:
        return c
a1 = int(input("Введите a1: "))
a2 = int(input("Введите a2: "))
b1 = int(input("Введите b1: "))
b2 = int(input("Введите b2: "))
c1 = int(input("Введите c1: "))
c2 = int(input("Введите c2: "))
def task_131(a1, b1, c1, a2, b2, c2):
    middle1 = find_middle_of_three(a1, b1, c1)
    middle2 = find_middle_of_three(a2, b2, c2)
    return (middle1 + middle2) / 2
print(find_middle_of_three(a,b,c), task_131(a1,b1,c1,a2,b2,c2))
# task 4.132
x = int(input("Введите x: "))
y = int(input("Введите y: "))
def task_132(x, y):
    if x == 0 or y == 0:
        return "Точка лежит на оси координат"
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4
print(f"{task_132(x,y)}")
# task 4.133
day_number = int(input("Введите номер дня недели: "))
def task_133(day_number):
    days = {
        1: "понедельник",
        2: "вторник",
        3: "среда",
        4: "четверг",
        5: "пятница",
        6: "суббота",
        7: "воскресенье" }
    if 1 <= day_number <= 7:
        return days[day_number]
    else:
        return "Неверный номер дня недели"
print(f"{task_133(day_number)}")
# task 4.134
month_number = int(input("Введите номер месяца: "))
def task_134(month_number):
    months = {
        1: "январь",
        2: "февраль",
        3: "март",
        4: "апрель",
        5: "май",
        6: "июнь",
        7: "июль",
        8: "август",
        9: "сентябрь",
        10: "октябрь",
        11: "ноябрь",
        12: "декабрь" }
    if 1 <= month_number <= 12:
        return months[month_number]
    else:
        return "Неверный номер месяца"
print(f"{task_134(month_number)}")
# task 4.135
month_number = int(input("Введите номер месяца: "))
def task_135(month_number):
    if month_number in [12, 1, 2]:
        return "зима"
    elif month_number in [3, 4, 5]:
        return "весна"
    elif month_number in [6, 7, 8]:
        return "лето"
    elif month_number in [9, 10, 11]:
        return "осень"
    else:
        return "Неверный номер месяца"
print(f"{task_135(month_number)}")
# task 4.136
year = int(input("Введите год: "))
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
month = int(input("Введите месяц: "))
def task_136(month, is_leap=False):
    if month < 1 or month > 12:
        return "Неверный номер месяца"
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 29 if is_leap else 28
print(task_136(month))
# task 4.137
month = int(input("Введите месяц: "))
def task_137(month):
    if month < 1 or month > 12:
        return "Неверный номер месяца"
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 28
print(task_137(month))
# task 4.138
m = int(input("Введите номер масти: "))
def task_138(m):
    if m == 1:
        return "пики"
    elif m == 2:
        return "трефы"
    elif m == 3:
        return "бубны"
    elif m == 4:
        return "червы"
    else:
        return "Неверный номер масти"
print(task_138(m))
# task 4.139
k = int(input("Введите номер карты: "))
def task_139(k):
    if k < 6 or k > 14:
        return "Неверный номер карты"
    if k == 11:
        return "валет"
    elif k == 12:
        return "дама"
    elif k == 13:
        return "король"
    elif k == 14:
        return "туз"
    elif 6 <= k <= 10:
        names = {
            6: "шестерка",
            7: "семерка",
            8: "восьмерка",
            9: "девятка",
            10: "десятка"
        }
        return names[k]
    else:
        return "Неверный номер карты"
print(task_139(k))
# task 4.140
m = int(input("Введите масть от 1 до 4: "))
k = int(input("Введите достоинство от 6 до 14: "))
def task_140(m, k):
    suits = {
        1: ("пики", "пик"),
        2: ("трефы", "треф"),
        3: ("бубны", "бубен"),
        4: ("червы", "червей")
    }
    ranks = {
        6: "Шестерка",
        7: "Семерка",
        8: "Восьмерка",
        9: "Девятка",
        10: "Десятка",
        11: "Валет",
        12: "Дама",
        13: "Король",
        14: "Туз"
    }
    if m not in suits or k not in ranks:
        return "Неверные параметры"
    suit_name, suit_genitive = suits[m]
    rank_name = ranks[k]
    if k in [6, 7, 8, 9, 10]:
        return f"{rank_name} {suit_genitive}"
    else:
        return f"{rank_name} {suit_genitive}"
print(f"{task_140(m,k)}")
# task 4.141
# а)
k = int(input("Введите номер дня: "))
def task_141_a(k):
    if k < 1 or k > 365:
        return "k должно быть от 1 до 365"
    day_of_week = ((k - 1) % 7) + 1
    days = {
        1: "понедельник",
        2: "вторник",
        3: "среда",
        4: "четверг",
        5: "пятница",
        6: "суббота",
        7: "воскресенье"
    }
    return days[day_of_week]
print(task_141_a(k))
# б)
k = int(input("Введите номер дня: "))
d = int(input("Введите d: "))
def task_141_b(k, d):
    if k < 1 or k > 365:
        return "k должно быть от 1 до 365"
    if d < 1 or d > 7:
        return "d должно быть от 1 до 7"
    day_of_week = (d - 1 + (k - 1)) % 7 + 1
    days = {
        1: "понедельник",
        2: "вторник",
        3: "среда",
        4: "четверг",
        5: "пятница",
        6: "суббота",
        7: "воскресенье"
    }
    return days[day_of_week]
print(task_141_b(k,d))
# task 4.142
n = int(input("Введите сколько месяцев прошло: "))
def task_142(n):
    if n < 0:
        return "Количество месяцев не может быть отрицательным"
    start_year = 2010
    years_passed = n // 12
    month_in_year = n % 12
    current_year = start_year + years_passed
    months = [
        "январь", "февраль", "март", "апрель", "май", "июнь",
        "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"
    ]
    month_name = months[month_in_year]
    return f"{month_name} {current_year} года"
print(task_142(n))
# task 4.143
year = int(input("Введите год: "))
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
month = int(input("Введите месяц: "))
def days_in_month(month, is_leap=False):
    if month < 1 or month > 12:
        return 0
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 29 if is_leap else 28
# а)
n = int(input("Введите число: "))
m = int(input("Введите номер месяца: "))
def task_143a_previous_day(n, m):
    if n > 1:
        return n - 1, m
    else:
        if m > 1:
            prev_month = m - 1
        else:
            prev_month = 12
        days_prev = days_in_month(prev_month, False)
        return days_prev, prev_month
print(task_143a_previous_day(n,m))
    # б)
n = int(input("Введите число: "))
m = int(input("Введите номер месяца: "))
def task_143b_next_day(n, m):
    days_current = days_in_month(m, False)
    if n < days_current:
        return n + 1, m
    else:
        if m < 12:
            next_month = m + 1
        else:
            next_month = 1
        return 1, next_month
print(task_143b_next_day(n,m))
# task 4.144
# a)
g = int(input("Введите год: "))
n = int(input("Введите число: "))
m = int(input("Введите номер месяца: "))
def task_144a_previous_day(g, n, m, consider_leap=True):
    is_leap = is_leap_year(g) if consider_leap else False
    if n > 1:
        return g, n - 1, m
    else:
        if m > 1:
            prev_month = m - 1
            prev_year = g
        else:
            prev_month = 12
            prev_year = g - 1
        prev_leap = is_leap_year(prev_year) if consider_leap else False
        days_prev = days_in_month(prev_month, prev_leap)
        return prev_year, days_prev, prev_month
print(task_144a_previous_day(g,n,m,consider_leap=True))
# б)
g = int(input("Введите год: "))
n = int(input("Введите число: "))
m = int(input("Введите номер месяца: "))
def task_144b_next_day(g, n, m, consider_leap=True):
    is_leap = is_leap_year(g) if consider_leap else False
    days_current = days_in_month(m, is_leap)
    if n < days_current:
        return g, n + 1, m
    else:
        if m < 12:
            next_month = m + 1
            next_year = g
        else:
            next_month = 1
            next_year = g + 1
        return next_year, 1, next_month
print(task_144b_next_day(g,n,m,consider_leap=True))
# task 4.145
year = int(input("Введите год: "))
def task_145(year):
    animals = [
        "Крыса", "Бык", "Тигр", "Кролик", "Дракон", "Змея",
        "Лошадь", "Коза", "Обезьяна", "Петух", "Собака", "Свинья"
    ]
    elements = ["Дерево", "Огонь", "Земля", "Металл", "Вода"]
    element_colors = ["Зеленый", "Красный", "Желтый", "Белый", "Черный"]
    start_year = 1984
    if year < start_year:
        cycles_before = (start_year - year - 1) // 60 + 1
        equivalent_year = year + cycles_before * 60
    else:
        equivalent_year = year
    offset = equivalent_year - start_year
    animal_index = offset % 12
    animal = animals[animal_index]
    element_cycle = offset % 10
    element_index = element_cycle // 2
    element = elements[element_index]
    color = element_colors[element_index]
    year_in_element = element_cycle % 2
    yin_yang = "Ян" if year_in_element == 0 else "Инь"
    return f"{animal}, {color}"
print(task_145(year))