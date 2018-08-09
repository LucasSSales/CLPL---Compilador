import re

digit = re.compile("\d+")
decimal = re.compile("(\d)+.(\d)+")
char = re.compile("'\w'", re.ASCII)
word = re.compile("\"\w*\"", re.ASCII)
id = re.compile("[a-zA-z][a-zA-z\d]*")
Global = re.compile("@[a-zA-z][a-zA-z\d]*")

def isRegex(num, regex) :
    i = regex.match(num)
    if i == None : return  False
    return i.group() == num

