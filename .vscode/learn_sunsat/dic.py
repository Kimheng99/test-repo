# lists = {"name" :74}
# key = input("key: ")
# value = input("value: ")
# lists.update({f"{key}" : f"{value}"})
# for key, value in lists.items():
#     print(key,value)




# dic = {"animal": {"dog": 2,"cat": 3},
#        "food": { "Pizza": 3, " Hambuger" : 4}}
# print(f"{dic["animal"]["food"]}")


# dis = {"101" : "lita",
#        "102" : " kanha",
#        "103" : "sophea"}
# dis.pop("101")
# print(dis)

def op():
    dictionary = { 

    }
    while True:
        option = input("Enter Option: ")
        if option == "1":
            num = int(input("Number: "))
            count  = 0
            while count < num:
                food = input("Food: ")
                price = float(input(f"Price of {food}: $"))
                dictionary.update({f"{food}":f"{price}"})
                count += 1
        elif option == "2":
            print(dictionary)
        elif option == "3":
            foods = input("food for delete: ")
            if foods in dictionary:
                dictionary.pop(foods)
            else:
                print("Food is not found!")
        elif option == "4":
            search = input("Search: ")
            if search in dictionary:
                print(dictionary[search])
            else:
                print("Search is not found!")
        else:
            break

            

print("---****Chooes option****---")
print("1. Update")
print("2. Print")
print("3. Delete")
print("4. Search")
print("******---------------*******")



op()

