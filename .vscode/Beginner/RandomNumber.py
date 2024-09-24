#import random
#low = 1
#high = 6
#guests = 0

#number = random.randint(low,high)

#while True:
#    guest = int(input("Enter your number your guest: "))
 #   guests+=1
  #  if guest < number:
  #      print(f"{guest} is too low")
  #  elif guest > number:
  #      print(f"{guest} is too hight")
   # else:
    #    print("The number is correct!")
     #   break

#print(f"You took {guests} guest")

#import random

#low = 1
#high = 100
#guesses = 0
#num = random.randint(low,high)
#num_running = True

#print("Python guessing game")
#print("Enter number between 1 to 100!")

#while num_running:
#    guess = input(": ")
#    if guess.isdigit():
 #       guess = int(guess)
  #      guesses += 1
   #     if guess< low or guess > high:
   #         print("This number is not in range!")
   #         print("Enter number between 1 to 100! ")
   #     elif guess < num:
   #         print("guess is too lower!")
   #     elif guess > num:
   #         print("guess is too higher!")
   #     else:
   #         print("Correct anwser!!")
   #         print(f"Your took : {guesses} guesse")
   # else:
   #     print("Unvalid Number!")
   #     print("Enter number between 1 to 100!")
   #     num_running = False
import random
low = 1
high = 100
guesses = 0
number = random.randint(low,high)
running_number = True

print("----------Python Game------------")
print("=>Enter number between 1 to 100<=")
while running_number:
    guess = input(":")
    if guess.isdigit():
        guess = int(guess)
        
        if guess < low or guess >high:
            print("ERROR! Please Agian!")
        elif guess > number:
            print(f"{guess} is too higher.")
        elif guess < number:
            print(f"{guess} is too lower.")
        else:
            print("Correct number!")
            running_number = False
            print(f"You took {guesses} gussing!")
        guesses += 1
    else:
        print("Your number is unvolid!")
        print("Please Enter Number Agian!")


print("Thank you for playing.")






