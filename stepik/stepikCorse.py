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

num = input()
rev =  num[::-1]
last_digit = int(rev[0])
# print(num, type(num))
if last_digit == 1 and num != "11" and num != "111" and num != "211" and num != "311" and num != "411" and num != "511" and num != "611" and num != "711" and num != "811" and num != "911":
    print(num, "программист")
if (last_digit == 2 or last_digit == 3 or last_digit == 4) and (num != "112" and num != "113" and num != "114"):
    print(num, "программиста")
if (int(num) >=11 and int(num) <= 19):
    print(num,"программистов")
if last_digit >= 5 and last_digit <= 9:
    print(num,"программистов")
if last_digit == 0:
     print(num,"программистов")
if int(num) == 112 or int(num) == 113 or int(num) == 114 or int(num) == 111 or int(num) == 211 or int(num) == 311 or int(num) == 411 or int(num) == 511 or int(num) == 611 or int(num) == 711 or int(num) == 811 or int(num) == 911:
    print(num,"программистов")