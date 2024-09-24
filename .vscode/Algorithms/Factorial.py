
# def fac(n):
#     fac1 = 1
#     for i in range(1, n+1):
#         fac1 *= i
#     return fac1
# print(fac(5))

# f(x) = ax2+bx +c
# import math
# a = int(input("Input a: "))
# b = int(input("Input b: "))
# c = int(input("Input c: "))

# def deta(a,b,c):
#     deta = b**2 - 4*a*c
#     return deta
# d = deta(a,b,c)
# if a == 0:
#     x = (-c)/b
#     print(x)
# elif d == 0:
#     x1 = x2 = (-b)/(2*a)
#     print(f"x1 = x2 = {x1}")
# elif d > 0:
#     x1 = ((-b)-math.sqrt(d))/(2*a)
#     x2 = ((-b)+math.sqrt(d))/(2*a)
#     print(f"x1= {x1}")
#     print(f"x2= {x2}")
# else:
#     print("F(x) haven't root!")

def change(a, b):
    
    temp = a
    a= b
    b = temp
    print(a,b)

change(1,2)



    