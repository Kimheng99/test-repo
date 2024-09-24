#import math
#n = int(input("Enter N: "))
#def sum(n):
#    s = ((n-1)*(n+3))//4
#    return s
#s = sum(n)
#print(s)
import math

def sum_cos(num):
    sum_of_cos = 0

#  
 
    for i in range(1, num + 1):
        sum_of_cos += math.cos(math.radians(i))  # Convert degrees to radians
    
    return sum_of_cos

# Input: Last angle in the series (N)
num = int(input("Enter the last angle in degrees (N): "))

# Calculate and display the sum
restul = sum_cos(num)

print(f"The sum of the series Cos(1°) + Cos(2°) + Cos(3°) + ... + Cos({num}°) is: {restul}")

        


#import math



#def sum_cos(num):
   
#    total = 0
#    for i in range(1, num+1):
#        total += math.cos(math.radians(i))
#    return total
#num = int(input("Enter number: "))
#result = sum_cos(num)
#print(result)

#import math
#n = int(input("Enter number: "))
#def sum(n):
#    s = (n*(n+2))//4
#    return s
#sum1 = sum(n)
#print(f"2+4+...+{n}={sum1}")

#import math
#n = int(input("Enter number: "))
#def sum(n):
 #   s = ((n-1)*(n+3))//4
 #   return s
#sum1 = sum(n)
#print(f"3+5+...+{n}={sum1}")








    









