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

a = int(input())

if (((a % 4) == 0) and ((a % 100) != 0)) or (a % 400) == 0:
    print("Высокосный")
else: 
    print("Обычный")