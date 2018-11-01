from Analizador_Lexico import *
import sys


filename = sys.argv[1]
file = open(filename, "r")

myreader = reader(file)
k = myreader.nextToken()

while k.token.value != TokenCategory.EOF.value :
    print(k.token)
    k = myreader.nextToken()
print(k)


