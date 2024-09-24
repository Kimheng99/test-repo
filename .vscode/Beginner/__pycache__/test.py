#def sum(n):
#    s = 0
    
#    for i in range(1, n+1):
#      s += i
#    return s
#n = int(input("Enter n: "))

#result = sum(n)
#print(f"1+2+3+ ... +{n} = {result}")

def sum(n):
    s = 0
    
    for i in range(2, n+1):
      i += 2
      s = i*2
    return s
n = int(input("Enter n: "))

result = sum(n)
print(f"2+4+6+ ... +{n} = {result}")



