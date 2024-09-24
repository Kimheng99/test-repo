#meat = ["pig","cow","chicken"]
#fruit = ["apple", "orange", "bannana"]
#food = ["pizza", "hamburger", "sandwid"]

#all = [("pig","cow","chicken")
 #      , ("apple", "orange", "bannana"),
  #       ("pizza", "hamburger", "sandwid")]

#for x in all :
 #   for y in x :
  #      print(y, end=(" "))
   # print()

#bottom_call = [(1,2,3)
#               ,(4,5,6)
#               ,(7,8,9)
#               ,("*",0,"#")] 
#for row in bottom_call:
#    for column in row:
#        print(column,end=" ")
#    print()
#questions = ("How many students in this class?",
 #           "How many team did tuyet trinh ?",
  #          "How many Lao students in this class?",
   #         "How many CPC students in this class?",
    #        "How many Teacher in this class?")

#options = [("A.50", "B.52", "C.60", "D.80"),
 #         ("A.1", "B.2", "C.3", "D.4"),
  #        ("A.5", "B.2", "C.3", "D.7"),
   #       ("A.6", "B.2", "C.3", "D.4"),
    #      ("A.1", "B.2", "C.6", "D.4")]    
#anwsers = ("D", "B", "B", "C", "A")
#guests =[]
#scores = 0
#question_num = 0

#for question in questions:
#    print("------------------")
#    print(question)
#    for option in options[question_num]:
#        print(option)
    
 #   guest = input("Enter A, B, C, D: ").upper()
 #   guests.append(guest)
 #   if guest == anwsers[question_num]:
 #       print("Correct!!!")
 #       scores +=1
 #   else:
 #       print("Uncorrect!")
 #       print(f"The awnser is: {anwsers[question_num]} ")
  #  question_num += 1
#print("---------------")
#print("----Resuld-----")
#print("---------------")
#for anwser in anwsers:
 #   print(anwser, end=(""))
#for guest in guests:
 #   print(guest, end=(""))

#total = (scores/len(questions))*100
#print(f"Your scores is: {total}%")



questions = ("What are you doing?",
            "What is jerry doing?",
            "Are you sitting in the class?",
            "What are you studying?",
            "What time is it?")
options = [("A.sleep", "B.learning code", "C.writing", "D.focus study"),
           ("A.sleep", "B.play phone", "C.writting", "D.focus study"),
           ("A.sleep", "B.learning code", "C.yes", "D.no"),
           ("A.tam ly hoc", "B.tu suy cong nghe", "C. A and B", "D.ky nang mem"),
           ("A.11:10", "B.12:00", "C.13:00", "D.1:00")]

anwsers = ("B","B","C","B","A")
guests = []

score = 0

ques_num = 0

for question in questions:
    print("---------")
    print(question)
    for optiion in options[ques_num]:
        print(optiion)
    guest = input("Enter your anwser: ")
    if guest == anwsers[ques_num]:
        print("Correct!!")
        score += 1
    else:
        print("Uncorrect!")
        print(f"The Awnser is :{anwsers[ques_num]}")

    ques_num += 1

    for guest in guests:
        print(guest, end=(""))
    print()
for anwser in anwsers:
    print(anwser, end=(" "))
print()

total = (score/len(questions))*100
print(f"Your Score is: {total}%")









    