#operator = input("Enter Operator('+, -, *, / '): ")
#num1 = float(input("Enter Number 1: "))
#num2 = float(input("Enter Number 2: "))

#if operator == "+":
#   result = num1 + num2
    #print(round(result,2))
#elif operator == "-":
#    result = num1 - num2
    #print(round(result,2))
#elif operator == "*":
#    result = num1 * num2
    #print(round(result,2))
#elif operator == "/":
#    result = num1 + num2
 #   print(round(result,2))
#else:
 #   print("It's not valid in operator!")

#weight = float(input("Enter your weight: "))
#unit = input("Enter your unit want to convertor: (K or L): ")

#if unit == "K":
#    weight *= 2.205
#    unit = "Lbs"
#elif unit =="L":
 #   weight /= 2.205
#    unit = "Kgs"
#else:
 #   print(f"{weight} was not valid!")


#print(f"Your convertor is : {round(weight,2)} {unit}")

#temp = float(input("Input the temperture: "))
#unit = input("Input unit of Temperture ( C or F) : ")

#if unit == "C":
#   temp = (temp * 9)/5 + 32
#   unit = "F"
 #   print(f" Temperture in F: {temp} {unit} ")
#elif unit == "F":
 #   temp = (temp -32)*9/5
 #   unit = "C"
  #  print(f"Temperture in C is: {temp}{unit}")
#else:
 #   print(f"{unit} is an invalid!")


#sunny = True
#if not sunny:
#    print("It's cloude outside!")
#else:
#    print("It's sunny outside!")

#num = 5
#a= 2
#b= 5
#age = 10

#print("Positive" if num > 0 else "Nagetive")
#print("Even" if num%2 == 0 else "Odd")
#max_num = a if a>b else b
#min_num = a if a<b else b

#print(max_num)
#print(min_num)
#print("Adult" if age>=18 else "Child")

#name = input("Enter name: ")

#print(name.find("-"))

#validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

#name = input("Enter your user name: ")
#if len(name)>12:
#    print("This user name can't process!")
#elif not name.find(" ") == -1:
#    print("This user name can't process!")
#elif  not name.isalpha():
#    print("No no no!!!")
#lse:
#    print(f"Your name: {name}")

#name = "1234-567-89"
#idix = name[-2:]
#print(f"XXXX-XX-{idix}")


import getpass
import matplotlib.pyplot
import numpy
import colorama 

username = input("Enter username: ")
password = getpass.getpass("Input password: ")
def login(username, password):
    names = []
    values = []
    count = 0
    
    
    if username == "admin" and password == "kimheng":
        print("Login succes!")

        
        while True:
            option = int(input("Enter Number of option: "))
            if option == 1:
                number = int(input("Enter Number: "))
                

                while count<number:
                    
                    name = input("Enter name of product: ")
                    value = int(input("Enter value: "))
                    names.append(name)
                    values.append(value)
                    count +=1
            elif option == 2:
                for name in names:
                    print(name,end=" ")
                print()
                for value in values:
                    print(value,end=" ")
                print()
            elif option == 3:
                types = str(input("Enter Type of matplot: ")).upper()
                if types == 'BAR':
                    names1 = []
                    
                    names1= names
                    values1 = numpy.array(values)
                    matplotlib.pyplot.bar(names1,values1)
                    matplotlib.pyplot.show()
                elif type == 'TIE':
                    names1 = []
                    
                    names1= names
                    values1 = numpy.array(values)
                    matplotlib.pyplot.tie(values1,lambda=names1)
                    matplotlib.pyplot.show()

                    

                    

                

    else:
        print("Please try agian!")

login(username,password)















