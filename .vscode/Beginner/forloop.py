#for x in reversed(range(1,11)):
#    print(x)

#print("Happy new year!")

#name = "heng"
#for x in name:
#    print(x)

#for x in range(1,21):
#    if x==13:
        
#        continue
#    else:
#        print(x)

#rows = int(input("Enter number of rows: "))
#columns = int(input("Enter number of columns: "))
#symbol = input("Enter your symbols: ")

#for x in range(rows):
  #  for y in range(columns):
  #      print(symbol, end="")
  #  print()
#import time
#secone = int(input("Enter s: "))
#for x in reversed(range(secone)):
#    print(x) 
#    time.sleep(1)
import time
seconds = int(input("Enter seconds of time: "))
for x in range(seconds,0, -1):
    seconds = x%60
    minit = int(x/60)%60
    hour = int(x/3600)%60
    day = int(x/3600/24)%24

    print(f"{day} day {hour:02}:{minit:02}:{seconds:02}")
    time.sleep(1)


