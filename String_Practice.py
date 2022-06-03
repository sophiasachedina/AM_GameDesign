#SophiaSachedina
#This is the string practice for June 2
#len
#strings as arrays
#
#Exercise 1A: Create a string made of the first, middle and last character

import os

os.system('cls') 

str1='James'
#print the whole word
print(str1[0], end="")
#print middle letter
middle= int(len(str1)/2)
#print last letter
print(str1[middle], end="")
#print the amount of characters
print(str1[len(str1)-1])

#Exercise 1B: Create a string made of the middle three characters
#case1
str1="JhonDipPeta"
#print characters 'Dip'
print(str1[4:7])
#case2
#print characters 'Son'
str2="JaSonAy"
print(str2[2:5])

#Excercise 2: Append new string in the middle of a given str8ng
#Given 2 strings, s1 and s2, write a progeam to creat a new string called s3 by appending s2 in the middle of s1
#Given strings:
s1="Ault"
s2="Kelly"
#print first 3 characters of s1
print(s1[0:2],end="")
#print first 5 characters of s2 after the first 3 characters of s1
print(s2[0:5],end="")
#print the last 2 characters of s1 after the first 5 characters of s2
print(s1[2:4])

#Excercise 3: Creat a new string made of the first, middle, and last characters of each input string
#Given:
s1="America"
s2="Japan"
#print 1st character of s1 
print(s1[0],end="")
#print 1st character of s2 directly after
print(s2[0],end="")
#print 4th character/3rd index of s1 directly after
print(s1[3],end="")
#print 3rd character/2nd index of s2 directly after
print(s2[2],end="")
#print 7th character/6th index of s1 directly after
print(s1[6],end="")
#print 5th character/4th index of s2 directly after
print(s2[4])

#Excercise 4:  Arrange string characters such that lowercase letters should come first
#Given:
str1="PyNaTive"
#Print 2nd character
print(str1[1],end="")
#Print 4th character directly after
print(str1[3],end="")
#Print 5th through 7th characters directly after
print(str1[5:8],end="")
#Print 1st character directly after
print(str1[0],end="")
#Print 3rd character directly after
print(str1[2],end="")
#Print 5th character directly after
print(str1[4],end="")