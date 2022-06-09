#RuthGebru
#we are going to play a guessing game and there will be levels and choices that will need to be madee


import random






def game (level, hiNum):
    print( "**** LEVEL",level," *****\nGuess number between 1 and ",hiNum)
    ifNotGuessed = True
    global score
    guesses = 0
    random_number = random.randint(1,hiNum)
    print("random num is ", random_number)
    while ifNotGuessed and guesses < 5:
        guess = int(input('guess what number between 1 through 25 '))
        print(random_number)
        if guess == random_number:
            print("Congragulations you guessed the number!")
            ifNotGuessed = False
            score += 1
        else:
            print("Sorry, please guess again")
            guesses += 1
    if ifNotGuessed == True:
        print("Sorry you lose")
    






print ("*****************************")
print ("*     Number Game yay!!!     ")
title="guessing number game"
print('this is a guessing game and you will only get 5 tries and i hope you have fun')

continuePlaying = True
count = 0
level = 1
score = 0

while continuePlaying:
    print(" 1 Instruction \n 2 level: 1 - 25 \n 3 Level 2: 1-50 \n 4 Level 3: 1-100 \n 5 Print Score \n 6 Exit")
    selection = input('Enter a selection from the menu: ')
    try:
        selection = int(selection)
    except:
        print('You must enter a number')
    if selection == 1:
        print("chose a number between 1 and 25, so be smart!!!")
    elif selection == 2:
        game(level, 25)
    elif selection == 3:
        game(level, 50)
    elif selection == 4:
        game(level, 100)
    elif selection == 5:
        print("your score is: ",score)
    elif selection == 6:
        continuePlaying = False


        
    

        