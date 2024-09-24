import random
def spin():
    symbols = ['🍉', '🍋', '🍎', '⭐', '🟠']
    return [ random.choice(symbols) for  _ in range(3)]

def print_row(row):
    print(" | ".join(row))
def payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍉':
            return bet * 3
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🍎':
            return bet * 7
        elif row[0] == '⭐':
            return bet * 10
        elif row[0] == '🟠':
            return bet * 20
    else:
        return 0
    

def main():
    print("-----***Python Slot Machine***-----")
    print("Symbol: 🍉 🍋 🍎 ⭐ 🟠")
    print("*****Happy for Spring*****")
    balane = float(input("Enter your balance: $"))
    print(f"Blance: ${balane}")
    
    while balane> 0:
        
        bet = input("Enter bet: ")
        if not bet.isdigit():
            print("Please Enter amount!!")
            continue
        bet = int(bet)
        if bet > balane:
            print("Your balane is not anouth")
            continue
        if bet <= 0 :
            print("Bet must be great than 0!")
            continue
        
       
        balane -= bet
        
        row = spin()
        print("************")
        print_row(row)
        print("************")

        pay = payout(row,bet)
        if pay > 0:
            print(f"You won : ${pay}")
        else:
            print("Sorry you are lose!")

        balane += pay
        print("Balance: $",balane)
        play = input("You want to continue game(Y/N): ").upper()
        if not play == "Y":
            break

        
        print("Spring!.....")
    print(f"Game Over! Your final balance : ${balane}")
   


main()
        


        




