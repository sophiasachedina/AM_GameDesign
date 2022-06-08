#Sophia Sachedina
from ctypes.wintypes import WORD
import random
import os 

os.system ('cls')
from time import sleep
seconds=.5

theWord=""

languagelist = ["english", "spanish", "chinese", "french", "german", "japanese", "portugese", "hindi", "swahili", "vietnamese"]
flowerlist = ["daisy","sunflower",'dandelion', "rose", "hibiscus"]
streamingserviceslist = ["netflix","hulu", "hbo", "disney+", "prime"]

Game=True
cnt=0
def hint():
    global cnt    
    if cnt ==0:
        print("Here is a hint:")
        print("This is a widely spoken language in the world")
       

    else:
        print("Try again untill you get it right")
    
    print()
def selectWrd(choice): 
    global theWord
    if choice ==1:
        theWord= random.choice(languagelist)    
    if choice ==2:
        theWord= random.choice(flowerlist)
    if choice ==3:
        theWord= random.choice(streamingserviceslist)
    return theWord  
name=input("What is your name? ")
high=0 
while Game:
    
    print("Welcome to Sophia's Guessing Game!")
    print("You have the choice to pick one of three lists to guess a word from")
    print("List 1 is about languages, List 2 is about flowers, and Lost 3 is about streaming services.")
    print("The game will give you a hint to help you guess.")

    
    print(name, end=", ")
    answer=input("Would you like to play? ")
    if 'n' in answer:
        break
    while True:
        choice=input("What game would y like to play 1, 2, or 3")
        try:
            choice=int(choice)
            if choice>0 and choice <4:
                break
            else:
                print("give me 1, 2, or 3")
        except:
            print("i need to know which game you want to play, sorry!")
    theWord = selectWrd(choice) 
    os.system('cls')
    check=True
    while check and cnt <5:
        guess=input("type your guess: ")
        print()
        if guess == theWord:
            print("Yay! You guessed correct!")
            check=False
        else:
            hint()
        cnt+=1  
        if cnt ==5:
            print("Sorry!" )
    score=200-40*cnt
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