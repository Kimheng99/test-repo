
#prices = []
#total2 = []
#codes = []
#names = []
#quatitys = 0
#total = 0
#while True:
    #name = input("Name: ")
    #if name == "q" :
    #    break
    #else:
        
     #   code = int(input("Code: "))
     #   price = float(input("Price: $"))
    #    quatity = int(input("Quatity: "))
    #    names.append(name)
     #   codes.append(code)
     #   prices.append(price)
     #   total1 = price*quatity
      #  total2.append(total1)
#print("-----Result------")
#for name in names:
#    print(name , end=" ")
#print()
#for code in codes:
#    print(code, end="   ")
#print()
#for price in prices:
 #   print(price, end="$   ")

#print()
#for total1 in total2:
 #   total += total1
 #   total1= round(total1,2)
 #   print("$",total1, end="   ")
#print("")
#print(f"Your total of payment: ${total:.2f}")

names = []
codes = []
total_prices = []
qutitys = []
total= 0
prices = []

while True:
    name = input("Enter Name: ")
    if name =="q":
        break
    else:
        code = input("Enter Code: ")
        price = float(input("Enter price:$"))
        qutity = int(input("Enter Qutity: "))
        names.append(name)
        codes.append(code)
        prices.append(price)
        qutitys.append(qutity)
        total_price = price * qutity
        total_prices.append(total_price)
for x in names:
    print(x, end=" ")
print()
for y in codes:
    print("code: ",y, end=" ")
print()
for z in prices:
    print("$",z, end=" ")
print()
for i in qutitys:
    print("quty:",i, end=" ")
print()
for k in total_prices:
    k = round(k,2)
    print("$",k, end=" ")
print()
for total_price in total_prices:
    total += total_price
print(f"Total of all product is: {total:.2f}") 










        
    
    

