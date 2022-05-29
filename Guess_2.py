# Odwróćmy teraz sytuację z pierwszego zadania: ("Gra w zgadywanie liczb").
# Niech użytkownik pomyśli sobie liczbę z zakresu 1-1000, a komputer będzie zgadywał.
# Zrobi to maksymalnie w 10 ruchach (pod warunkiem, że gracz nie będzie oszukiwał).
# Zadaniem gracza będzie udzielanie odpowiedzi "To small", "To big", "You win".
# Do tego warsztatu dołączony jest schemat blokowy algorytmu. Zaimplementuj go w Pythonie.

def guess_2():
    print('Think of a number from a range 1-1000, and CPU will guess it in 10 attempts max')
    max = 1000
    min = 0
    guess_count = 1
    while True:
        guess = int((max-min)/2) + min
        print('CPU guess: ' + str(guess))
        ans = input('type:\nY for correct guess\nM for More than guessed\nL for Less than guessed\n>> ')
        if ans.upper() == 'Y':
            print(f'CPU won in {guess_count} tries!\nProtein component is so overestimated in today\'s world...')
            return
        elif ans.upper() == 'M':
            min = guess
            guess_count += 1
        elif ans.upper() == 'L':
            max = guess
            guess_count += 1
        else:
            print('please provide correct feedback')



if __name__ == '__main__':
    guess_2()