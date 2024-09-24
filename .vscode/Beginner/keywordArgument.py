# def hello(geeting, title, first, last):
#     print(f"{geeting} {title} {first} {last}")

# hello("hello", "Mr", last = "kimheng", first= "nut")

#print('1', '2', '3',sep="-")
# def getphone(contry, area, firstname, lastname):
#     return print(f"{contry} {area} {firstname} {lastname}")

# phone = getphone("1",area="22",firstname="333", lastname="4444")


#def num(*args):
#    total = 0
#    for arg in args:
#        total += arg
#    return total
#print(num(1,2,3))

# def name(*args):
#     for arg in args:
#         print(arg, end=" ")


# name("Hello", "Mrr", "KIMHENGNUT")


# def num(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     print(total)

# num(1,2,3,4)


def address(*args,**kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    print(kwargs.get('name'))

    print(kwargs.get('id'))
    print(kwargs.get('gander'))
    


     #for key, value in kwargs.items():
      #   print(f"{key} : {value}")


address("cat", "dog", "tiger", 
        name="Kimheng",
         id= 239707,
         gander= 'M')


