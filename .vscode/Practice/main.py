import randoms

try:
    randoms.login()
except ValueError:
    print("Value Error!")
except NameError:
    print("Name Error!")
except:
    print("Error!!")
