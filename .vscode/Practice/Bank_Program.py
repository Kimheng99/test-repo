def balance_bank(balance):
    print(f"Your balance: ${balance:.2f}")
def deposit():
    amount = float(input("Input your amount for deposit: "))
    return amount
def withdraw():
    amount = float(input("Input your amount for deposit: "))
    return amount




def main():
    balance = 0
    running = True
    while running:
       print("------***Bank Account***--------")
       print("1. Balance: ")
       print("2. Deposit: ")
       print("3. Withdraw: ")
       print("4. Exit: ")
       print("***************************")
       choice = input("Enter Choices (1-4): ")
       if choice == "1":
           balance_bank(balance)
       elif choice == "2":
            balance += deposit()
       elif choice == "3":
            balance -= withdraw()
       elif choice == "4":
            running = False
       else:
        print("This is unvalid! ")

    print("Thank for playing!")


main()



