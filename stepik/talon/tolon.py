num = input()

first_part =  int(num[0]) + int(num[1]) + int(num[2])
second_part = int(num[3]) + int(num[4]) + int(num[5])
if first_part == second_part:
    print("Счастливый")
else:
    print("Обычный")