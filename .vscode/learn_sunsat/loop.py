number = int(input("Enter your number: "))
factorail = 1


for x in range(1 , number+1):
    factorail*=x
print(f"Factorai {number} is: {factorail}")