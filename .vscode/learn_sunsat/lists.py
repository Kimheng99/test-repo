
# name = ["bannana", "orange", "apple"]
# name.(1,3)
# print(name)

#animal = ["dog", "cat", "pig"]
#food = ["hambuger", "pizza", "sandwid"]
#animal[1] = "tiger"
#animal.extend(food)
#animal.remove("pizza")
#animal.pop(3)
#for x in animal:
#    print(x, end=" ")

names = []
while True:
    option = int(input("Enter option: "))

    try:
        if option == 1:
            number = int(input("Number: "))
            count = 0
            while count < number:
                name = input("Enter name: ")
                names.append(name)
                count += 1

            
        elif option == 2:
            for x in names:

                print(x, end=" ")
            print()
        elif option == 3:
            dellet = input("name: ")
            names.remove(dellet)
        elif option == 4:
            num = int(input("Enter index of insert: "))
            name22 = input("name :")
            names.insert(num,name22)


        elif option == 5:
            break
            
    except ValueError:
        print("Value error!")
    except:
        print("Error!")
