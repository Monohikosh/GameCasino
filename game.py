import random

balance = 20
check_balance = balance

print('Welcome to the casino')
start = input('Shall we start? (y/n) ')
while start != 'y' and start != 'Y' and start != 'yes' and start != 'Yes' and start != 'YES' and start != 'n'\
        and start != 'N' and start != 'no' and start != 'No' and start != 'NO':
    print('Error! Try again')
    start = input('Shall we start? (y/n) ')

while start == 'y' or start == 'Y' or start == 'yes' or start == 'Yes' or start == 'YES':
    print('Your balance: ', balance, ' $')
    color = input('What color is it? ')
    while color != 'green' and color != 'Green' and color != 'GREEN' and color != 'red' and color != 'Red'\
            and color != 'RED' and color != 'black' and color != 'Black' and color != 'BLACK':
        print('Error! Enter the green, red or black')
        color = input('What color is it? ')
    if color != 'green' and color != 'Green' and color != 'GREEN':
        number = int(input('What is the number? '))
        while number < 1 or number > 50:
            print('Error! Minimum number: 1; Maximum number: 50')
            number = int(input('What is the number? '))
    else:
        number = 0
    bet = int(input('Place a bet: '))
    while bet < 0 or bet > balance:
        print('Error! Minimum bet: 0 $; Maximum bet: ', balance, ' $')
        bet = int(input('Place a bet: '))
    balance -= bet
    print('Your bet: ', color, number, ',', bet, '$')
    color_robot = random.randint(1, 102)
    number_robot = random.randint(1, 51)
    if color_robot == 101:
        print('Dropped out: green ' + '0')
        if color == 'green' or color == 'Green' or color == 'GREEN':
            print('Congratulations! Your bet has won')
            print('Your balance: ', balance + bet * 50)
            balance = balance + bet * 50
    elif color_robot % 2 == 0:
        print('Dropped out: red', number_robot)
        if (color == 'red' or color == 'Red' or color == 'RED') and number == number_robot:
            print('Congratulations! Your bet has won')
            print('Your balance: ', balance + bet * 20)
            balance = balance + bet * 20
        if color == 'red' or color == 'Red' or color == 'RED':
            print('Congratulations! Your bet has won')
            print('Your balance: ', balance + bet * 2)
            balance = balance + bet * 2
    elif color_robot % 2 != 0 and color_robot != 101:
        print('Dropped out: black', number_robot)
        if (color == 'black' or color == 'Black' or color == 'BLACK') and number == number_robot:
            print('Congratulations! Your bet has won')
            print('Your balance: ', balance + bet * 20)
            balance = balance + bet * 20
        if color == 'black' or color == 'Black' or color == 'BLACK':
            print('Congratulations! Your bet has won')
            print('Your balance: ', balance + bet * 2)
            balance = balance + bet * 2
    if balance < check_balance:
        print('Oh! You have lost')
        print('Your balance: ', balance)
    check_balance = balance
    if balance == 0:
        print('Game over!')
        break
    start = input('Сontinue? (y/n) ')
    while start != 'Y' and start != 'y' and start != 'yes' and start != 'Yes' and start != 'YES' and start != 'n'\
            and start != 'N' and start != 'no' and start != 'No' and start != 'NO':
        print('Error! Try again')
        start = input('Сontinue? (y/n) ')
exit_1 = input('Press any button to exit ')
if exit_1 == '':
    print('Goodbye!')