from tokens import *

tokenSequence = []
filename = "test.txt" #input()
file = open(filename, "r")
l = 0
atomics = [' ', '{', '}', '(', ')', ':', '\n', ';', '+', '-','*','/','%','^',',', '>', '<', '=']
isString = False
#ver: aspas, comentarios, ERROS E <= >= == E ESSES cOMPOSTOS

for lines in file.readlines() :
    c = 0
    newtoken = ''
    character = ''
    for character in lines:
        if(character == '\"'):isString = not isString
        #print(newtoken)
        #print(character)
        #   print()
        if isString == False and character in atomics:
            print(newtoken)
            if(newtoken != ''):
                tokenSequence.append(Token(defineTokenCategory(newtoken), newtoken))
            newtoken = ''
            if(character != ' ' and character != '\n'):
                #print(character)
                tokenSequence.append(Token(defineTokenCategory(character), character))
            continue


        newtoken += character


        c = c + 1
    l = l + 1
    #if(newtoken == ''): continue
    #tokenSequence.append(Token(defineTokenCategory(newtoken), newtoken, l, c-1))
    #print(newtoken)

for i in tokenSequence :
    print(i)