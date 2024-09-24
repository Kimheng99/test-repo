import getpass
import matplotlib.pyplot
import numpy
import colorama 

username = str(input("Enter username: "))
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
                elif type == 'PIE':
                    names1 = []
                    
                    names1= names
                    values1 = numpy.array(values)
                    matplotlib.pyplot.pie(values1,labels=names1)
                    matplotlib.pyplot.show()
                elif type == 'PLOT':
                    names1 = []
                    
                    names1= names
                    values1 = numpy.array(values)
                    matplotlib.pyplot.plot(names1,values1)
                    matplotlib.pyplot.show()
            elif option == 4:
                delete = int(input("Enter index delet: "))
                names.pop(delete)
                values.pop(delete)

            elif option ==5:
                break

                    

                    

                

    else:
        print("Please try agian!")


login(username,password)



    
    