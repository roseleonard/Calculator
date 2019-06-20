# print("Hello calculator")

# #Add 2 numbers
# number1 = input("Give me a number.")
# number2 = input("What's the second number?")

# def addition(number1,number2):
#     step1 = int(number1) + int(number2)
#     return step1

# def mulitplication(number1,number2):
#     step1 = int(number1) * int(number2)
#     return step1
    
# def division(number1,number2):
#     step1 = int(number1) / int(number2)
#     return step1
    
# def subtraction(number1,number2):
#     step1 = int(number1) - int(number2)
#     return step1
    

# #2 function calculator



# function = input("""
# What operation would you like to perform?
# a = addition
# b = multiplication
# c = division
# d = subtraction"""
# )


# if function == "a":
#     print(addition(number1,number2))
# elif function == "b":
#     print(mulitplication(number1,number2))
# elif function == "c":
#     print(division(number1,number2))
# elif function == "c":
#     print(subtraction(number1,number2))
# else:
#     print("Please enter a,b,c,or d")



birth_month = input("What is your birth month? (mm)")

birth_date = input("What is your birthday? (dd)")


if int(birth_month + birth_date) >= 120 and int(birth_month + birth_date) <= 218:
    print("You are an Aquarius!")
elif int(birth_month + birth_date) >= 219 and int(birth_month + birth_date) <= 320:
    print("You are a Pisces!")
elif int(birth_month + birth_date) >= 321 and int(birth_month + birth_date) <= 419:
    print("You are an Aries!")
elif int(birth_month + birth_date) >= 420 and int(birth_month + birth_date) <= 520:
    print("You are a Taurus!")
elif int(birth_month + birth_date) >= 521 and int(birth_month + birth_date) <= 620:
    print("You are a Gemini!")
elif int(birth_month + birth_date) >= 621 and int(birth_month + birth_date) <= 722:
    print("You are a Cancer!")
elif int(birth_month + birth_date) >= 723 and int(birth_month + birth_date) <= 822:
    print("You are a Leo!")
elif int(birth_month + birth_date) >= 823 and int(birth_month + birth_date) <= 922:
    print("You are a Virgo!")
elif int(birth_month + birth_date) >= 923 and int(birth_month + birth_date) <= 1022:
    print("You are a Libra!")
elif int(birth_month + birth_date) >= 1023 and int(birth_month + birth_date) <= 1121:
    print("You are a Scorpio!")
elif int(birth_month + birth_date) >= 1122 and int(birth_month + birth_date) <= 1221:
    print("You are a Sagittarius!")
elif int(birth_month + birth_date) >= 119 or int(birth_month + birth_date) <= 1222:
    print("You are a Capricorn!")








































