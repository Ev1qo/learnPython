num = int(input())
prog1 = 'программист'
prog2 = 'программиста'
prog3 = 'программистов'


if num >= 0:
    if num % 100 >= 10 and num % 100 <= 20:
        print(num, prog3)
    elif num % 10 == 0:
        print(num, prog3)
    elif num % 10 == 1:
        print(num, prog1)
    elif num % 10 >= 2 and num % 10 <= 4:
        print(num, prog2)
    else:
        print(num, prog3)