writer = 'А.С Пушкина'

age = int(input(f'Год рождения {writer}?\n'))

if age == 1799:
    day = int(input(f'Теперь скажи число рождения {writer}?\n'))
    if day == 6: print('Да, все верно)')
    elif day != 6: print('Неверный день рождения')
else: print("Неверный год рождения")
