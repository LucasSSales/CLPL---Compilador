from tokens import *


tokenSequence = []
filename = input()
file = open(filename, "r")
for lines in file.readlines() :
    newtoken = ''
    character = ''
    for character in lines:
        if nextChar(newtoken, character):
            newtoken += character
        elif character != ' ':
            tokenSequence.append(Token(defineTokenCategory(newtoken), newtoken))
            newtoken = ''
            newtoken += character
        else:
            tokenSequence.append(Token(defineTokenCategory(newtoken), newtoken))
            newtoken = ''
    tokenSequence.append(Token(defineTokenCategory(newtoken), newtoken))

for i in tokenSequence :
    print(i)