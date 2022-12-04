writer = 'А.С Пушкина'

age = 1

while age != 1799:
    age = int(input(f'Год рождения {writer}?\n'))
    if age != 1799: print('Неверно')

print('Верно')