import random

print('Это игра "Угадай число"')
print('Я загадал число от 1 до 100, у тебя есть 10 порыток чтобы угадать его')
user_number = input('Введи свое число->')
print(user_number)
pc_number = random.randint(1, 10)
print(pc_number)
