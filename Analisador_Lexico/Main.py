from Analizador_Lexico import *
import sys

filename = sys.argv[1]
file = open(filename, "r")

myreader = reader(file)
end = True
line = 0
k = myreader.nextToken()

while k.token.value != TokenCategory.EOF.value :
    print(k)
    k = myreader.nextToken()
print(k)