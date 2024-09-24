# class human:
#     def __init__(self, name, id, score1, score2, score3):

#         self.name = name
#         self.id = id
#         self.score1 = score1
#         self.score2 = score2
#         self.score3 = score3
#     def output(self):
#         print("-------------------------")
#         print(f"name: {self.name}")
#         print(f"id: {self.id}")
#         print(f"score1: {self.score1}")
#         print(f"score2: {self.score2}")
#         print(f"score3: {self.score3}")
#         total = self.score1 + self.score2 + self.score3
#         averange = total/3
#         print("Totala: ",total)
#         print("Averange: ",averange)
#         print("-----------------")

# obj = human("Kimheng", "9707",99 ,98 ,97 )
# obj.output()


class animal:
    def __init__(self, name, place, color, eat):
        self.name = name
        self.place = place
        self.color = color 
        self.eat = eat
    def ouput(self):
        print("Name: ",self.name)
        print("Place: ",self.place)  
        print("Color: ",self.color)  
        print("Eat: ",self.eat)


class dog(animal):
    def soud(self):
        print("burs!!.....")

    
obj = dog("Jenei", "House", "White and Black", "Rice")

obj.ouput()
obj.soud()    

    
       
       
       

    