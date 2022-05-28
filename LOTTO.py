# Jak zapewne wiesz, LOTTO to gra liczbowa polegająca na losowaniu 6 liczb z zakresu 1 – 49.
# Zadaniem gracza jest poprawne wytypowanie losowanych liczb. Nagradzane jest trafienie 3, 4, 5 lub 6 poprawnych liczb.
#
# Napisz program, który:
#
# zapyta o typowane liczby, przy okazji sprawdzi następujące warunki:
# czy wprowadzony ciąg znaków jest poprawną liczbą,
# czy użytkownik nie wpisał tej liczby już poprzednio,
# czy liczba należy do zakresu 1-49,
# po wprowadzeniu 6 liczb, posortuje je rosnąco i wyświetli na ekranie,
# wylosuje 6 liczb z zakresu i wyświetli je na ekranie,
# poinformuje gracza, ile liczb trafił.

import random

def player_nbrs():
    p_nbrs = []
    while True:
        n = input('podaj liczbę: ')
        try:
            int(n)
            if int(n) in list(range(1, 50)):
                if int(n) in p_nbrs:
                    print('tę liczbę juz mam')
                else:
                    p_nbrs.append(int(n))
                    if len(p_nbrs) == 6:
                        p_nbrs.sort()
                        return p_nbrs
            else:
                print('liczba poza zakresem 1-49')

        except ValueError as e:
            print('to nie jest liczba')


# print(player_nbrs())

def lotto():
    los = [x for x in range(1, 50)]
    random.shuffle(los)
    result = los[:6]
    result.sort()
    player = player_nbrs()
    hit_count = 0
    for i in result:
        if i in player:
            hit_count += 1
    return 'Wybrano: ', player, 'wylosowano: ', result, 'trafionych: ', hit_count

print(lotto())