import random

print('Это игра "Угадай число"')
chise = 'y'
while chise == 'y':
    print('Я загадал число от 1 до 10, у тебя есть 3 порытки чтобы угадать его')
    pc_number = random.randint(1, 10)
    print("Число от пк", + pc_number)
    counter = 1
    while counter < 4:
        print("Попитка №", + counter)
        user_number = int (input("Введи свое число ->"))
        if user_number > pc_number:
            print("\n")
            print("Твое число больше")
        elif user_number < pc_number:
            print("\n")
            print("Твое число меньше")
        else:
            print("\n")
            print("Ты угадал")
            break
        counter += 1
        print("\n")
    else:
        print("Ты проиграл") 
    print("\n")   
    chise = input('Продолжить? y/n ->')
