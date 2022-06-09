#SophiaSachedina
#Eitan Hahn
#Guess the number game
import os

os.system('cls')
import random
cnt=0
print('---------------------')
print('GUESS THE NUMBER GAME')
print('---------------------')
print('Level 1: 1-25')
print('Level 2: 1-50')
print('Level 3: 1-100')
print()
name=input('What is your name?')
print (name, end="" )
Game=True
level=""
theNum=0
def selectNum(choice):
    
    global theNum, level
    if choice==1:
        theNum=random.randint(1,25)  # you must give a beginning and end
        level="1-25"
    if choice==2:
        theNum=random.randint(1,50)
        level="1-50"
    if choice==3:
        theNum=random.randint(1,100) 
        level="1-100"
    if choice==4:
        print("Instructions:")
        print("The objective of the game is to guess the number that is randomly chosen by the computer.")
        print("In Level 1, your options are numbers between 1 and 25, and you will get 10 guesses.")    
        print("In Level 2, your options are numbers between 1 and 50, and you will get 20 guesses.")   
        print("In Level 3, your options are numbers between 1 and 100, and you will get 30 guesses.")   
        print("If you do not guess the number correctly within the alloted amount of tries, you lose.")
        print("If you guess it right, your score will be calculated")
        print(input("press enter if you would like to go back to the menu"))

    return theNum
high=0 
while Game:
    choice=input(', Which level would you like to play? (press 4 if you would like to see instructions')
    
    while True:         # the try and except should be in a while loop
        try:
            choice=int(choice) 
            if choice > 0 and choice < 5:
                break
            else:
                print('give me 1, 2, or 3')
        except:
            print('Tell me which level you want to play')
        
    theNum=selectNum(choice)
    os.system('cls')
    check=True
    while check and cnt < 5:
        message="give me a number between "+ level
        guess=int(input(message))
        if guess==theNum:
            print('congratulations! you guessed the correct number')
            score=110-10*cnt
            if score > high:   
                high=score
                print(name+", your score is "+str(score))
                input("Press enter ")
                os.system('cls')
  
                answer=input("Do you want to play again? ")
                if ('n' or 'N') in answer:
                    Game=False
                print("Thank you for playing! I hope you enjoyed:)" )
            
    cnt=0 
print("Wow! Your highest score was: " + str(high))

import random
import os, datetime

os.system('cls')

date=datetime.datetime.now()
print(date)
print(date.strftime("%m-%d-%Y"))


sce=str(high)
scrLine=str(sce)+"\t "+name + "\t"+date.strftime("%m-%d-%Y")+ "\n"
myFile = open("scre.txt", 'a')
myFile.write(scrLine)
myFile.close()
myFile = open("scre.txt", 'r')
stuff=myFile.readlines()
stuff.sort(reverse=True)
myFile.close()
for line in stuff:
    print(line)
    check=False
    if guess!= theNum: 
            print("Try again")
    cnt+=1
    if cnt==10:
            print("You Lose:(")
    