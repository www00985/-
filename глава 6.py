import math
#  глава 6
# 6.1
# a = int(input("Введите a: "))
# b = int(input("Введите b: "))
# quotient = 0
# remainder = a
#
# while remainder >= b:
#     remainder -= b
#     quotient += 1
# print("Целая часть:", quotient)
# print("Остаток:", remainder)
# 6.2
# n = int(input("Введите n: "))
# i = 1
# while i <= n:
#     print(i, end=" ")
#     i += 1
# 6.3
# i = 11
# while i <= 100:
#     print(i, end=" ")
#     i += 2
# 6.4
# x = 191
# while x % 17 != 0:
#     x += 1
# print(x)
# 6.5
# x = 5000
# while x % 139 != 0:
#     x -= 1
# print(x)
# 6.6
# fact = int(input("Введите факториал: "))
# n = 1
# current = 1
# while current < fact:
#     n += 1
#     current *= n
# if current == fact:
#     print("Число:", n)
# else:
#     print("Такого натурального числа не существует")
# 6.7
# n = int(input("Введите n: "))
# i = 1
# while i * i <= n:
#     print(i, end=" ")
#     i += 1
# 6.8
# n = int(input("Введите n: "))
# i = 1
# while i <= 100:
#     if i * i > n:
#         print(i)
#         break
#     i += 1
# 6.9
# while True:
#     x = int(input("Введите четное число: "))
#     if x % 2 == 0:
#         break
#     print("Ошибка! Число нечетное.")
# 6.10
# PASSWORD = 1234
# while True:
#     x = int(input("Введите пароль: "))
#     if x == PASSWORD:
#         print("Добро пожаловать!")
#         break
#     print("Неверный пароль!")
# 6.11
# count = 0
# while count < 10:
#     x = int(input("Введите число: "))
#     if x == 0:
#         break
#     count += 1
# 6.12
# while True:
#     x = int(input("Введите число: "))
#     print("Вы ввели число:", x)
#     if x == 0:
#         break
# 6.13
# а)
# i = 10
# while i <= 30:
#     print(i)
#     i += 1
# б)
# i = 10
# while True:
#     print(i)
#     i += 1
#     if i > 30:
#         break
# 6.14
# i = 100
# while i >= 80:
#     print(i)
#     i -= 1
# 6.15
# for n in range(21, 152, 10):
#     print(2 * n)
# 6.16
# #for i in range(2, 25):
#     n = i * 0.5
#     print(n)
# 6.17
# x = 1.0
# while x <= 13.5:
#     print(x)
#     x += 0.5
# 6.18
# а)
# a = int(input("Введите a: "))
# b = int(input("Введите b: "))
# i = a
# while i >= b:
#     print(math.sqrt(i))
#     i -= 1
# б)
# i = a
# while True:
#     print(math.sqrt(i))
#     i -= 1
#     if i < b:
#         break
# 6.19
# n = int(input("Введите число: "))
# while n > 0:
#     print(n % 10)
#     n //= 10
# 6.20
# n = int(input("Введите число: "))
# temp = n
# sum_digits = 0
# count = 0
# product = 1
# sum_sq = 0
# sum_cube = 0
# last_digit = n % 10
# while temp > 0:
#     digit = temp % 10
#     sum_digits += digit
#     product *= digit
#     sum_sq += digit ** 2
#     sum_cube += digit ** 3
#     count += 1
#     first_digit = digit
#     temp //= 10
# average = sum_digits / count
# print("Сумма цифр:", sum_digits)
# print("Количество цифр:", count)
# print("Произведение цифр:", product)
# print("Среднее арифметическое:", average)
# print("Сумма квадратов:", sum_sq)
# print("Сумма кубов:", sum_cube)
# print("Первая цифра:", first_digit)
# print("Сумма первой и последней цифр:", first_digit + last_digit)
# 6.21
# n = int(input("Введите число (>9): "))
# while n >= 100:
#     n //= 10
# print(n % 10)
# 6.22
# n = int(input("Введите число (>99): "))
# while n >= 1000:
#     n //= 10
# print(n % 10)
# 6.23
# n = int(input("Введите число: "))
# m = int(input("Введите m: "))
# s = 0
# count = 0
# while n > 0 and count < m:
#     s += n % 10
#     n //= 10
#     count += 1
# print("Сумма:", s)
# 6.24
# а)
# n = int(input("Введите число: "))
# s = 0
# sign = 1
# while n > 0:
#     digit = n % 10
#     s += sign * digit
#     sign = -sign
#     n //= 10
# print(s)
# б)
# n = int(input("Введите число: "))
# temp = n
# digits = 0
# while temp > 0:
#     digits += 1
#     temp //= 10
# s = 0
# sign = 1
# while n > 0:
#     digit = n % 10
#     s += sign * digit
#     sign = -sign
#     n //= 10
# if digits % 2 == 0:
#     s = -s
# print(s)
# 6.25
# n = int(input("Введите число: "))
# d = 2
# while n % d != 0:
#     d += 1
# print(d)
# 6.26
# а)
# for i in range(13, 100, 13):
#     print(i)
# б)
# i = 13
# while i < 100:
#     print(i)
#     i += 13
# 6.27
# count = 0
# x = 100
# while count < 15:
#     if x % 19 == 0:
#         print(x)
#         count += 1
#     x += 1
# 6.28
# count = 0
# x = 500
# while count < 20:
#     if x % 13 == 0 or x % 17 == 0:
#         print(x)
#         count += 1
#     x += 1
# 6.29
# count = 0
# x = 100
# while count < 10:
#     if x % 10 == 7 and x % 9 == 0:
#         print(x)
#         count += 1
#     x += 1
# 6.30
# a = int(input("Введите a: "))
# b = int(input("Введите b: "))
# q = 0
# temp = b
# while temp >= a:
#     temp -= a
#     q += 1
# print("Результат:", q)
# 6.31
# deposit = 1000
# month = 0
# # а)
# temp = deposit
# while True:
#     increase = temp * 0.02
#     month += 1
#     temp += increase
#     if increase > 30:
#         print("а) За месяц:", month)
#         break
#
# б)
# deposit = 1000
# month = 0
# while deposit <= 1200:
#     deposit += deposit * 0.02
#     month += 1
# print("б) Через месяцев:", month)
# 6.32
# day = 1
# distance = 10
# # а)
# while distance <= 20:
#     distance += distance * 0.1
#     day += 1
# print("а) День:", day)
# # б)
# day = 1
# distance = 10
# total = 10
# while total <= 100:
#     distance += distance * 0.1
#     total += distance
#     day += 1
# print("б) День:", day)
# 6.33
# year = 1
# area = 100
# yield_per_ha = 20
# total_harvest = area * yield_per_ha
# # а)
# while yield_per_ha <= 22:
#     yield_per_ha += yield_per_ha * 0.02
#     year += 1
# print("а) Год:", year)
# # б)
# year = 1
# area = 100
# while area <= 120:
#     area += area * 0.05
#     year += 1
# print("б) Год:", year)
# в)
# year = 1
# area = 100
# yield_per_ha = 20
# total = area * yield_per_ha
# while total <= 800:
#     area += area * 0.05
#     yield_per_ha += yield_per_ha * 0.02
#     total += area * yield_per_ha
#     year += 1
# print("в) Год:", year)
# 6.34
# m = int(input("Введите m: "))
# n = int(input("Введите n: "))
# k = m
# limit = m * n
# while k <= limit:
#     print(k)
#     k += m
# k = n
# while k <= limit:
#     print(k)
#     k += n
# 6.35
# n = int(input("Введите число: "))
# temp = n
# count_3 = 0
# last = n % 10
# count_last = 0
# even_count = 0
# sum_gt5 = 0
# prod_gt7 = 1
# count_0_5 = 0
# while temp > 0:
#     d = temp % 10
#     count_3 += (d == 3)
#     count_last += (d == last)
#     even_count += (d % 2 == 0)
#     sum_gt5 += d * (d > 5)
#     prod_gt7 *= d if d > 7 else 1
#     count_0_5 += (d == 0) + (d == 5)
#     temp //= 10
# print("а)", count_3)
# print("б)", count_last)
# print("в)", even_count)
# print("г)", sum_gt5)
# print("д)", prod_gt7)
# print("е)", count_0_5)
# 6.336
# n = int(input("Введите число: "))
# a = int(input("Введите a (0–8): "))
# x = int(input("Введите x: "))
# y = int(input("Введите y: "))
# temp = n
# count_a = 0
# sum_gt_a = 0
# sum_even = 0
# count_xy = 0
# while temp > 0:
#     d = temp % 10
#     count_a += (d == a)
#     sum_gt_a += d * (d > a)
#     sum_even += d * (d % 2 == 0)
#     count_xy += (d == x) + (d == y)
#     temp //= 10
# print("а)", count_a)
# print("б)", sum_gt_a)
# print("в)", sum_even)
# print("г)", count_xy)
# 6.37
# n = int(input("Введите число: "))
# pos = 1
# answer = 0
# while n > 0:
#     d = n % 10
#     if d == 8:
#         answer = pos
#     n //= 10
#     pos += 1
# print(answer)
# 6.38
# n = int(input("Введите число: "))
# pos = 1
# answer = 0
# while n > 0:
#     d = n % 10
#     if d == 3 and answer == 0:
#         answer = pos
#     n //= 10
#     pos += 1
# print(answer)
# 6.39
# n = int(input("Введите число: "))
# temp = n
# power = 1
# while temp >= 10:
#     temp //= 10
#     power *= 10
# while power > 0:
#     print(n // power)
#     n %= power
#     power //= 10
# 6.40
# n = int(input("Введите число: "))
# temp = n
# while temp >= 10:
#     temp //= 10
# first = temp
# count = 0
# while n > 0:
#     if n % 10 == first:
#         count += 1
#     n //= 10
# print(count)
# 6.41
# n = int(input("Введите число: "))
# max_d = 0
# min_d = 9
# while n > 0:
#     d = n % 10
#     if d > max_d:
#         max_d = d
#     if d < min_d:
#         min_d = d
#     n //= 10
# print("Максимальная:", max_d)
# print("Минимальная:", min_d)
# 6.42
# n = int(input("Введите число: "))
# max_d = 0
# min_d = 9
# while n > 0:
#     d = n % 10
#     if d > max_d:
#         max_d = d
#     if d < min_d:
#         min_d = d
#     n //= 10
# print("а)", max_d, min_d)
# print("б)", max_d - min_d)
# print("в)", max_d + min_d)
# 6.43
# n = int(input("Введите число: "))
# a = int(input("Введите a: "))
# max_d = 0
# min_d = 9
# while n > 0:
#     d = n % 10
#     if d > max_d:
#         max_d = d
#     if d < min_d:
#         min_d = d
#     n //= 10
# print((max_d + min_d) % a == 0)
# 6.44
# n = int(input("Введите число: "))
# max_d = 0
# min_d = 9
# while n > 0:
#     d = n % 10
#     if d > max_d:
#         max_d = d
#     if d < min_d:
#         min_d = d
#     n //= 10
# print((max_d - min_d) % 2 == 0)
# 6.45
# n = int(input("Введите число: "))
# temp = n
# pos = 1
# max_d = -1
# min_d = 10
# pos_max_end = pos_min_end = 0
# while temp > 0:
#     d = temp % 10
#     if d > max_d:
#         max_d = d
#         pos_max_end = pos
#     if d < min_d:
#         min_d = d
#         pos_min_end = pos
#     temp //= 10
#     pos += 1
# length = pos - 1
# print("а) макс от конца:", pos_max_end)
# print("   макс от начала:", length - pos_max_end + 1)
# print("б) мин от конца:", pos_min_end)
# print("   мин от начала:", length - pos_min_end + 1)
# 6.46
# n = int(input("Введите число: "))
# temp = n
# pos = 1
# max_d = -1
# min_d = 10
# pos_max_end = pos_min_end = 0
# while temp > 0:
#     d = temp % 10
#     if d > max_d:
#         max_d = d
#         pos_max_end = pos
#     if d < min_d:
#         min_d = d
#         pos_min_end = pos
#     temp //= 10
#     pos += 1
# length = pos - 1
# print("а) от конца:")
# print("   макс:", pos_max_end)
# print("   мин:", pos_min_end)
# print("б) от начала:")
# print("   макс:", length - pos_max_end + 1)
# print("   мин:", length - pos_min_end + 1)
# 6.47
# n = int(input("Введите число: "))
# temp = n
# pos = 1
# max_d = -1
# min_d = 10
# pos_max = pos_min = 0
# while temp > 0:
#     d = temp % 10
#     if d > max_d:
#         max_d = d
#         pos_max = pos
#     if d < min_d:
#         min_d = d
#         pos_min = pos
#     temp //= 10
#     pos += 1
# if pos_max > pos_min:
#     print("Максимальная левее")
# else:
#     print("Минимальная левее")
# 6.48
# n = int(input("Введите число: "))
# temp = n
# pos = 1
# max_odd = -1
# min_d = 10
# pos_min_end = 0
# while temp > 0:
#     d = temp % 10
#     if d % 2 == 1 and d > max_odd:
#         max_odd = d
#     if d < min_d:
#         min_d = d
#         pos_min_end = pos
#
#     temp //= 10
#     pos += 1
# length = pos - 1
# print("а) Максимальная нечетная цифра:", max_odd)
# print("б) Номер минимальной цифры слева:", length - pos_min_end + 1)
# 6.49
# n = int(input("Введите число: "))
# temp = n
# sum_d = 0
# prod = 1
# count = 0
# last = n % 10
# while temp > 0:
#     d = temp % 10
#     sum_d += d
#     prod *= d
#     first = d
#     count += 1
#     temp //= 10
# print("а)", sum_d > 10)
# print("б)", prod < 50)
# print("в)", count % 2 == 0)
# print("г)", count == 4)
# print("д)", first <= 6)
# print("е)", first == last)
# if first > last:
#     print("ж) первая цифра больше")
# elif first < last:
#     print("ж) последняя цифра больше")
# else:
#     print("ж) цифры равны")
# 6.50
# n = int(input("Введите число: "))
# a = int(input("Введите a: "))
# b = int(input("Введите b: "))
# k = int(input("Введите k: "))
# m = int(input("Введите m: "))
# temp = n
# sum_d = 0
# prod = 1
# count = 0
# while temp > 0:
#     d = temp % 10
#     sum_d += d
#     prod *= d
#     first = d
#     count += 1
#     temp //= 10
# print("а)", sum_d < a)
# print("б)", prod > b)
# print("в)", count == k)
# print("г)", first > m)
# 6.51
# n = int(input("Введите число: "))
# k = int(input("Введите k: "))
# b = int(input("Введите b: "))
# x = int(input("Введите x: "))
# y = int(input("Введите y: "))
# a = int(input("Введите a: "))
# m = int(input("Введите m: "))
# n2 = int(input("Введите n: "))
# temp = n
# sum_d = 0
# prod = 1
# count = 0
# last = n % 10
# while temp > 0:
#     d = temp % 10
#     sum_d += d
#     prod *= d
#     first = d
#     count += 1
#     temp //= 10
# print("а)", sum_d > k and n % 2 == 0)
# print("б)", count % 2 == 0 and n <= b)
# print("г)", first == x and last == y)
# print("д)", prod < a and n % b == 0)
# print("е)", sum_d > m and n % n2 == 0)
# 6.52
# n = int(input("Введите число: "))
# has3 = False
# has2 = False
# has5 = False
# while n > 0:
#     d = n % 10
#     if d == 3:
#         has3 = True
#     if d == 2:
#         has2 = True
#     if d == 5:
#         has5 = True
#     n //= 10
# print("а)", has3)
# print("б)", has2 and has5)
# 6.53
# n = int(input("Введите число: "))
# a = int(input("Введите a: "))
# b = int(input("Введите b: "))
# k = int(input("Введите k: "))
# count_a = 0
# has_b = False
# temp = n
# while temp > 0:
#     d = temp % 10
#     if d == a:
#         count_a += 1
#     if d == b:
#         has_b = True
#     temp //= 10
# print("а)", count_a > 0)
# print("б)", not has_b)
# print("в)", count_a > k)
# print("г)", count_a > 0 and has_b)
# 6.54
# n = int(input("Введите число: "))
# count0 = 0
# count9 = 0
# while n > 0:
#     d = n % 10
#     if d == 0:
#         count0 += 1
#     if d == 9:
#         count9 += 1
#     n //= 10
# if count0 > count9:
#     print("0")
# elif count9 > count0:
#     print("9")
# else:
#     print("Одинаково")
# 6.55
# n = int(input("Введите число: "))
# a = int(input("Введите a: "))
# b = int(input("Введите b: "))
# count_a = 0
# count_b = 0
# while n > 0:
#     d = n % 10
#     if d == a:
#         count_a += 1
#     if d == b:
#         count_b += 1
#     n //= 10
# print(count_a < count_b)
# 6.56
# n = int(input("Введите число: "))
# pos = 1
# pos2 = pos5 = 0
# while n > 0:
#     d = n % 10
#     if d == 2:
#         pos2 = pos
#     if d == 5:
#         pos5 = pos
#     n //= 10
#     pos += 1
# if pos2 > 0 and pos5 > 0:
#     if pos2 > pos5:
#         print("2 левее")
#     else:
#         print("5 левее")
# 6.57
# n = int(input("Введите число: "))
# a = int(input("Введите a: "))
# b = int(input("Введите b: "))
# pos = 1
# pos_a = pos_b = 0
# while n > 0:
#     d = n % 10
#     if d == a and pos_a == 0:
#         pos_a = pos
#     if d == b and pos_b == 0:
#         pos_b = pos
#     n //= 10
#     pos += 1
# if pos_a > 0 and pos_b > 0:
#     if pos_a < pos_b:
#         print("a правее")
#     else:
#         print("b правее")
# 6.58
# 1) Два цикла
# #n = int(input("Введите число: "))
# temp = n
# max_d = 0
# while temp > 0:
#     d = temp % 10
#     if d > max_d:
#         max_d = d
#     temp //= 10
# count = 0
# while n > 0:
#     if n % 10 == max_d:
#         count += 1
#     n //= 10
# print(count)
# 2) Один цикл
# n = int(input("Введите число: "))
# max_d = -1
# count = 0
# while n > 0:
#     d = n % 10
#     if d > max_d:
#         max_d = d
#         count = 1
#     elif d == max_d:
#         count += 1
#     n //= 10
# print(count)
# 6.59
# 1) Два цикла
# n = int(input("Введите число: "))
# temp = n
# min_d = 9
# while temp > 0:
#     d = temp % 10
#     if d < min_d:
#         min_d = d
#     temp //= 10
# count = 0
# while n > 0:
#     if n % 10 == min_d:
#         count += 1
#     n //= 10
# print(count)
# 2) Один цикл
# n = int(input("Введите число: "))
# min_d = 10
# count = 0
# while n > 0:
#     d = n % 10
#     if d < min_d:
#         min_d = d
#         count = 1
#     elif d == min_d:
#         count += 1
#     n //= 10
# print(count)
# 6.60
# n = int(input("Введите число: "))
# max1 = max2 = -1
# min1 = min2 = 10
# while n > 0:
#     d = n % 10
#     if d > max1:
#         max2 = max1
#         max1 = d
#     elif d > max2:
#         max2 = d
#     if d < min1:
#         min2 = min1
#         min1 = d
#     elif d < min2:
#         min2 = d
#     n //= 10
# print("а) две максимальные:", max1, max2)
# print("б) две минимальные:", min1, min2)
# 6.61
# n = int(input("Введите число: "))
# pos = 1
# max1 = max2 = -1
# min1 = min2 = 10
# pos_max1 = pos_max2 = 0
# pos_min1 = pos_min2 = 0
# temp = n
# while temp > 0:
#     d = temp % 10
#     if d > max1:
#         max2, pos_max2 = max1, pos_max1
#         max1, pos_max1 = d, pos
#     elif d > max2:
#         max2, pos_max2 = d, pos
#     if d < min1:
#         min2, pos_min2 = min1, pos_min1
#         min1, pos_min1 = d, pos
#     elif d < min2:
#         min2, pos_min2 = d, pos
#     temp //= 10
#     pos += 1
# length = pos - 1
# print("а) максимальные:")
# print("   от конца:", pos_max1, pos_max2)
# print("   от начала:", length - pos_max1 + 1, length - pos_max2 + 1)
# print("б) минимальные:")
# print("   от конца:", pos_min1, pos_min2)
# print("   от начала:", length - pos_min1 + 1, length - pos_min2 + 1)
# 6.62
# n = int(input("Введите число: "))
# a = int(input("Введите цифру a: "))
# # а)
# rev = 0
# temp = n
# while temp > 0:
#     rev = rev * 10 + temp % 10
#     temp //= 10
# print("а)", rev)
# # б)
# print("б)", int("2" + str(n) + "2"))
# # в)
# res = 0
# p = 1
# temp = n
# while temp > 0:
#     d = temp % 10
#     if d != a:
#         res += d * p
#         p *= 10
#     temp //= 10
# print("в)", res)
# # г)
# last = n % 10
# temp = n
# while temp >= 10:
#     temp //= 10
# first = temp
# middle = n // 10 % (10 ** (len(str(n)) - 2)) if len(str(n)) > 2 else 0
# print("г)", last * 10 ** (len(str(n)) - 1) + middle * 10 + first)
# # д)
# print("д)", int(str(n) + str(n)))
# 6.63
# n = int(input("Введите число: "))
# temp = n
# rev = 0
# while temp > 0:
#     rev = rev * 10 + temp % 10
#     temp //= 10
# print(n == rev)
# 6.64
# n = int(input("Введите сумму: "))
# values = [64, 32, 16, 8, 4, 2, 1]
# for v in values:
#     count = n // v
#     if count > 0:
#         print(v, "руб.:", count)
#         n %= v
# 6.65
# a = int(input("Введите a: "))
# b = int(input("Введите b: "))
# while b != 0:
#     a, b = b, a % b
# print("НОД:", a)
# 6.66
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# while b != 0:
#     a, b = b, a % b
# while c != 0:
#     a, c = c, a % c
# print("НОД:", a)
# 6.67
# a = int(input("Введите a: "))
# b = int(input("Введите b: "))
# x, y = a, b
# while y != 0:
#     x, y = y, x % y
# nok = a * b // x
# print("НОК:", nok)
# 6.68
# a = int(input("Числитель: "))
# b = int(input("Знаменатель: "))
# x, y = a, b
# while y != 0:
#     x, y = y, x % y
# p = a // x
# q = b // x
# print("Сокращенная дробь:", p, "/", q)
# 6.69
# a = 425
# b = 131
# while a != 0 and b != 0:
#     if a > b:
#         k = a // b
#         print(f"Квадраты {b}×{b}: {k}")
#         a = a - b * k
#     else:
#         k = b // a
#         print(f"Квадраты {a}×{a}: {k}")
#         b = b - a * k
# 6.70
# a = int(input("Введите a: "))
# b = int(input("Введите b: "))
# while a != 0 and b != 0:
#     if a > b:
#         k = a // b
#         print(f"Квадраты {b}×{b}: {k}")
#         a -= b * k
#     else:
#         k = b // a
#         print(f"Квадраты {a}×{a}: {k}")
#         b -= a * k
# 6.71
# n = int(input("Введите число: "))
# a = 0
# b = 1
# while b < n:
#     a, b = b, a + b
# print(b == n or n == 0)
# 6.72
# n = int(input("Введите n: "))
# f = int(input("Первый член: "))
# s = int(input("Шаг: "))
# if s != 0:
#     print((n - f) % s == 0 and (n - f) // s >= 0)
# else:
#     print(n == f)
# 6.73
# m = int(input("Введите m: "))
# g = int(input("Первый член: "))
# z = int(input("Знаменатель: "))
# x = g
# while x < m:
#     x *= z
# print(x == m)
# 6.74
# а)
# n = int(input("Введите число: "))
# temp = n
# while temp > 1 and temp % 3 == 0:
#     temp //= 3
# print("а)", temp == 1)
# б)
# n = int(input("Введите число: "))
# temp = n
# while temp > 1 and temp % 5 == 0:
#     temp //= 5
# print("б)", temp == 1)
# 6.75
# а)
# def f(x):
#     return x**4 + 2*x**3 - x - 1
# a = 0
# b = 1
# eps = 0.001
# while b - a > eps:
#     c = (a + b) / 2
#     if f(a) * f(c) <= 0:
#         b = c
#     else:
#         a = c
# print("Корень:", (a + b) / 2)
# б)
# def f(x):
#     return x**3 - 0.2*x**2 - 0.2*x - 1.2
# a = 1
# b = 1.5
# eps = 0.001
# while b - a > eps:
#     c = (a + b) / 2
#     if f(a) * f(c) <= 0:
#         b = c
#     else:
#         a = c
# print("Корень:", (a + b) / 2)
# 6.77
# n = int(input("Введите число: "))
# temp = n
# last = temp % 10
# same_all = True
# same_near = False
# prev = last
# temp //= 10
# while temp > 0:
#     d = temp % 10
#     if d != last:
#         same_all = False
#     if d == prev:
#         same_near = True
#     prev = d
#     temp //= 10
# print("а)", same_all)
# print("б)", same_near)
# 6.78
# n = int(input("Введите число: "))
# ok = True
# prev = n % 10
# n //= 10
# while n > 0:
#     d = n % 10
#     if d <= prev:
#         ok = False
#     prev = d
#     n //= 10
# print(ok)
# 6.79
# n = int(input("Введите число: "))
# ok = True
# prev = n % 10
# n //= 10
# while n > 0:
#     d = n % 10
#     if d < prev:
#         ok = False
#     prev = d
#     n //= 10
# print(ok)
# 6.80
# n = int(input("Введите число: "))
# # находим первую цифру
# temp = n
# while temp >= 10:
#     temp //= 10
# prev = temp
# power = 10
# while power <= n:
#     d = (n // power) % 10
#     if d <= prev:
#         print(False)
#         break
#     prev = d
#     power *= 10
# else:
#     print(True)
# 6.81
# n = int(input("Введите число: "))
# temp = n
# while temp >= 10:
#     temp //= 10
# prev = temp
# power = 10
# ok = True
# while power <= n:
#     d = (n // power) % 10
#     if d <= prev:
#         ok = False
#     prev = d
#     power *= 10
# print(ok)
# 6.82
# n = int(input("Введите число: "))
# temp = n
# while temp >= 10:
#     temp //= 10
# prev = temp
# power = 10
# ok = True
# while power <= n:
#     d = (n // power) % 10
#     if d < prev:
#         ok = False
#     prev = d
#     power *= 10
# print(ok)
# 6.83
# n = int(input("Введите число: "))
# temp = n
# while temp >= 10:
#     temp //= 10
# prev = temp
# inc = True
# dec = True
# power = 10
# while power <= n:
#     d = (n // power) % 10
#     if d <= prev:
#         inc = False
#     if d >= prev:
#         dec = False
#     prev = d
#     power *= 10
# print(inc or dec)