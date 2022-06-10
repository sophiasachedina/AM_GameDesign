#SophiaSachedina
#This was very hard I hope it works

import os
os.system ("cls")
import random
continuePlaying = True
count = 0
level = 1
score = 0

name=input("What is your name? ")

def game (level, theNum):
    print( "Guess number between 1 and ",theNum)
    ifNotGuessed = True
    global score
    guesses = 0
    random_number = random.randint(1,theNum)
    print("random num is ", random_number)
    while ifNotGuessed and guesses < 5:
        guess = int(input('type your guess '))
        print(random_number)
        if guess == random_number:
            print("You guessed it right!")
            ifNotGuessed = False
        else:
            print("Sorry, you got it wrong:( Please try again.")     
    if ifNotGuessed == True:
        print("Oh No! You lose")
    
print ("Hi, " +name, "Welcome to Guess the Number!")


while continuePlaying:
    print("Menu: \n 1. View Instructions \n 2. level: 1 - 25 \n 3. Level 2: 1-50 \n 4. Level 3: 1-100 \n 5. Print Score \n 6. Exit \n       ")
    selection = input('Enter the number that corresponds to what you would like to do from the options above: ')
    try:
        selection = int(selection)
    except:
        print('You must enter a number')
    if selection == 1:
        print("Instructions:")
        print("The objective of the game is to guess the number that is randomly chosen by the computer.")
        print("In Level 1, your options are numbers between 1 and 25, and you will get 10 guesses.")    
        print("In Level 2, your options are numbers between 1 and 50, and you will get 20 guesses.")   
        print("In Level 3, your options are numbers between 1 and 100, and you will get 30 guesses.")   
        print("If you do not guess the number correctly within the alloted amount of tries, you lose.")
        print("If you guess it right, your score will be calculated")
        print("Now, select which level you would like to play from the menu.")
    elif selection == 2:
        game(level, 25)
    elif selection == 3:
        game(level, 50)
    elif selection == 4:
        game(level, 100)
    elif selection == 5:
        while count <5:
            print() 
        score=500-10*count   
        print(name+ ", your score is "+str(score))
    elif selection == 6:
        continuePlaying = False
        import os, datetime

        os.system('cls')
        high=score
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
        
        


