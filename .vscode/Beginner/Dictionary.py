#capital = {"Cambodia" : "Phnom penh ",
#               "Lao" : "Vieng chan" ,
#               "Vietnam": "Ha noi", 
 #              "Thai": "Bankok"}
#item = capital.items()
#print(item)
#for keyeee, value in capital.items():
#    print(f"{keyeee} has 1 city is :  {value}")

# menu = {"Pizza" : 10.00,
#         "Hambuger" : 5.99,
#         "Sandwid" : 3.99,
#         "Capuchuno" : 2.99,
#         "CocaCola" : 1.50,}

# card = []
# total = 0

# print("----------Menu----------")
# for key, value in menu.items():
#     print(f"{key:20} : ${value:.2f}")

# while True:
#     pick = input("Pick your item: ")
#     if pick == "q":
#         break
#     elif menu.get(pick) is not None:
#         card.append(pick)
# for pick in card:
#     total += menu.get(pick)
#     print(pick ,end=" ")
# print()

# print(f"Total of your food is: {total:.2f}")

lists = {"PP": "cambodia",
         "VC": "lao",
         "HN": "vietname"}
for key, value in lists.items():
    print(f"{key} : {value}")