from tokens import *

atomics = [' ', '{', '}', '(', ')', '[', ']', ':', '\n', ';', '+', '-','*','/','%','^',',', '>', '<', '=', '!']
composites = ['>=', '<=', '==', '!=', '++']

def readLine(lines, numLine):
    column, character = 0, ''
    tokenSequence = []
    isString, isComment, newtoken, line = False, False, '', 0
    for character in lines:
        column += 1
        #comentario de bloco
        if (newtoken + character == "/*") and isString == False:
            isComment = True
        #fecha comentario de bloco se ja estiver em um comentario
        if isComment == True and (newtoken[-1] + character == "*/"):
            isComment = False
            newtoken = ''
            continue

        #quando encontra comentario de linha, para o loop e vai p proxima linha
        if newtoken + character == '//':
            newtoken = ''
            break

        #quando encontra abre/fecha aspas, se tiver \ antes, nao reconhece
        if(character == '\"' and newtoken[-1] != '\\' and isComment == False):
            isString = not isString
            #se antes das aspas tiver um abre parenteses, lanca o token
            if(newtoken == '('):
                tokenSequence.append(Token(defineTokenCategory(newtoken), newtoken, numLine, column))
                newtoken = ''

        #so entra se nao estiver concatenando uma string ou lendo um comentario
        #eh aqui que os tokens serao lancados
        if (isString == False and isComment == False):
           #caso token pertenca a composites
            if(newtoken + character in composites):
                tokenSequence.append(Token(defineTokenCategory(newtoken + character), newtoken + character, numLine, column))
                newtoken = ''
                continue
            #caso token pertenca a atomics
            elif(newtoken in atomics):
                tokenSequence.append(Token(defineTokenCategory(newtoken), newtoken, numLine, column))
                newtoken = ''
            #caso mais geral, tratando p n entrar nulo
            elif(newtoken != '' and character in atomics):
                tokenSequence.append(Token(defineTokenCategory(newtoken), newtoken, numLine, column))
                newtoken = ''

            #apos lancar o token, se estiver num ' ' ou num '\n', passa pro proximo
            if(character == ' ' or character == '\n'): continue

        newtoken += character
        #tokenSequence.append(Token(defineTokenCategory(newtoken), newtoken, 0, column))
    return tokenSequence
