# word = "apple"
# letter = input("Guess letter in secret world: ")
# if letter in word:
#     print(f"{letter} is in word!")
# else:
#     print(f"{letter} was not found!")


# students = {"Dara", "Nita", "Mey"}
# student = input("Enter student!: ")
# if student in students:
#     print(f"{student} is a student!")
# else:
#     print(f"{student} was not found!")

email = input("Input email: ")
if "@" in email and "." in email:
    print("This email is valid!")
else:
    print("This email is invalid!")