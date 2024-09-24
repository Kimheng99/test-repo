import random

fruit = ("apple", "banana", "orange", "coconut", "pineapple")

hangman = {0 :  ("   ", 
                 "   ",
                 "   "),
            1 : (" o ", 
                 "   ",
                 "   "),
            2 : (" 0 ", 
                 " | ",
                 "   "),
            3  :(" o", 
                 "/| ",
                 "   "),
            4 : (" o ", 
                 "/|\\",
                 "   "),
            5 : (" o ", 
                 "/|\\",
                 "/  "),
            6 : (" o ", 
                 "/|\\",
                 "/ \\"), 
            
               }
def display(wrong):
    print("********************")
    for lain in hangman[wrong]:
        print(lain)
    print("********************")
def news(new):
    print(" ".join(new))
def anwsers(anwser):
    print(" ".join(anwser))
def main():
    anwser = random.choice(fruit)
    new = ["_"] * len(anwser)
    wrong = 0
    guesses = set()
    running = True
    while running:
        display(wrong)
        news(new)
        guess  = input("Enter letter your guess: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Letter is not valid!")
            continue
        if guess in guesses:
            print(f"{guess} is already guessed!")
            continue
        guesses.add(guess)          


        if guess in anwser:
            for i in range(len(anwser)):
                if anwser[i] == guess:
                    new[i] = guess
        else:
            wrong += 1
        
        if "_" not in new:
            display(wrong)
            anwsers(anwser)
            print("You Win!")
            running = False
        elif wrong > len(hangman):
            display(wrong)
            anwsers(anwser)
            print("You Lose!")
            running = False

   


main()
