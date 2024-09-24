#a = int(input("A = : "))
#b = int(input("B = : "))
#c = int(input("C = : "))
#d = int(input("D = : "))

#def avr(a,b,c,d):
#    return (a+b+c+d)/4
#averange = avr(a,b,c,d)
#print(f"Averanger : {averange}")
#if averange > 50:
#    print("pass!")
#else:
#    print("Fale!")


def play():
    s = "Hello"
    def play2():
        nonlocal s
        s = "Heng"
    play2()
    print(s)

play()
