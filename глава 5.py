import math
# # 5.1
# print('20 ' * 10)
# # 5.2
# a = int(input("Введите число: "))
# s = int(input("Сколько раз вывести? "))
#
# for i in range(s):
#     if i == s - 1:
#         print(a)
#     else:
#         print(a, end=' ')
# # 5.3
# # a)
# for i in range(20, 36):
#     print(i)
# # б)
# a = int(input("Введите a (a ≤ 50): "))
# for i in range(a, 51):
#     print(i ** 2)
# # в)
# b = int(input("Введите b (b ≥ 10): "))
# for i in range(10, b + 1):
#     print(i ** 3)
# # г)
# a = int(input("Введите a: "))
# b = int(input("Введите b (b ≥ a): "))
# for i in range(a, b + 1):
#     print(i)
# # 5.4
# # а)
# for i in range(10, 26):  # от 10 до 25 включительно
#     print(i, i + 0.4)
# # б)
# for i in range(25, 36):  # от 25 до 35 включительно
#     print(i, i + 0.5, i - 0.2)
# # 5.5
# # а)
# for i in range(21, 9, -1):
#
#     print(i, i - 1.8)
# # б)
# for i in range(45, 24, -1):
#     print(i, i - 0.5, i - 0.8)
# 5.6
# а)
# for i in range(21, 36):
#     print(i, i - 0.6)
# б)
# for i in range(16, 25):
#     print(i, i - 0.5, i + 0.8)
# 5.7
# price_per_unit = 20.4
#
# for quantity in range(2, 21):
#     total_price = quantity * price_per_unit
#     print(quantity, total_price)
# 5.8
# print("Фунты  Кг")
# for pounds in range(1, 11):
#     kg = pounds * 0.453
#     print(pounds, kg)
# 5.9
# print("Дюймы  См")
# for inches in range(10, 23):
#     cm = inches * 2.54
#     print(inches, cm)
# 5.10
# a = float(input("Введите курс доллара к рублю: "))
# print("Доллары  Рубли")
# for dollars in range(1, 21):
#     rubles = round(dollars * a, 2)
#     print(dollars, rubles)
# 5.11
# R = 6350
# print("Высота (км)  Расстояние до горизонта (км)")
# for h in range(1, 11):
#     d = math.sqrt(2 * R * h)
#     print(f"{h:>10}  {d:>22.2f}")
# 5.12
# p0 = 1.29
# z = 1.25e-4
# print("Высота (м)  Плотность (кг/м³)")
# for h in range(0, 1001, 100):
#     p = p0 * math.exp(-h * z)
#     print(f"{h:>9}  {p:>14.4f}")
# 5.13
# for i in range(1, 10):
#     print(f"{i:>2} х 7 = {i * 7:>2}")
# 5.14
# for i in range(1, 10):
#     print(f"{i:>2} х 9 = {i * 9:>2}")
# 5.15
# n = int(input("Введите число n (1 ≤ n ≤ 9): "))
# for i in range(1, 10):
#     print(f"{i} × {n} = {i * n}")
# 5.16
# import math
# for i in range(2, 16):
#     print(math.sin(i))
# 5.17
# for x in range(4, 29):
#     t = x + 3
#     y = 3 * t**2 + 4.87 * t - 3
#     print(f"x = {x}, y = {y:.2f}")
# 5.18
# for a in range(2, 18):
#     t = 3 * a
#     z = 4.3 * t**2 - 8 * t + 13
#     print(f"a = {a}, z = {z:.2f}")
# 5.19
# x = 0.1
# while x <= 1.5:
#     print(f"{math.sin(x):.4f}")
#     x += 0.1
# 5.20
# for i in range(1, 10):
#     print(f"{i / 10:.1f}")
# 5.21
# p = float(input("Введите стоимость 1 кг сыра: "))
# print("Масса (г)  Стоимость")
# for grams in range(50, 1001, 50):
#     cost = p * grams / 1000
#     print(f"{grams:>5} г   {cost:.2f}")
# 5.22
# p = float(input("Введите стоимость 1 кг конфет: "))
# print("Масса (г)  Стоимость")
# for grams in range(100, 2001, 100):
#     cost = p * grams / 1000
#     print(f"{grams:>5} г   {cost:.2f}")
# 5.23
# x = 2.1
# while x <= 2.8:
#     print(f"{x:.1f}")
#     x += 0.1
# 5.24
# x = 3.2
# while x <= 3.9:
#     print(f"{x:.1f}")
#     x += 0.1
# 5.25
# x = 2.2
# while x <= 4.2:
#     print(f"{x:.1f}")
#     x += 0.2
# 5.26
# x = 4.4
# while x <= 6.4:
#     print(f"{x:.1f}")
#     x += 0.2
# 5.27
# a)
# a1 = 200
# an = 600
# n = an - a1 + 1
# S = n * (a1 + an) // 2
# print(f"Сумма от 200 до 600: {S}")
# б)
# a = int(input("Введите a (a ≤ 400): "))
# if a <= 400:
#     n = 400 - a + 1
#     S = n * (a + 400) // 2
#     print(f"Сумма от {a} до 400: {S}")
# else:
#     print("Ошибка: a должно быть ≤ 400!")
# в)
# b = int(input("Введите b (b ≥ -15): "))
# if b >= -15:
#     n = b - (-15) + 1
#     S = n * (-15 + b) // 2
#     print(f"Сумма от -15 до {b}: {S}")
# else:
#     print("Ошибка: b должно быть ≥ -15!")
# г)
# start = int(input("Начало диапазона: "))
# end = int(input("Конец диапазона: "))
# if start <= end:
#     n = end - start + 1
#     S = n * (start + end) // 2
#     print(f"Сумма от {start} до {end}: {S}")
# else:
#     print("Ошибка: начало диапазона должно быть ≤ конца!")
# 5.28
# # a)
# p = 1
# for i in range(7, 15):
#     p *= i
# print("Произведение от 7 до 14 =", p)
# # б)
# a = int(input("Введите a (1 ≤ a ≤ 15): "))
#
# p = 1
# for i in range(a, 16):
#     p *= i
# print("Произведение от", a, "до 15 =", p)
# # в)
# b = int(input("Введите b (1 ≤ b ≤ 10): "))
# p = 1
# for i in range(1, b + 1):
#     p *= i
# print("Произведение от 1 до", b, "=", p)
# # г)
# a = int(input("Введите a: "))
# b = int(input("Введите b (b ≥ a): "))
# p = 1
# for i in range(a, b + 1):
#     p *= i
# print("Произведение от", a, "до", b, "=", p)
# 5.28
# а)
# s = 0
# count = 0
# for i in range(1, 751):
#     s += i
#     count += 1
# avg = s / count
# print("Среднее от 1 до 750 =", avg)
# б)
# b = int(input("Введите b (b ≥ 150): "))
# s = 0
# count = 0
# for i in range(150, b + 1):
#     s += i
#     count += 1
# avg = s / count
# print("Среднее от 150 до", b, "=", avg)
# в)
# a = int(input("Введите a (a ≤ 200): "))
# s = 0
# count = 0
# for i in range(a, 201):
#     s += i
#     count += 1
# avg = s / count
# print("Среднее от", a, "до 200 =", avg)
# г)
# a = int(input("Введите a: "))
# b = int(input("Введите b (b ≥ a): "))
# s = 0
# count = 0
# for i in range(a, b + 1):
#     s += i
#     count += 1
# avg = s / count
# print("Среднее от", a, "до", b, "=", avg)
# 5.30
# а)
# s = 0
# for i in range(25, 41):
#     s += i**3
# print("Сумма кубов от 25 до 40 =", s)
# б)
# a = int(input("Введите a (0 ≤ a ≤ 50): "))
# s = 0
# for i in range(a, 51):
#     s += i**2
# print("Сумма квадратов от", a, "до 50 =", s)
# в)
# n = int(input("Введите n (1 ≤ n ≤ 100): "))
# s = 0
# for i in range(1, n + 1):
#     s += i**2
# print("Сумма квадратов от 1 до", n, "=", s)
# г)
# a = int(input("Введите a: "))
# b = int(input("Введите b (b ≥ a): "))
# s = 0
# for i in range(a, b + 1):
#     s += i**2
# print("Сумма квадратов от", a, "до", b, "=", s)
# 5.31
# n = int(input("Введите натуральное число n: "))
# s = 0
# for i in range(n, 2*n + 1):
#     s += i**2
# print("Сумма =", s)
# 5.32
# s = 0
# for i in range(1, 11):
#     s += 1/i
# print("Сумма =", s)
# 5.33
# s = 0
# for i in range(2, 11):
#     s += i / (i + 1)
# print("Сумма =", s)
# 5.34
# n = int(input("Введите значение n: "))
# s = 0
# for i in range(1, n + 1):
#     s += i**2
# print("Сумма квадратов от 1 до", n, "=", s)
# 5.35
# n = int(input("Введите n (n ≥ 2): "))
# s = n * (n - 1) * (n + 1) // 3
# print("Сумма:", s)
# 5.36
# s = 0
# term = 1.0
# for _ in range(9):
#     s += term
#     term /= 3
# print(s)
# 5.37
# n = int(input("Введите n (n ≥ 1): "))
# s = 0.0
# sign = 1
# for k in range(1, n + 1):
#     s += sign / k
#     sign = -sign
# print(s)
# 5.38
# x = 2
# s = 0.0
# power = x
# for k in range(1, 12, 2):
#     s += power / k
#     power *= x * x
# print(s)
# 5.39
# x = 2
# s = 0.0
# power = 1
# sign = 1
# for k in range(1, 12):
#     s += sign * (k / (k + 1)) * power
#     power *= x
#     sign = -sign
# print(s)
# 5.40
# n = int(input("Введите 9-значное число: "))
# s = 0
# while n > 0:
#     s += n % 10
#     n //= 10
# print("Сумма цифр:", s)
# 5.41
# x = int(input("Введите натуральное число: "))
# n = int(input("Введите n: "))
# s = 0
# p = 1
# for _ in range(n):
#     digit = x % 10
#     s += digit
#     p *= digit
#     x //= 10
# print("Сумма:", s)
# print("Произведение:", p)
# 5.42
# N = 100
# position = 0.0
# direction = 1
# total_path = 0.0
# for k in range(1, N + 1):
#     step = 1 / k
#     position += direction * step
#     total_path += step
#     direction = -direction
# print("Расстояние от дома после 100 этапов:", position)
# print("Общий пройденный путь:", total_path)
# 5.43
# n = int(input("Введите n: "))
# a = 1.0
# print(f"a0 = {a}")
# for k in range(1, n + 1):
#     a = k * a + 1 / k
#     print(f"a{k} = {a}")
# 5.44
# а)
# n = int(input("Введите n (n ≥ 3): "))
# f1 = 1
# f2 = 1
# for _ in range(3, n + 1):
#     f1, f2 = f2, f1 + f2
# print("n-й член последовательности Фибоначчи:", f2)
# б)
# n = int(input("Введите n (n ≥ 3): "))
# f1 = 1
# f2 = 1
# print(f1, f2, end=' ')
# for _ in range(3, n + 1):
#     f1, f2 = f2, f1 + f2
#     print(f2, end=' ')
# 5.45
# print("n  F(n)")
# a, b = 1, 1
# for n in range(3, 11):
#     c = a + b
#     print(f"{n}  {c}")
#     a, b = b, c
# 5.46
# а)
# k = int(input("Введите k (k ≥ 1): "))
# if k == 1:
#     print("k-й член: 1/1")
# elif k == 2:
#     print("k-й член: 2/1")
# else:
#     num1, den1 = 1, 1  # 1/1
#     num2, den2 = 2, 1  # 2/1
#     for i in range(3, k + 1):
#         num_next = num1 + num2
#         den_next = den1 + den2
#         num1, num2 = num2, num_next
#         den1, den2 = den2, den_next
#     print(f"k-й член: {num_next}/{den_next}")
# б)
# n = int(input("Введите n (n ≥ 1): "))
# if n >= 1:
#     print("1/1", end=" ")
# if n >= 2:
#     print("2/1", end=" ")
# if n > 2:
#     num1, den1 = 1, 1  # F₁
#     num2, den2 = 2, 1  # F₂
#     for i in range(3, n + 1):
#         num_next = num1 + num2
#         den_next = den1 + den2
#         print(f"{num_next}/{den_next}", end=" ")
#         num1, num2 = num2, num_next
#         den1, den2 = den2, den_next
# print()
# 5.47
# def calculate_v_n(n):
#     if n < 4:
#         raise ValueError("n должно быть >= 4")
#     v = [0, 0, 1.5]
#     for i in range(3, n):
#         idx_i_minus_1 = i - 1
#         idx_i_minus_2 = i - 2
#         idx_i_minus_5 = i - 5
#         v_i_minus_5 = v[idx_i_minus_5] if idx_i_minus_5 >= 0 else 0
#         v_i = ((i) / ((i + 1) ** 2 + 1)) * v[idx_i_minus_1] - v[idx_i_minus_2] + v_i_minus_5
#         v.append(v_i)
#     return v[n - 1]
# n = int(input("Введите n (n >= 4): "))
# result = calculate_v_n(n)
# print(f"v_{n} = {result}")
# 5.48
# initial_cells = 1
# division_interval = 3
# time_points = range(3, 25, 3)
# print("Количество амеб в зависимости от времени:")
# for hours in time_points:
#     number_of_divisions = hours // division_interval
#     cells_count = initial_cells * (2 ** number_of_divisions)
#     print(f"Через {hours} часов: {cells_count} клеток")
# 5.49
# a)
# initial_amount = 1000
# monthly_rate = 0.02
# amount = initial_amount
# print("Прирост суммы по месяцам:")
# for month in range(1, 11):
#     increase = amount * monthly_rate
#     print(f"Месяц {month}: {increase:.2f} руб.")
#     amount += increase
# # b)
# initial_amount = 1000
# monthly_rate = 0.02
# print("\nСумма вклада через 3–12 месяцев:")
# for month in range(3, 13):
#     total = initial_amount * (1 + monthly_rate) ** month
#     print(f"Месяц {month}: {total:.2f} руб.")
# 5.50
# a)
# initial_distance = 10
# daily_increase_rate = 0.10
# distance = initial_distance
# print("Пробег лыжника за 2–10 день:")
# for day in range(2, 11):
#     distance *= (1 + daily_increase_rate)
#     print(f"День {day}: {distance:.2f} км")
# # b)
# initial_distance = 10
# daily_increase_rate = 0.10
# distance = initial_distance
# total_distance = distance
# for day in range(2, 8):
#     distance *= (1 + daily_increase_rate)
#     total_distance += distance
# print(f"\nСуммарный путь за первые 7 дней: {total_distance:.2f} км")
# 5.51
# a)
# initial_area = 100
# initial_yield = 20
# area_increase_rate = 0.05
# yield_increase_rate = 0.02
# current_yield = initial_yield
# print("Урожайность за 2–8 год (ц/га):")
# for year in range(2, 9):
#     current_yield *= (1 + yield_increase_rate)
#     print(f"Год {year}: {current_yield:.2f} ц/га")
# #b)
# initial_area = 100
# initial_yield = 20
# area_increase_rate = 0.05
# yield_increase_rate = 0.02
# current_area = initial_area
# for year in range(2, 8):
#     current_area *= (1 + area_increase_rate)
#     if 4 <= year <= 7:
#         print(f"Год {year}: {current_area:.2f} га")
# c)
# initial_area = 100
# initial_yield = 20
# area_increase_rate = 0.05
# yield_increase_rate = 0.02
# current_area = initial_area
# current_area = initial_area
# current_yield = initial_yield
# total_harvest = current_area * current_yield
# for year in range(2, 7):
#     current_area *= (1 + area_increase_rate)
#     current_yield *= (1 + yield_increase_rate)
#     total_harvest += current_area * current_yield
# print(f"\nОбщий урожай за первые 6 лет: {total_harvest:.2f} ц")
# 5.52
# num_balls = 12
# wall_thickness = 0.5
# inner_diameter = 10
# def sphere_volume(diameter):
#     radius = diameter / 2
#     return (4/3) * math.pi * radius**3
# total_volume_cm3 = 0
# current_inner_diameter = inner_diameter
# for i in range(num_balls):
#     outer_diameter = current_inner_diameter + 2 * wall_thickness
#     wall_volume = sphere_volume(outer_diameter) - sphere_volume(current_inner_diameter)
#     total_volume_cm3 += wall_volume
#     current_inner_diameter = outer_diameter
# total_volume_liters = total_volume_cm3 / 1000
# print(f"Суммарный объем стенок 12 шаров: {total_volume_liters:.3f} л")
# 5.53
# start = 22
# end = 210
# total = 0
# for number in range(start, end + 1):
#     total += number
# print(f"Сумма чисел от {start} до {end} = {total}")
# 5.54
# a = float(input("Введите число a: "))
# n = int(input("Введите натуральное число n: "))
# current = a
# print("Последовательность:")
# for i in range(1, n + 1):
#     print(f"a{i} = {current}")
#     current *= a
# # 5.55
# n = 10
# total = 0
# sign = -1
# for i in range(1, n + 1):
#     total += sign * i * i
#     sign *= -1
# print(f"Сумма последовательности = {total}")
# 5.56
# a = 0
# b = math.pi
# n = 1000
# dx = (b - a) / n
# area = 0
# for i in range(n):
#     x1 = a + i * dx
#     x2 = a + (i + 1) * dx
#     area += (math.sin(x1) + math.sin(x2)) / 2 * dx
# print(f"Приближенная площадь под одной аркой синусоиды: {area:.5f}")
# 5.57
# def f(x):
#     return 0.3 * (x - 1)**2 + 3
# y1 = 2
# y2 = 4
# x_min = 1 - math.sqrt((y2 - 3)/0.3)
# x_max = 1 + math.sqrt((y2 - 3)/0.3)
# n = 1000
# dx = (x_max - x_min) / n
# area = 0
# for i in range(n):
#     x1 = x_min + i * dx
#     x2 = x_min + (i + 1) * dx
#     y1_val = max(2, min(f(x1), 4))
#     y2_val = max(2, min(f(x2), 4))
#     area += (y1_val + y2_val) / 2 * dx
# print(f"Приближенная площадь фигуры: {area:.5f}")
# 5.58
# def f(x):
#     return 0.4 * (x + 2)**2 + 1
# x_left = -2 - math.sqrt(2.5)
# x_right = 0  # ось ординат
# n = 1000
# dx = (x_right - x_left) / n
# area = 0
# for i in range(n):
#     x1 = x_left + i * dx
#     x2 = x_left + (i + 1) * dx
#     y1_val = min(f(x1), 2)
#     y2_val = min(f(x2), 2)
#     area += (y1_val + y2_val) / 2 * dx
# print(f"Приближенная площадь фигуры: {area:.5f}")
# 5.59
# n = int(input("Введите натуральное число n: "))
# if n < 1:
#     print("Число должно быть натуральным (n >= 1).")
# else:
#     factorial = 1
#     for i in range(1, n + 1):
#         factorial *= i
#     print(f"Факториал числа {n} = {factorial}")
# 5.60
# n = int(input("Введите целое число n: "))
# a = float(input("Введите вещественное число a: "))
# negative = False
# if n < 0:
#     negative = True
#     n = -n
# result = 0.0
# for _ in range(n):
#     result += a
# if negative:
#     result = -result
# print(f"Произведение {n} и {a} = {result}")
# 5.61
# x = int(input("Введите натуральное число x: "))
# y = int(input("Введите натуральное число y: "))
# product1 = 0
# for _ in range(y):
#     product1 += x
# print(f"Произведение {x} и {y} (метод 1) = {product1}")
# 5.62
# a = float(input("Введите вещественное число a: "))
# n = int(input("Введите целое число n: "))
# if n == 0:
#     result = 1
# else:
#     result = 1
#     exponent = abs(n)
#     for _ in range(exponent):
#         result *= a
#     if n < 0:
#         result = 1 / result
# print(f"{a}^{n} = {result}")
# 5.63
# result = 20**2 - 19**2
# for i in range(18, 1, -1):
#     result = (result - i**2)**2
# result = (result - 1**2)**2
# print(f"Значение выражения = {result}")
# 5.64
# number = int(input("Введите семизначное число: "))
# if 1000000 <= number <= 9999999:
#     reversed_number = 0
#     temp = number
#     while temp > 0:
#         digit = temp % 10
#         reversed_number = reversed_number * 10 + digit
#         temp //= 10
#     print(f"Число, читаемое справа налево: {reversed_number}")
# else:
#     print("Ошибка: число не семизначное")
# 5.65
# n = int(input("Введите натуральное число n: "))
# square = 0
# for i in range(1, 2*n, 2):
#     square += i
# print(f"{n}^2 = {square}")
# 5.66
# sum_squares = 0
# for n in range(1, 13):
#     square = 0
#     odd = 1
#     for _ in range(n):
#         square += odd
#         odd += 2
#     sum_squares += square
# print("Сумма квадратов от 1 до 12:", sum_squares)
# 5.67
# n = int(input("Введите натуральное число n: "))
# start = n * (n - 1) + 1
# cube = 0
# for i in range(n):
#     cube += start
#     start += 2
# print(f"{n}^3 =", cube)
# 5.68
# n = int(input("Введите число n (2 ≤ n ≤ 10): "))
# factorial = 1
# sum_factorials = 0
# for i in range(1, n + 1):
#     factorial *= i
#     sum_factorials += factorial
# print("Сумма факториалов от 1 до", n, ":", sum_factorials)
# 5.69
# n = int(input("Введите n (1 < n <= 10): "))
# if n <= 1 or n > 10:
#     print("Ошибка: n должно быть в диапазоне (1, 10].")
# else:
#     sum_result = 1.0
#     factorial = 1
#     for i in range(1, n + 1):
#         factorial *= i
#         sum_result += 1 / factorial
#     print(f"Сумма равна: {sum_result}")
# 5.70
# n = int(input("Введите n (1 <= n <= 10): "))
# x = float(input("Введите x: "))
# if n < 1 or n > 10:
#     print("Ошибка: n должно быть в диапазоне [1, 10].")
# else:
#     sum_result = 1.0
#     factorial = 1
#     power_x = 1
#     for i in range(1, n + 1):
#         factorial *= i
#         power_x *= x
#         sum_result += power_x / factorial
#     print(f"Сумма равна: {sum_result}")
# 5.71
# sum_result = 0
# for i in range(1, 51):
#     sum_result += math.sqrt(i)
# print(f"Сумма равна: {sum_result}")
# 5.72
# а)
# n = int(input("Введите n: "))
# sum_result = 0
# sin_sum = 0
# for i in range(1, n + 1):
#     sin_sum += math.sin(i)
#     sum_result += 1 / sin_sum
# print(f"Сумма равна: {sum_result}")
# б)
# n = int(input("Введите n: "))
# sum_result = n * math.sqrt(2)
# print(f"Сумма равна: {sum_result}")
# в)
# n = int(input("Введите n: "))
# sum_result = 0
# sin_sum = 0
# cos_sum = 0
# for i in range(1, n + 1):
#     sin_sum += math.sin(i)
#     cos_sum += math.cos(i)
#     sum_result += cos_sum / sin_sum
# print(f"Сумма равна: {sum_result}")
# г)
# n = int(input("Введите n: "))
# sum_result = 0
# for i in range(1, n + 1):
#     sum_result += math.sqrt(3 * i)
# print(f"Сумма равна: {sum_result}")
# 5.73
# L = 4.5
# x = 3.0
# step = 0.2
# print("Расстояние (м)  Угол (градусы)")
# while x <= L:
#     angle_rad = math.acos(x / L)
#     angle_deg = math.degrees(angle_rad)
#     print(f"{x:>12.1f}  {angle_deg:>13.2f}")
#     x += step
# 5.74
# for i in range(10, 101):
#     if i % 2 != 0:
#         print(i)
# 5.75
# for i in range(100, 201):
#     if i % 3 == 0:
#         print(i)
# 5.76
# a = int(input("Введите a: "))
# b = int(input("Введите b: "))
# c = int(input("Введите c: "))
# for i in range(a, b + 1):
#     if i % c == 0:
#         print(i)
# 5.77
# for i in range(10, 100):
#     if i % 2 != 0 and (i % 10 == 3 or i % 10 == 7):
#         print(i)
# 5.78
# for i in range(100, 1000):
#     if i % 47 == 43 and i % 43 == 45:
#         print(i)
# 5.79
# for i in range(1000, 10000):
#     if i % 133 == 125 and i % 134 == 111:
#         print(i)
# 5.80
# n = int(input("Введите n (0–9): "))
# for i in range(10, 100):
#     if i % n == 0 or str(n) in str(i):
#         print(i)
# 5.81
# а)
# for i in range(100, 1000):
#     if i * i % 1000 == i:
#         print(i)
# б)
# for i in range(100, 1000):
#     if i % 7 == 0:
#         s = sum(map(int, str(i)))
#         if s % 7 == 0:
#             print(i)
# 5.82
# а)
# for i in range(10, 100):
#     a = i // 10
#     b = i % 10
#     if (a*a + b*b) % 13 == 0:
#         print(i)
# б)
# for i in range(10, 100):
#     s = sum(map(int, str(i)))
#     if s + s * s == i:
#         print(i)
# 5.83
# s = 0
# for i in range(1, 50):
#     if i % 2 != 0:
#         s += i
# print("Сумма =", s)
# 5.84
# s = 0
# for i in range(100, 1000):
#     if i % 2 == 0:
#         s += i
# print("Сумма =", s)
# 5.85
# a = int(input("Введите a: "))
# b = int(input("Введите b: "))
# s = 0
# for i in range(a, b + 1):
#     if i > 0 and i % 4 == 0:
#         s += i
# print("Сумма =", s)
# 5.86
# s = 0
# for i in range(31, 100):
#     if i % 3 == 0 and i % 10 in (2, 4, 8):
#         s += i
# print("Сумма =", s)
# 5.87
# count = 0
# for i in range(100, 501):
#     if sum(map(int, str(i))) == 15:
#         count += 1
# print("Количество =", count)
# 5.88
# s = int(input("Введите s: "))
# count = 0
# for i in range(100, 1000):
#     if sum(map(int, str(i))) == s:
#         count += 1
# print("Количество =", count)
# 5.89
# count = 0
# for i in range(100, 1000):
#     if i % 7 == 0 and sum(map(int, str(i))) % 7 == 0:
#         count += 1
# print("Количество =", count)
# 5.90
# n = int(input("Введите n: "))
# a, b = 1, 1
# s = a
# for _ in range(2, n + 1):
#     a, b = b, a + b
#     s += a
# if s % 2 == 0:
#     print("Сумма четная")
# else:
#     print("Сумма нечетная")
# 5.91
# n = int(input("Введите число n: "))
# d = int(input("Введите d: "))
# divs = []
# for i in range(1, n + 1):
#     if n % i == 0:
#         divs.append(i)
# print("а) Делители:", divs)
# print("б) Сумма делителей:", sum(divs))
# print("в) Сумма четных делителей:", sum(x for x in divs if x % 2 == 0))
# print("г) Количество делителей:", len(divs))
# print("д) Количество нечетных делителей:", sum(1 for x in divs if x % 2 != 0))
# print("е) Четных делителей:", sum(1 for x in divs if x % 2 == 0))
# print("ж) Делителей больше d:", sum(1 for x in divs if x > d))
# 5.92
# n = int(input("Введите число: "))
# is_prime = n > 1
# for i in range(2, int(n ** 0.5) + 1):
#     if n % i == 0:
#         is_prime = False
#         break
# if is_prime:
#     print("Число простое")
# else:
#     print("Число не простое")
# 5.93
# n = int(input("Введите число: "))
# s = 0
# for i in range(1, n):
#     if n % i == 0:
#         s += i
# if s == n:
#     print("Число совершенное")
# else:
#     print("Число не совершенное")
# 5.94
# n = int(input("Введите n: "))
# for i in range(1, int(n ** 0.5) + 1):
#     print(i)