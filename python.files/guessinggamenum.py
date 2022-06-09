#SophiaSachedina

from ast import Num
import os
from socketserver import ThreadingUnixStreamServer
os.system ('cls')
import random
Game = True
cnt = 0
high = 0
name = input('What is your name? ')

def Menu(choice):
    global theNum
    if choice==1:
        theNum=random.randint(1,25)+1
    if choice==2:
        theNum=random.randint(1,50)+1
    if choice==3:
        theNum=random.randint(1,100)
    if choice==4:
        print("Instructions:")
        print("The objective of the game is to guess the number that is randomly chosen by the computer.")
        print("In Level 1, your options are numbers between 1 and 25, and you will get 10 guesses.")    
        print("In Level 2, your options are numbers between 1 and 50, and you will get 20 guesses.")   
        print("In Level 3, your options are numbers between 1 and 100, and you will get 30 guesses.")   
        print("If you do not guess the number correctly within the alloted amount of tries, you lose.")
        print("If you guess it right, your score will be calculated")
        print(input("press enter if you would like to go back to the menu"))
    if choice==5:
        



