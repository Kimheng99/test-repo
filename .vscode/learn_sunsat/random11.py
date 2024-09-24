#import time
#import random as heng


#while True:
#    num = heng.randint(1,10)
#    time.sleep(0.5)
#    print(num)
import math
n = int(input("Enter N: "))
def sum(n):
    s = (n*(n+2))//4
    return s
s = sum(n)
print(f"2+4+6+...+{n} :{s}")
