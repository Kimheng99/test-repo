# import random
# low =1
# high = 100
# guesses = 0
# numbers = random.randint(low,high)
# print("********Python Game*********")
# print("=>Enter number between (1 to 100)")
# while True:
#     guess = input(": ")
#     if guess.isdigit():
#         guess = int(guess)
#         if guess < 0 or guess >100:
#             print("Agian!!")
#             continue
#         elif guess > numbers:
#             print(f"{guess} is too higher!")
#         elif guess < numbers:
#             print(f"{guess} is too lower!")
#         else:
#             print(f"Correct number!!")
            
#             print(f"you took {guesses} guess!")
#             break
#         guesses += 1
#     else:
#         print("Your number is unvalid!")
#         print("Please Ener your number agian!")
# print("Thank for playing!")


import getpass
import matplotlib.pyplot

username = input("Enter your user name: ")
password = getpass.getpass("Ener Password: ")
def login(username, password): 
    if username == "Kimheng" and password == "Kimheng9":
        print("login sucess!!")
        count = 0
        names = []
        values = []
        while True:
            option = int(input("Input Option: "))
            if option == 1:
                number = int(input("Enter number: "))
                while count < number:
                    name = input("Name: ")
                    value = int(input("Value: "))
                    names.append(name)
                    values.append(value)
                    count +=1
            elif option == 2:
                for name in names:
                    print(name, end=" ")
                print()
                for value in values:
                    print(value, end=" ")
                print()
            elif option == 3:
                types = input("Enter Type of matplot: ").upper()
                if types == "BAR":
                    matplotlib.pyplot.bar(names,values)
                    matplotlib.pyplot.show()
                elif types == "PIE":
                    matplotlib.pyplot.pie(values,labels=names)
                    matplotlib.pyplot.show()
                elif types == "PLOT":
                    matplotlib.pyplot.plot(names,values)
                    matplotlib.pyplot.show()
            elif option == 4:
                index = int(input("Enter Index to delet: "))
                names.pop(index)
                values.pop(index)
            elif option == 5:
                break




    else:
        print("Unsucess!")


    print("Thank you!")

