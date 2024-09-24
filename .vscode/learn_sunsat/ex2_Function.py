#def change(n):
#    C = (n - 32)*5/9
#    return C
#n = int(input("Enter n:"))
#result = change(n) 

#print(f" {n}F  =  {result:.2f}C")


#A = []
#B = []
#a=0
#b=0
#def vote(n):


 #   n = input("Enter vode: ")
 #   if n == "a":
  #      a +=1
  #  else:
  #      b +=1

def voting_system():
    votes = {'A': 0, 'B': 0}

    while True:
        vote = input("Vote for A or B (press Q to quit):").strip().upper()

        if vote == 'Q':
            break
        elif vote == 'A':
            votes['A'] += 1
        elif vote == 'B':
            votes['B'] += 1
        else:
            print("Invalid input. Please vote for A or B.")

    print("\nVoting Summary:")
    print(f"Votes for A: {votes['A']}")
    print(f"Votes for B: {votes['B']}")
    print("Thank you for voting!")

voting_system()


