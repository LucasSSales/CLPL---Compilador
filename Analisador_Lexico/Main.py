from compiler import *
import sys

filename = sys.argv[1]
file = open(filename, "r")

myreader = reader(file)
end = True
line = 0
while end :
    while not myreader.queue :
        myline = myreader.nextLine()
        line += 1
        if myline == "" :
            end = False
            break
        else :
            print(myline, end = '')
        myreader.queue = readLine(myline, line)
    if end :
        print(myreader.nextToken())  
    