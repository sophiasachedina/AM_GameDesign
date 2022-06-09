#SophiaSachedina
#Learning about lists, functions of lists
#we are going to learn about for loop

import random #allows you to get pseudorandom values
import os #library to clear screen
os.system('cls')

thislist = ["apple", "banana", "cherry", "kiwi", "melon", "mango"]
#              0         1         2        3       4        5     
#             -6        -5        -4       -3      -2       -1 
#print from a specific index, in this case banana (second index)
print(thislist[1])
#negative starts at the end (banana would be negative 2 bc it is second from the last)
#print 2nd to last term from the end
print(thislist[-2])
#print range of elements in a list (index 2-4)
print(thislist[2:4])
#everything up to an index number
print(thislist[:3])
#from an element to the end
print(thislist[2:])
#between numbers from the end of the list
print(thislist[-4:-1])

#is any element is the list is apple, even if there are multiple elements are apple
if "apple" in thislist:
    print("yes the apple is in the list")

#num is amount of times it loops through
for num in range(10):
    print(num, end = "")
print()

#example 2
#element acts as a specific index in the list
for element in thislist: #element thislist(times run through the loop)
    print(element, end = "")

#how to add elements to a list
#method 1
thislist.append("pineapple") #will add a specific element to the end of the list
print(thislist[0:])

#method 2
# for num in range(10):
#     thislist.append(input("input a food"))
# print(thislist[0:])

#adding a certain element to a specific index insert(index, "element you want to add")
#put pineapple in front of the list
thislist.insert(0, "pineapple")
print(thislist[0:])

#how many elements are in the list
for i in range(len(thislist)):
    print(thislist[i], end = " / ")
print()

#to add the elements of two lists (putting them both together)
list_num = [1, 2, 3, 4]
thislist.extend(list_num)
print(thislist)
#add the whole list inside of the other list
list_num.append(thislist)
print(list_num[-1])
print(list_num[-1][0])

#how to selsct a random element from a list
word = str(random.choice(thislist)) ##picks a random element in the list
print(word)

guess = input("input a food")
if guess.lower() in word.lower():
    print("congrats you guessed the food")

for i in range (40):
    print("*", end = "")
print()

print("*****************")
print("** Guess the Food**")
print("*         *")
