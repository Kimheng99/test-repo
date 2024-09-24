#foods = []
#prices = []
#total = 0

#while True:
#    food = input("Enter food you nees(Press q or Qiut): ")
    
 #   if food == "q":
  #      break
  #  else:
        

   #     price = float(input(f"Enter price of {food}: $$  "))
    #    prices.append(price)
     #   foods.append(food)


#print("Your Shoppiing Cart")

#for food in foods:
 
 #   print(food, end=" ")
#for price in prices:
 #   total +=price
#print()
#print(f"Your total is : ${total}")


#foods = []
#prices = []
#total = 0

#while True:
#    food = input("Enter the food you need: ")
#    if food =="q":
#        break
#    else:
#        price = float(input(f"Enter price of {food}: $"))
#        foods.append(food)
#        prices.append(price)
#
#print("___Shopping Card____")
#for food in foods:
#    print(food,end=(" "))
#for price in prices:
#    total += price
#print()
#print(f"Total of food is: ${total:.2}")







#foods = []
#prices = []
#total = 0

#while True:
#    food = input("Enter your food: ")
#    if food == "q":
#        break
#    else:
#        foods.append(food)
#        price = float(input(f"Enter price of {food}: $"))
#        prices.append(price)

#print("------------Shopping Card----------")
#for food in foods:
#    print(food,end=" ")
#print()
#for price in prices:
#    total += price
#print(f"Total of your payment: ${total:.2f}") 
    
        
foods = []
prices = []
total = 0

while True:
    food = input("Enter Food: ").lower()
    if food == "q":
        break
    else:
        foods.append(food)
        price = float(input(f"Enter price of {food}: $"))
        prices.append(price)
print("-------------Shopping Card-----------")
for food in foods:
    print(food, end=" ")
print()
for price in prices:

    total += price
print(f"Total of your payment: ${total}")





