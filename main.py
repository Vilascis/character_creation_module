from random import randint


def attack(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        war_a: int = 5 + randint(3, 5)
        return (f'{char_name} нанёс урон противнику равный {war_a}')
    if char_class == 'mage':
        mag_a: int = 5 + randint(5, 10)
        return (f'{char_name} нанёс урон противнику равный {mag_a}')
    if char_class == 'healer':
        heal_a: int = 5 + randint(-3, -1)
        return (f'{char_name} нанёс урон противнику равный {heal_a}')
    return (f'{char_name} не атаковал')


def defence(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')
    return (f'{char_name} не смог блокировать урон')


def special(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        war_s: int = 80 + 25
        return (f'{char_name} применил специальное '
                f'умение «Выносливость {war_s}»')
    if char_class == 'mage':
        mag_s: int = 5 + 40
        return (f'{char_name} применил специальное умение «Атака {mag_s}»')
    if char_class == 'healer':
        heal_s: int = 10 + 30
        return (f'{char_name} применил специальное умение «Защита {heal_s}»')
    return (f'{char_name} не применил специальное умение')


def start_training(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или special — '
          'чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd: str = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class: str = input(
            'Введи название персонажа, '
            'за которого хочешь играть: '
            'Воитель — warrior, Маг — mage, '
            'Лекарь — healer: '
        )
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. Черпает силы из '
                  'природы, веры и духов.')
        approve_choice: str = input(
            'Нажми (Y), чтобы подтвердить выбор, '
            'или любую другую кнопку, чтобы выбрать '
            'другого персонажа '
        ).lower()
    return char_class


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))


main()
