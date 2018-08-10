from compiler import *
import sys

def nextToken() :
    if sequence :
        return sequence.pop(0)
    return "Vazio"

filename = sys.argv[1]
file = open(filename, "r")
sequence = []
end = True
line = 0
while end :
    while not sequence :
        myline = file.readline()
        line += 1
        if myline == "" :
            end = False
            break
        sequence = readLine(myline, line)
    if end :
        print(nextToken())  