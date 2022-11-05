# Условия игры: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.

import random

name = input('Введи имя любого игрока: ')     # жеребьёвка
num = random.randint(1,2)
print(f'Игрок {name} является Игроком {num}, т.е. ходит {num}-ым')

sum = 117
max = 28
min = 1
player = 1
print(f'На столе лежит {sum} конфет. Сколько конфет ты заберёшь?')

while True:
    take = int(input(f'Игрок {player}: '))
    if take<min or take>max:
        print('Введено неверное число.')
    else:
        sum = sum-take
        print(f'Осталось конфет: {sum}')
        if sum == 0:
            print(f'Победил Игрок {player}!')
            exit()
        if player == 1: player = 2
        else: player = 1