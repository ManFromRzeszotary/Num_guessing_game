# import random
#
#
# def get_number():
#     """Get number from user.
#
#     Try until user give proper number.
#
#     :rtype: int
#     :return: given number as int
#     """
#     while True:
#         try:
#             result = int(input("Guess the number: "))
#             break
#         except ValueError:
#             print("It's not a number")
#
#     return result
#
#
# def guess_the_number():
#     """Main function with our game."""
#     secret_number = random.randint(1, 100)
#     given_number = get_number()
#     while given_number != secret_number:
#         if given_number < secret_number:
#             print("Too small!")
#         else:
#             print("Too big!")
#         given_number = get_number()
#     print("You Win!")
#
#
# if __name__ == '__main__':
#     guess_the_number()


# Napisz prostą grę w zgadywanie liczb. Komputer musi wylosować liczbę w zakresie 1 – 100. Następnie:
#
# Zadać pytanie: "Guess the number: " i pobrać liczbę z klawiatury.
# Sprawdzić, czy wprowadzony napis, to rzeczywiście liczba i w razie błędu wyświetlić komunikat "It's not a number!", po czym wrócić do pkt. 1
# Jeśli liczba podana przez użytkownika jest mniejsza niż wylosowana, wyświetlić komunikat "To small!", po czym wrócić do pkt. 1.
# Jeśli liczba podana przez użytkownika jest większa niż wylosowana, wyświetlić komunikat "To big!", po czym wrócić do pkt. 1.
# Jeśli liczba podana przez użytkownika jest równa wylosowanej, wyświetlić komunikat "You win!", po czym zakończyć działanie programu.

def guess_no():
    import random

    b = random.randint(1, 100)
    counter = 1
    while True:
        a = input('Guess the number: ')
        counter += 1
        try:
            int(a)
            if int(a) == b:
                print(f'You win!\nIt took {counter} attempts')
                return
            elif int(a) > b:
                print('Too big!')
            else:
                print('Too small!')
        except:
            print('''It's not a number!''')


guess_no()
