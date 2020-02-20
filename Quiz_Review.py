
import decimal
from random import randint, random

a = """a
b
c
d"""

b = ' Hello "World" '

c = 'don\'t'

d = "This is a quote: \" "

t = "Thank" + "-" + "You"

repetition = "*" * 3

#print(repetition)

#print("First value is %d and second value is %d." %(3,5))
#print("First letter is %s and second letter is %s." %("S","H"))

#print("{} {}".format("Hello","World"))
#print("{1} {0}".format("Hello","World"))
#print("{0} {1}".format("Hello","World"))
#print("{2} {1} {0}".format("Good","Morning","guys"))

# original data type: integer
x = 41    # data type: integer
y = "41"  # data type: string
z = "90"   # data type: string

x = str(x)    #data type: string
y = int(y)

#print(type(x))
#print(type(y))
#print(type(decimal.Decimal(z)))

#print(b)
#print(len(b))
#print(b.strip())
#print(len(b.strip()))
#print(b.upper())
#print(b.replace("Hello","Hey"))


# print on the same line
for i in range(1,11):
    print (i, end="")

# print "*",
# print "*",

# x = "$" * 3
# for i in range(1,5):
    # print("$"* i)

birth_year = 1985
current_year = 2020

# print("Lived_Month : " + str((current_year - birth_year)*12))
# print("Lived_Day : " + str((current_year - birth_year)*12*365))


# Celcius = input("\n Celcius: ")
# Fahrenheit = (9 * Celcius)/5 + 32
# print(Fahrenheit)


# print initials
# first_name = raw_input("What is your first name >")
# last_name = raw_input("What is your last name >")

# first_name = first_name.strip().upper()
# last_name = last_name.strip().upper()

# print("The initials are %s and %s" % (first_name[0], last_name[0]))
# print("The initials are {0} and {1}".format(first_name[0], last_name[0]))


# num = input("Input a number > ")

# if num % 10 == 0:
    # print("A multiplier of 10.")
# else:
    # print("Not a multiplier of 10.")


# i = 1
# while i < 10:
    # print(i),
    # i += 1
    # if i == 6:
        # break
# 1 2 3 4 5

# i = 1
# while i < 10:
    # print(i),
    # if i == 6:
        # break
    # i += 1
# 1 2 3 4 5 6

# i = 1
# while i < 6:
    # i += 1
    # if i == 3:
        # continue
    # print(i),
# 2 4 5 6


# message = " "
# while message != "quit":
    # message = raw_input("Input a word > ")
    # print (message)
    # if message == "quit":
        # print ("Loop is ended.")


# num = input("Enter a number: ")
# while num != 1:
    # if num % 10 == 0:
        # print("It is a multiplier of 10.")
        # num = input("Enter a number: ")
    # elif num % 10 != 0:
        # print("Not a multiplier of 10.")
        # num = input("Enter a number: ")


#for a in range(1,101):
    #if a % 2 == 0:
        #print (a),


# for num in range(0,26):
    # if num % 3 == 0:
        # if num % 5 == 0:
            # if num == 0 or num == 15:
                # print(num),
                # print("FizzBuzz")
                # continue
            # print(num),
            # print("FizzBuzz")
        # print(num),
        # print("Fizz")
    # elif num % 5 == 0:
        # print(num),
        # print("Buzz")
    # else:
        # print(num)


# for i in range(0,101):
    # a = randint(0,101)
    # print(a)
    # num = input('Input a number: ')
    # if num > a:
        # print("Greater than the chosen number.")
    # elif num < a:
        # print ("Less than the chosen number.")
    # elif num == a:
        # print("Bravo, you guess correctly after " + str(i) + " times.")
        # break


# alist = [1,42,"Hello"]
# blist = [1,42,"Hello",["a","b","c"],2,3]

# print (alist[1])
# for a in alist[-2:]:
    # print(a),


import random
# random_list=[random.randrange(1,100)for i in range(1,21)]
# print(random_list)

# max = random_list[0]
# min = random_list[0]
# for n in random_list:
    # if n > max:
        # max = n
# print (max)

# for n in random_list:
    # if n < min:
        # min = n
# print(min)

# Length = len(random_list)
# Sum = sum(random_list)
# Max = max(random_list)
# Min = min(random_list)
# Average = Sum / Length

# print(Length)
# print (Sum)
# print (Max)
# print (Min)
# print (Average)



# squares = [value**2 for value in range(1,11)]
# print(squares)

# pow(value, exponent)
# power_list = [pow(2,n) for n in range(1,11)]
# print (power_list)


# mylist = ["A", "B", "C"]
# mylist2 = ['abc', mylist, [1, 2, 3]]

# item1 = mylist2[2][2]
# item2 = mylist2[0]
# item3 = item2[2]
# item4 = mylist2[1][1]

# print(item1) # 3
# print(item2) # abc
# print(item3) # c
# print(item4) # B


# mylist = ["A","B","C"]

# copied_list_1 = mylist
# copied_list_2 = mylist[:]

# mylist[1] = "X"

# print (copied_list_1)
# print (copied_list_2)


# countries = {'us': 'USA', 'fr': 'France', 'uk': 'Eng', "jp": "Japan"}

# countries.update({"de":"Germany"})
# countries["jp"] = "Japan"
# del countries["us"]
# countries.clear()
# del countries

# print countries['uk']
# print (countries.get('zb', 'Unknown'))
# print (countries)


# for n in countries.keys():
    # print(n)

# for k in countries.values():
    # print(k)

# for m in countries.items():
    # print(m)

# print("fr" in countries)
# print("zb" in countries)



# with open("my_input_file.txt","w") as file_object:
    # file_object.write("Welcome \n")
    # file_object.write("To Python \n")

# with open("my_input_file","a") as file_object:
    # file_object.write("Thanks!")

# with open("my_input_file","r") as file_object:
    # lines = file_object.readlines()

# for line in lines:
    # print (line.rstrip())


# f = open("test_file2.txt", "w+")
# f.write("Testing 123")
# print(f.read())
# f.seek(4)
# f.write("*")
# f.seek(0)
# print(f.read())



#filename = raw_input('Enter a file name: ')
#try:
    #f = open (filename, "r")
#except IOError:
    #print ('There is no file named', filename )


# try:
    # f = open("test_file2.txt", 'rb')
# except IOError:
    # print "Could not read file:", test_file2.txt
    # sys.exit()


# Approach 1

# import os

# if os.path.exists("test_file.txt"):
    # print("True")
# else:
    # print ("False")


# Approach 2

# try:
    # f = open("test_file.txt", 'r')
    # print ("True")
# except IOError:
    # print "False. Could not read file:", "test_file.txt"


# mylist = ["red","green","blue"]
# mylist.append("black")
# mylist.append(("white"))
# mylist[2] = "yellow"
# del mylist[1]
# mylist.remove("red")

# print(mylist)
# print(len(mylist))

# for (n,i) in zip(range(len(mylist)),mylist):
    # n += 1
    # print (n),
    # print (i.capitalize())
