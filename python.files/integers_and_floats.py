#SophiaSachedina
#Assignment: Write a code that find if the number input by the user is even or odd if the number is multiple of 3 or 5

import os

os.system('cls') 

#tell user to give the program a number
number=int(input("your number is"))
#tell program that if the number is divisible by 2, tell the user it is an even number
if(number%2==0):
    print("number is even")
    #tell program that if the number is not divisible by 2, tell the user it is an odd number
else:
    print("number is odd")
#tell program that if the number is divisible by 3, tell the user it is a multiple of three
if(number%3==0):
    print("this is a multiple of three")
#tell program that if the number is divisible by 5, tell the user it is a multiple of five
if(number%5==0):
    print("this is a multiple of five")

