score1 = float(input("Enter Score 1: "))
score2 = float(input("Enter Score 2: "))
score3 = float(input("Enter Score 3: "))
score4 = float(input("Enter Score 4: "))
score5 = float(input("Enter Score 5: "))

total = score1 + score2 + score3 + score4 + score5
averange = total/5

print("_______________---Output---_________________")
print(f"Score1: {score1:.2f}")
print(f"Score2: {score2:.2f}")
print(f"Score3: {score3:.2f}")
print(f"Score4: {score4:.2f}")
print(f"Score5: {score5:.2f}")
print(f"Total Scorce is: {total:.2f}")
if averange >= 90:
    print(f"{averange:.2f} is Grade : A")
elif averange >=80 and averange <90:
    print(f"{averange:.2f} is Grade : B")
elif averange >=70 and averange <80:
    print(f"{averange:.2f} is Grade : C")
elif averange >=60 and averange <70:
    print(f"{averange:.2f} is Grade : D")
elif averange >=50 and averange <60:
    print(f"{averange:.2f} is Grade : E")
else:
    print(f"{averange:.2f} is Grade : F")

