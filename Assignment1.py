import random

def spin_row():
    symbols = ['🍇', '🍊', '🥝', '🔔', '💵']
    weights = [10, 10, 5, 1, 0.1] 
    return random.choices(symbols, weights=weights, k=3)

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍇':
            return bet * 2
        elif row[0] == '🍊':
            return bet * 5
        elif row[0] == '🥝':
            return bet * 7
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '💵':
            return bet * 20
    return 0

def main(): 

    print("****************************")
    print("     Welcome to Gambling")
    print("  Symbols: 🍇 🍊 🥝 🔔 💵")
    print("****************************")

    deposit = int(input("How much would you like to deposit? "))
    balance = deposit

    while balance > 0:
        print(f"Current balance: 💲{balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please input a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue
       
        if bet <= 0:
            print("Bet more than that")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won💲{payout}")
        else:
            print("Aww Dangit..")
        
        balance += payout

        if balance <= 0:
            print("You are now broke")
            break

        play_again = input(f"You have💲{balance} Do you want to spin again? (Y/N): ").upper()

        if play_again == 'Y':
            continue

        else:
            print("Thank you for playing!")
            break
            

if __name__ == '__main__':
    main()