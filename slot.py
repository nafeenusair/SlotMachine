import random

def spin_row():
    spins = ['🍒', '🍉', '🍋', '🔔', '⭐']

    return [random.choice(spins) for x in range(3)]

def print_row(rows):
    print("|".join(rows))

def get_payout(rows, bets):
    if rows[0] == rows[1] == rows[2]:
        if rows[0] == '🍒':
            return bets * 3
        elif rows[0] == '🍉':
            return bets * 4
        elif rows[0] == '🍋':
            return bets * 5
        elif rows[0] == '🔔':
            return bets * 10
        elif rows[0] == '⭐':
            return bets * 20
    return 0

print("Welcome to Python Slot")
print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
balance = 100
print(f"Your current balance is : {balance}$")

while balance > 0:
    bet = input("Enter your betting amount: ")

    if not bet.isdigit():
        print("Invalid enter a valid number")
        continue
    bet = int(bet)

    if bet > balance:
        print("Insufficient Balance")
        continue

    if bet <= 0:
        print("Bet can't be zero or less")
        continue

    balance -= bet

    row = spin_row()
    print("Spinning")
    print_row(row)

    payout = get_payout(row, bet)

    if payout > 0:
        print("You won this round")
    else:
        print("You lost this round.")

    balance += payout
    print(f"Your current balance is: {balance}$")

    choice = input("Do you want to play again?(y/n): ")

    if choice.upper() == "N":
        print("Thanks for playing!")
        break

if balance == 0:
    print(f"You're out of balance")
