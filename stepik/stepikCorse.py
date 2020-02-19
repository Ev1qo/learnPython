# x = int(input())
# h = int(input())
# m = int(input())
# min_when_sleep = h*60 + m + x
# print(min_when_sleep // 60)
# print(min_when_sleep % 60)

# x = 5
# y = 10
# y > x * x or y >= 2 * x and x < y
# y > 25 or y >= 10 and x < y
# False or (False and True)

# a = int(input())
# b = int(input())
# h = int(input())

# if h >= a and h <= b:
#     print("Это нормально")
# elif h > b:
#     print("Пересып")
# else: 
#     print("Недосып")

# a = int(input())

# if (((a % 4) == 0) and ((a % 100) != 0)) or (a % 400) == 0:
#     print("Высокосный")
# else: 
#     print("Обычный")

# a = float(input())
# b = float(input())
# do = input()

# if b == 0.0 and (do == "/" or do == "div" or do == "mod"):
#     print("Деление на 0!")
# elif do == "+":
#     print(a + b)
# elif do == "-":
#         print(a - b)
# elif do == "*":
#     print(a * b)
# elif do == "/" and b != 0.0:
#     print(a / b)
# elif do == "mod" and b != 0.0:
#     print(a % b)
# elif do == "pow":
#     print(a ** b)
# elif do == "div" and b != 0.0:
#     print(a // b)

# shepe_type = input()

# if shepe_type == "треугольник":
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     p = (a + b + c)/2
#     s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# elif shepe_type == "прямоугольник":
#     a = int(input())
#     b = int(input())
#     s = a * b

# elif shepe_type == "круг":
#     a = int(input())
#     s = 3.14 * a**2

# print(float(s))


# a = int(input())
# b = int(input())
# c = int(input())
# if a>b and a>c:
#   max = a
#   if b>c:
#     mid=b
#     min=c
#   else:
#     mid=c
#     min=b
#   print(max)
#   print(min)
#   print(mid)
# elif b>a and b>c:
#   max=b
#   if a>c:
#     mid=a
#     min=c
#   else:
#     mid=c
#     min=a
#   print(max)
#   print(min)
#   print(mid)
# elif c>a and c>b:
#   max=c
#   if a>b:
#     mid=a
#     min=b
#   else:
#     mid=b
#     min=a
#   print(max)
#   print(min)
#   print(mid)
# elif c==a and b==c:
#   max=a
#   min=b
#   mid=c
#   print(max)
#   print(min)
#   print(mid) 
# elif c==a and (b>a or b>c):
#   max=b
#   min=c
#   mid=a
#   print(max)
#   print(min)
#   print(mid) 
# elif c==a and (b<a or b<c):
#   max=a
#   min=b
#   mid=c
#   print(max)
#   print(min)
#   print(mid) 
# elif a==b and (c<b or c<a):
#   max=a
#   min=c
#   mid=b
#   print(max)
#   print(min)
#   print(mid) 
# elif a==b and (c>b or c>a):
#   max=a
#   min=b
#   mid=c
#   print(max)
#   print(min)
#   print(mid) 
# elif c==b and (a>c or a>b):
#   max=a
#   min=c
#   mid=b
#   print(max)
#   print(min)
#   print(mid) 
# elif c==b and (a<c or a<b):
#   max=c
#   min=a
#   mid=b
#   print(max)
#   print(min)
#   print(mid) 
#
# i = 0
# while i <= 10:
#     i = i + 1
#     if i > 7:
#         i = i + 2
# print(i)
# a = 1
# sum = 0
# while a != 0:
#     a = int(input())
#     sum = sum + a
# print(sum)

# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         break
#     i = i + 1
# print(i)

#######################
# Таблица умножения с прямоугольными блоками

# def total(initial=5, *numbers, extra_number):
#     count = initial
#     for number in numbers:
#         count += number
#     count += extra_number
#     print(count)
#
# total(10, 1, 2, 3, extra_number=50)
# #total(10, 1, 2, 3)

# def printMax(x, y):
#     '''Выводит максимальное из двух чисел.
#
#         Оба значения должны быть целыми числами.'''
#     x = int(x) # конвертируем в целые, если возможно
#     y = int(y)
#     if x > y:
#         print(x, 'наибольшее')
#     else:
#         print(y, 'наибольшее')
# printMax(3, 5)
# print(printMax.__doc__)

##########################
# Програма для вывода таблицы умножения введеных чисел

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# for i in range(c, d + 1):
#     print("\t" + str(i), end = "")
# print("")
# for x in range(a, b + 1):
#     print(str(x) + "\t", end="")
#     for g in range(c, d + 1):
#         print(str(g * x) + "\t", end="")
#     print("")

############################################################
# Среднее арихметическое из отрезка чисел что делаляться на 3
a = int(input())
b = int(input())
sum = 0
counter = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        sum += i
        counter += 1
print(sum / counter)