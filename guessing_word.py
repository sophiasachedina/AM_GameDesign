#SophiaSachedina

#Assignment: 
    #Type your pseudocode at the top of your code as a comment
    #Give instructions to the user what is the game about (print statements, make it pretty)
    #Make a list of at least 10 words
    #Randomly select a word
    #ask the user to guess the word (give a hint about what kind of words you are using: fruits, animals,etc)
    #If they guess right congratulate them if not say sorry "you missed"
    #CHALLENGE: run the program until the user does not want to play any more

#Pseudocode:
    #start
    #import os and random
    #print instructions
    #input list of words (languages)
    #get list of languages
    #get randomizer to choose a language from the list above
    #print the hint saying: "hint, the answer is a language"
    #import the input to guess a language
    #print "your guess is correct!" if the guess was correct
    #input break is the guess was correct
    #print "sorry you missed:(" if the guess was incorrect
    #end

import random
import os
os.system('cls') 

#Instructions
print("Welcome to Sophia's Guessing Game!")
print("The Instructions for this game will be that you, the user will guess a word.")
print("The game will give you a hint to help you guess.")
print("If you guess the answer right, the computer will say, 'your guess is correct!'")
print("If you don't guess the answer right, the computer will say 'sorry you missed:('")

#list of languages"
languagelist = ["english", "spanish", "chinese", "french", "german", "japanese", "portugese", "hindi", "swahili", "vietnamese"]
#code to pick a random element in the list
word = str(random.choice(languagelist)) 
print(word)
#hint
print("hint: the answer is a language")
#tell user to type their guess 
guess = input("type your guess")
#message if the guess is correct
if guess.lower() == word.lower():
    print("your guess is correct!")
#message if the guess is incorrect
else:
    print("sorry you missed:(")