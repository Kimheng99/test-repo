sentence = input("Enter the sentence: ")
string = sentence.lower()
print(string)
count = 0
list = ['a','e','i','o','u']
for i in string:
    if i in list:
        count+= 1
print("Number of vovel in sentence :", count)