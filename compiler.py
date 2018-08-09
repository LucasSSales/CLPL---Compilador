from tokens import *

tokenSequence = []
filename = "test.txt" #input()
file = open(filename, "r")
l = 0
for lines in file.readlines() :
    c = 0
    newtoken = ''
    character = ''
    for character in lines:
        if(character == '\n'):continue

        if nextChar(newtoken, character):
            newtoken += character
        elif character != ' ':
            tokenSequence.append(Token(defineTokenCategory(newtoken), newtoken, l, c-1))
            newtoken = ''
            newtoken += character
        else:
            tokenSequence.append(Token(defineTokenCategory(newtoken), newtoken, l, c-1))
            newtoken = ''
        c = c + 1
    l = l + 1
    if(newtoken == ''): continue
    tokenSequence.append(Token(defineTokenCategory(newtoken), newtoken, l, c-1))
    #print(newtoken)

for i in tokenSequence :
    print(i)