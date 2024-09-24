n = int(input("Enter yout number: "))
fact = 0
for i in range(1, n+1):
    if n%i == 0:
        fact+=1
if fact == 2:
    print(n, "is prime number")
else:
    print(n, "is not prime number")


    