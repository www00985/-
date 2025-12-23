import math
sm = float(input("Введите расстояние в сантиметрах: "))
metr = int(sm//10)
print(f"Полных метров {metr}")
mass_kg = float(input("Введите массу в килограммах: "))
cent = int(mass_kg//100)
print(f"Полных центнеров {cent}")
days = 234
weeks = days//7
print(f"Прошло полных недель {weeks}")
N = int(input("Введите количество школьников: "))
k = int(input("Введите количество яблок, которые делят: "))
kajdomy = k//N
kajdomy=k//N
ostatok = k%N
print(f"Каждый школьник получит {kajdomy} яблок(а).")
print(f"В корзинке останется {ostatok} яблок(а).")
width = 543
height = 130
side = 130
squares_along_width = width//side
squares_along_height = height//side
total_squares = squares_along_width*squares_along_height
print(f"Можно отрезать {total_squares} квадрата.")
apartment_number = int(input("Введите номер квартиры: "))
floor = (apartment_number-1)//3+1
print(f"Квартира {apartment_number} находится на этаже {floor}")
ticket = int(input("Введите номер билета: "))
row = (ticket-1)//15+1
print(f"Место {ticket} находится в ряду {row}")
sec = int(input("Введите количество секунд с начала суток: "))
hours = sec//3600
remaining_seconds = sec%3600
minutes = remaining_seconds//60
seconds = remaining_seconds%60
print(f"Полных часов: {hours}")
print(f"Полных минут: {minutes}")
print(f"Полных cекунд: {seconds}")
k = int(input("Введите номер дня в году (1-365): "))
variant = input("Выберите вариант (a, b или c): ")
if variant == "a":
    n = ((k-1)%7)+1
elif variant == "b":
    n = (k%7)+1
elif variant == "c":
    d = int(input("Введите день недели для 1 января (d от 1 до 7 ): "))
    n = ((d-1)+(k-1))%7+1
else:
    print("Некорректный вариант.")
print(f"День недели для {k}-го дня в году: {n}")
n = int(input("Введите количество прошедших месяцев n: "))
x = n + 1
print("Номер месяца:", x)
k = int(input("Введите номер квартиры: "))
etazh = (k - 1) // 4 + 1
nomer_na_etazhe = (k - 1) % 4 + 1
print("Этаж:", etazh)
print("Номер по счёту на этаже:", nomer_na_etazhe)
n = int(input("Введите порядковый номер элемента (1..50): "))
stroka = (n - 1) // 5 + 1
print("Строка с элементом:", stroka)
print("Строка, где находится значение:", stroka)
k = int(input("Введите номер квартиры: "))
podyezd = (k - 1) // 54 + 1
v_podyezde = (k - 1) % 54 + 1
etazh = (v_podyezde - 1) // 6 + 1
nomer_na_etazhe = (v_podyezde - 1) % 6 + 1
print("Подъезд:", podyezd)
print("Этаж:", etazh)
print("Номер по счёту на этаже:", nomer_na_etazhe)
m = int(input("Введите номер места: "))
sekciya = (m - 1) // 150 + 1
v_sekcii = (m - 1) % 150 + 1
yarus = (v_sekcii - 1) // 15 + 1
nomer_na_yaruse = (v_sekcii - 1) % 15 + 1
print("Секция:", sekciya)
print("Ярус:", yarus)
print("Место на ярусе:", nomer_na_yaruse)
n = int(input("Введите двузначное число: "))
desyatki = n // 10
edinitsy = n % 10
print("Десятки:", desyatki)
print("Единицы:", edinitsy)
n = int(input("Введите трехзначное число: "))
summa = n // 10 + n % 10
print("Сумма цифр:", summa)
n = int(input("Введите двузначное число: "))
a = n // 10
b = n % 10
new_number = b * 10 + a
print("Полученное число:", new_number)
n = int(input("Введите трехзначное число: "))
a = n // 100
b = (n // 10) % 10
c = n % 10
print(a, b, c, sep=", ")
n = int(input("Введите трехзначное число: "))
a = n // 100
b = (n // 10) % 10
c = n % 10
print("Единицы:", c)
print("Десятки:", b)
print("Сумма цифр:", a + b + c)
print("Произведение цифр:", a * b * c)
n = int(input("Введите трехзначное число: "))
a = n // 100
b = (n // 10) % 10
c = n % 10
reversed_number = c * 100 + b * 10 + a
print("Число наоборот:", reversed_number)
n = int(input("Введите трехзначное число: "))
a = n // 100
b = (n // 10) % 10
c = n % 10
new_number = b * 100 + c * 10 + a
print("Полученное число:", new_number)
n = int(input("Введите трёхзначное число: "))
a = n // 100
b = (n // 10) % 10
c = n % 10
new_num = c * 100 + a * 10 + b
print("Полученное число:", new_num)
n = int(input("Введите трёхзначное число: "))
a = n // 100
b = (n // 10) % 10
c = n % 10
new_num = b * 100 + a * 10 + c
print("Полученное число:", new_num)
n = int(input("Введите трёхзначное число: "))
a = n // 100
b = (n // 10) % 10
c = n % 10
new_num = a * 100 + c * 10 + b
print("Полученное число:", new_num)
n = int(input("Введите трёхзначное число: "))
a = n // 100
b = (n // 10) % 10
c = n % 10
print(a*100 + b*10 + c)
print(a*100 + c*10 + b)
print(b*100 + a*10 + c)
print(b*100 + c*10 + a)
print(c*100 + a*10 + b)
print(c*100 + b*10 + a)
n = input("Введите число (4- или 5-значное): ")
summa = int(n[0]) + int(n[1]) + int(n[2]) + int(n[3])
if len(n) == 4:
    print("Сумма цифр:", summa)
else:
    print("Сумма цифр:", summa + int(n[4]))
n = int(input("Введите четырёхзначное число: "))
a = n // 1000
b = (n // 100) % 10
c = (n // 10) % 10
d = n % 10
rev = d*1000 + c*100 + b*10 + a #a
print("Наоборот:", rev)
new1 = b*1000 + a*100 + d*10 + c #б
print("Перестановка 1–2 и 3–4:", new1)
new2 = a*1000 + c*100 + b*10 + d #в
print("Перестановка 2–3:", new2)
new3 = c*1000 + d*100 + a*10 + b #г с выделением цифр 1 способ
print("Перестановка (с цифрами):", new3)
# n = ABCD
left = n // 100     # AB
right = n % 100     # CD
new4 = right * 100 + left #г без выделения цифр 2 способ
print("Перестановка (без цифр):", new4)
n = int(input("Введите число n > 9: "))
edin = n % 10
des = (n // 10) % 10
print("Единицы:", edin)
print("Десятки:", des)
n = int(input("Введите число n > 99: "))
des = (n // 10) % 10
sot = (n // 100) % 10
print("Десятки:", des)
print("Сотни:", sot)
n = int(input("Введите число n > 999: "))
sot = (n // 100) % 10
tys = (n // 1000) % 10
print("Сотни:", sot)
print("Тысячи:", tys)
target = 237
last = target // 100
rest = target % 100
x = rest + last
print("x =", x)
target = int(input("Введите число (результат): "))
last = target // 100
rest = target % 100
n = rest + last
print("n =", n)
for x in range(100, 1000):
    if (x % 100) * 10 + (x // 100) == 564:
        print(x)
n = int(input("Введите число n(1-999):"))
for x in range(100, 1000):
    if (x % 100) * 10 + (x // 100) == n:
        print(x)
for x in range(100, 1000):
    a = x // 100
    b = (x // 10) % 10
    c = x % 10
    if b*100 + a*10 + c == 546:
        print(x)
n = int(input("Введите число n(10-999):"))
for x in range(100, 1000):
    a = x // 100
    b = (x // 10) % 10
    c = x % 10
    if b*100 + a*10 + c == n:
        print(x)
for x in range(100, 1000):
    a = x // 100
    b = (x // 10) % 10
    c = x % 10
    if c*100 + b*10 + a == 654:
        print(x)
n = int(input("Введите число n(1-999):"))
for x in range(100, 1000):
    a = x // 100
    b = (x // 10) % 10
    c = x % 10
    if c*100 + b*10 + a == n // 10 and n % 10 == c:
        print(x)
a2 = int(input("a2: "))
a1 = int(input("a1: "))
b2 = int(input("b2: "))
b1 = int(input("b1: "))
s1 = a1 + b1
c1 = s1 % 10
carry = s1 // 10
c2 = a2 + b2 + carry
print("Цифра десятков результата:", c2)
print("Цифра единиц результата:", c1)
a3 = int(input("a3: "))
a2 = int(input("a2: "))
a1 = int(input("a1: "))
b2 = int(input("b2: "))
b1 = int(input("b1: "))
s1 = a1 + b1
c1 = s1 % 10
carry = s1 // 10
s2 = a2 + b2 + carry
c2 = s2 % 10
carry2 = s2 // 10
c3 = a3 + carry2
print("Цифра сотен результата:", c3)
print("Цифра десятков результата:", c2)
print("Цифра единиц результата:", c1)
k = int(input("k: "))
pair = (k - 1) // 2
number = 10 + pair
if k % 2 == 1:
    digit = number // 10
else:
    digit = number % 10
print("а) номер пары (с 1):", pair + 1)
print("б) число:", number)
print("в) цифра:", digit)
print("к — четное" if number % 2 == 0 else "к — нечетное")
k = int(input("k: "))
triple = (k - 1) // 3
number = 101 + triple
pos = (k - 1) % 3
if pos == 0:
    digit = number // 100
elif pos == 1:
    digit = (number // 10) % 10
else:
    digit = number % 10
print("Число:", number)
print("Цифра:", digit)
h = int(input("h: "))
m = int(input("m: "))
s = int(input("s: "))
minute_angle = 6*m + 0.1*s
hour_angle = 30*h + 0.5*m + (0.5/60)*s
angle = abs(minute_angle - hour_angle)
if angle > 180:
    angle = 360 - angle
print("Угол между стрелками:", angle)
y = float(input("Угол y: "))
hours = int(y // 30)
minutes = int((y % 30) // 0.5)
print("Полных часов:", hours)
print("Полных минут:", minutes)
def task_349(y):
    hours = y / (2 * math.pi) * 12
    full_hours = int(hours)
    minutes = (hours - full_hours) * 60
    full_minutes = int(minutes)
    minute_angle = minutes / 60 * 2 * math.pi
    return minute_angle, full_hours, full_minutes
y = math.pi / 2
print(task_349(y))
def task_350(h, m):
    angle_h = h * 30 + m * 0.5
    angle_m = m * 6
    diff = (angle_m - angle_h) % 360
    t1 = (360 - diff) / 5.5
    t2a = (90 - diff) % 360 / 5.5
    t2b = (270 - diff) % 360 / 5.5
    t2 = min(t2a, t2b)
    return int(t1), int(t2)
print(task_350(3, 15))
def task_351(a, b):
    result = (a % b == 0) or (b % a == 0)
    return (0, 1)[result]  # True → 1, False → 0
print(task_351(6, 3))
print(task_351(7, 4))