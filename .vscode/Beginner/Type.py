#age = 24
#money = 22.99
#name = "Cheata"
#LearnCode = True

#money = int(money)
#age = float(age)


#print(type(age))
#print(type(money))
#print(type(name))
#print(type(LearnCode))

#name = input("Enter  your name: ")
#active = input("Enter your act: ")
#freeTime = input("Enter your freetime: ")

#print(f" Usually {name} {active} at 5:00")
#print(f"When {name} free time, He usually go to {freeTime}!!")

#num1 = 344.3343
#num2 = -89.4433
#num3 = 932.289
#print(f"Output number1:  {num1:-}")
#print(f"Output number2: {num2:-}")
#print(f"Output number3: {num3:-}")
#name = input("Enter your name: ")
#while name == "":
#   print("You not enter your name!")    name = input("Enter your name: ")

#print(f"Welcome {name}")
#age = int(input("Please Enter Your Age: "))
#while age<0:
#    print("Age can't be not negative number! ")
#    age = int(input("Please Enter Your Age: "))
#print(f"You are {age} year old! ")

#press = input("Please Press Q or P:")
#while not press == "Q":
#    print("You want to continue game!")
#    break
#print("You wamt to Quit game!")
#a = int(input("Input a between 1 - 10: "))
#while a<0 or a>10 :
#    print("It's an invalid number!")
#    a = int(input("Input a between 1 - 10: "))
#print(f" Value of a: {a}")

principal = 0
rate = 0
time = 0

while principal<= 0:
    principal = float(input("Enter principal: $"))
    if principal <= 0:
        print("principal can't be less than or equal Zero!")
while rate<= 0:
    rate = float(input("Enter rate: "))
    if rate <= 0:
        print("rate can't be less than or equal Zero!")
while time<= 0:
    time = int(input("Enter time of year: "))
    if time <= 0:
        print("time of year can't be less than or equal Zero!")
total = principal *pow(1+ rate/100,time)

print(f"Balane after {time} year : {total:.2f}$ ")

