import getpass
import login_file

try:
    login_file.login()
except ValueError:
    print("Value error!")
except NameError:
    print("Name error!")
except:
    print("Error!")

