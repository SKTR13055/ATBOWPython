#! /usr/bin/env/ python3
#This project aims for adding bulled points the particular lines/paragraph
#bulletPointAdder.py - Add wikipedia bullet points at the start to the start of each line of the text on the clipboard
import pyperclip

text = pyperclip.paste()
print(list) #check if the clipboard works or not

#Seperate lines and add stars
lines = text.split('\n')
print(lines)
for i in range(len(lines)): #loop through all the indexes in the "lines" list
    lines[i] = '* ' + lines[i] #add star to each string in "lines" list
text = '\n'.join(lines)#pyperclip.copy() is expecting a single string value, not a list of string values. so hence we use join
pyperclip.copy(text)