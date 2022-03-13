from random import randint
cont = 0
while True:
    print(f"\033[40m{' EVEN or ODD - The Python Game ':~^50}\033[m")
    comp = randint(0, 10)
    user = int(input('Type a number: '))
    s = comp + user
    choice = str(input('Will you chose EVEN or ODD [E/O]? ')).strip().upper()[0]
    while choice not in 'EO':
        choice = str(input('Will you chose EVEN or ODD [E/O]? ')).strip().upper()[0]
    print(f'\033[33mThe computer chose {comp} and you {user}.', end=' ')
    print(f'Result: {s} (Even)\033[m' if s % 2 == 0 else f'Result: {s} (Odd)\033[m')
    if s % 2 == 0 and choice == 'E':
        cont += 1
        print("\033[34mCongratulations, you win! Let's play again.\033[m")
    elif s % 2 != 0 and choice == 'O':
        cont += 1
        print("\033[34mCongratulations, you win! Let's play again.\033[m")
    else:
        print('\033[31mYou lose. More luck in the next time.\033m')
        break
    print()
print(f'\n\033[40mGAME OVER! You won {cont} times this turn.\033[m')
