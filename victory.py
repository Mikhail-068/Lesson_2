celebrities = {"Гайдна": 1732, "Паганини": 1782, "Брамса": 1833, "Генделя": 1685, "Бетховена": 1770}

res = 'да'
while res != 'нет':
    print('-' * 99)
    print('='* 40, 'В И К Т О Р И Н А', '='* 40,)
    print('-' * 99)

    list_errors = []

    for key, value in celebrities.items():
        age = int(input(f'Введите год рождения {key}\n'))
        if age == value: list_errors.append(1)
        else: list_errors.append(0)

    correct = sum(list_errors)
    error = len(list_errors) - correct

    print()
    print(f'Количество правильных ответов: {correct}')
    print(f'Количество ошибок: {error}')
    print(f'Процент правильных ответов: {correct*100/len(list_errors)}%')

    print('-' * 99)
    res = input('Не хотите ли ещё сыграть?\n').lower()
