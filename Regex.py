import re

digit = re.compile("^[0-9]+")

def isDigit(string) :
    i = digit.match(string)
    if i == None : return  False
    return i.group() == string


