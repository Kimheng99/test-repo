
# numberss = [1,2,3,4,5,6,7,8]

# #even = [number for number in numberss if number%2==0]
# #odd = [number for number in numberss if number%2==1]
# num = [number for number in numberss if number>4]
# print(num)


def day_week(day):
    match day:
        case "Monday"| "Tuesday" | "Wednesday" | "Thursday" |"Friday":
            return False
        case "Sunday" |"Saturday":
            return True
        
        case _:
            return "It's not valid!"
print(day_week("Suy"))
        
    