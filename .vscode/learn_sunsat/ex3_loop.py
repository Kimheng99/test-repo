#import random

#guesses = 0
#low = 1
#high = 100
#number = random.randint(low,high)
#running = True
#print("Enter number between 1 to 100: ")

#while running:
#    guess = input("Let Start:")
 #   if guess.isdigit():
 #       guess = int(guess)
 #       guesses += 1
 #       if guess < low or guess >high:
  #          print("This number is not in range!")
  #      elif guess < number:
  #          print("guess is too lower!")
  #      elif guess > number:
   #         print("guess is too higher!")
   #     else:
   #         print("Your guess is CORRECT!")
   #         print(f"You took {guesses} guess!")
   #         running = False
        
    #else:
    #    print("Please enter number 1 to 100!")
    #    print("This number is unvalidable")
#print("Thank for gussing!")
import random as heng
low = 1
high = 10
qut_guess = 0
running = True
num = heng.randint(low,high)
while running:
    guess = int(input("Enter number between 1 to 10: "))

    if guess < 1 or guess > 10:
        print("Please Enter agian!!")
    elif guess < num:
        print(f"{guess}is too low!")
    elif guess > num:
        print(f"{guess}is too hight!")
    else:

        print(f"Correct!")
        print(f"You took {qut_guess} guess.")
        running = False
    qut_guess += 1

    


