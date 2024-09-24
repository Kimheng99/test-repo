#import random
#option = ("rock", "paper", "scissor")

#running = True
#while running:
#    computer = random.choice(option)
#    player = None
#    while player not in option:
#        player = input("Please Enter (rock, paper, scissor): ")
#        print(f"You took : {player}")
#        print(f"Computer took: {computer}")
#        if player == computer:
#            print (" It's a tie!")
#        elif player == "rock" and computer == "scissor":
#            print (" You are win!")
#        elif player == "scissor" and computer =="paper":
#            print ("You are win!")
#        elif player == "rock" and computer == "paper":
#            print ("You are lose!")
#        else:
#            print("You are lose!")
#        player_run = input("Enter Y/N to Play agian: ").upper()
#        
#        if not player_run == "Y":
#            
#            running = False
        
#print("Thank for playing! ")


import random
option = ("rok", "scissor", "paper")
computer = random.choices(option)
running = True
while running:
    player = None
    print("Enter Rok, Paper, Scissor to play game!")
    while player not in option:
        player = input(":")
        print(f"You choese :{player}")









