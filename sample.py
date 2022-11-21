# asking for fav color and name
# name = input("What is your name: ")
# color = input("What is fav color: ")
# print("Hi "+name+" your fav color is "+color)
# output:Hi Harsh your fav color is blue


# This is converting lbs to KG
# weight_lbs =  int(input("Enter the weight in 'lbs': "))
# weight_kg = weight_lbs * 0.453592
# print(weight_kg)
# output:1 lbs = 0.453592


# muilt line string
# hello = '''
# this cat drink milk!
# and eat fish too.
# '''
# print(hello)
# output:
# this cat drink milk!
# and eat fish too.


# get the char from index
# hello = "hello world"
# print(hello[3:-1])
# output:lo worl


# formmated string to insert values dynamically
# name = "harsh"
# msg = f'the {name} is a coder'
# print(msg)
# output:the harsh is coder


# get legnth of the string 
# test = "This is test"
# print(len(test))
# output:12


# string convert Titel/Upper/lower case
# test="welcome to Hello World"
# print(test)
# print(test.upper())
# print(test.lower())
# print(test.title())
# output:
#         welcome to Hello World
#         WELCOME TO HELLO WORLD
#         welcome to hello world
#         Welcome To Hello World


# find the index of char
# test = "sample"
# print(test.find("a"))
# output: 1


# replace method to replace the world
# test = "this is sample text"
# print(test.replace("sample","demo"))
# output:this is demo text


# "IN" function to checking word in the Variable or not
# test = "this is sample text"
# print("sample" in test)
# output: True

# price = 1000000
# test = False
# if test:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"down payment: {down_payment} $")



# name = input("enter your name: ")
# name_len = len(name)
# if name_len <= 3:
#     print("Name Should be More then 3 Char")
# elif name_len >=50:
#     print("Name Should be Less then 50 Char")
# else:
#     print(f"Welcome {name}!")

# weight to KG or LBS
# weight = int(input("Enter the Weight: "))
# weight_lbs_kg = input("(L)Lbs or (K)Kg: ")
# if weight_lbs_kg.upper() == "L":
#     print("Lbs=",weight*2.20462)
# elif weight_lbs_kg.upper() == "K":
#     print("Kg=",weight*0.453592)
# else:
#     print("invaild input")



# while loop

# i=1
# while i<=10:
#     print(i)
#     i+=1
# print("done")

# i=1
# while i<=10:
#     print("*" * i)
#     i+=1

# print("done")

#while else. The else part work when loop didnt stop with break function 
# guess_count=0
# guess_limit=9
# while guess_count < 3:
#     guess = int(input("Guess:"))
#     guess_count+=1
#     if guess == guess_limit:
#         print("Your Guess is correct!")
#         break
# else:
#     print("You lost ")


while True:
    help_command = input(">")
    if help_command.lower() == "help":
        print("""
        Start - Start The Car
        Stop  - Stop  The Car
        Quit  - to Exit
        """)
    elif help_command.lower() == "start":
            print("Car Has Been Started......")
    elif help_command.lower() == "stop":
            print("Car Has Been Stopped......")
    elif help_command.lower() == "quit":
            break
    else:
            print("sorry invailed input......")









