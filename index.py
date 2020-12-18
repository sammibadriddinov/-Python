import random
number = random.randint(1, 100)
print(number)

user_number = None
count = 0
levels = {1:10, 2:5, 3:3}
print('Игра состоит из 3 уровня. В первом уровне у вас есть 10 попыток для угадание чисел,')
print('а во вотором уровне 5 попыток и в третьем уровне 3 попыток ')
level = int(input('Введите уровень сложности: '))

max_count = levels[level]

user_count = int(input('Введите количество участников: '))

users = []

for i in range(user_count):
    user_name = input(f'Введите имя пользователя {i+1}: ')
    users.append(user_name)
print(users)

is_winner = False
winner_name = None

while not is_winner:
    count += 1
    if count > max_count:
        print('Вы проиграли')
        break
    print(f'Попытка №{count}')
    for user in users:
        print(f'Xoд пользователя {user}')
        user_number = int(input('Введите число: '))
        if user_number == number:
            is_winner = True
            winner_name = user
            break
        elif user_number > number:
            print('Ваша число больше')
        elif user_number < number:
            print('Ваша число меньше')
else:
    print(f'Выиграл пользователь по имени {winner_name}')

