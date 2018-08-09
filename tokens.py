from enum import  Enum
from Regex import  *
class TokenCategory(Enum):
    id, Init, TypeInt, TypeFloat, TypeBool, TypeChar, TypeString, TypeConst, OpArAd, OpArMult, OpArdiv, OpArMod, OpArExp, OpReD, OpReI, OpLogAnd, OpLogOr, OpLogNot, OpLogBand, OpLogBor, OpConcac, OpAtr, InsSIf, InsSElseif, InsSElse, InsInWh, InsInDo, InsInfor, BeginP, EndP, BeginC, EndC, BeginCh, EndCh, ConstInt, ConstFlaot, ConstBool, ConstChar, ConstString, SepV, SepPV, void, IntTo, IntRate = list(range(44))

class Token() :
    def __init__(self, token, value, line, column):
        self.token = token
        self.value = value
        self.line = line
        self.column = column
    def __str__(self):
        return "<" + self.token.name + " : " + self.value + " , " + str(self.line) + ", " + str(self.column) + ">"

atomics = ['+', '-', ';']

def nextChar(currente, next) :
    #print("currente: " + str(currente))
    #print("next: " + str(next))
    #print()
    if currente == '' and next != ' ': return True
    if currente[0] == "\"": return True
    if next == ' ' or next == '(' or next == ')': return False
    if currente in atomics or next in atomics : return False

    return True


def defineTokenCategory(type) :
    if type == 'int' : return  TokenCategory.TypeInt
    if type == 'Init' : return TokenCategory.Init
    if type == 'float' : return TokenCategory.TypeFloat
    if type == 'bool' : return TokenCategory.TypeBool
    if type == 'char' : return  TokenCategory.TypeChar
    if type == 'String' : return TokenCategory.TypeString
    if type == 'const' : return TokenCategory.TypeConst
    if type == '+' or type == '-' : return  TokenCategory.OpArAd
    if type == '*' : return  TokenCategory.OpArMult
    if type == '/' : return TokenCategory.OpArdiv
    if type == '%' : return TokenCategory.OpArMod
    if type == '^' : return  TokenCategory.OpArExp
    if type == '>' or type == '>=' or type == '<' or type == '<=' : return  TokenCategory.OpReD
    if type == '=' or type == '!=' : return  TokenCategory.OpReI
    if type == 'and' : return TokenCategory.OpLogAnd
    if type == 'or' : return TokenCategory.OpLogOr
    if type == 'not' : return TokenCategory.OpLogNot
    if type == 'bitand' : return TokenCategory.OpLogBand
    if type == 'bitor' : return TokenCategory.OpLogBor
    if type == '==' : return TokenCategory.OpConcac
    if type == '=' : return TokenCategory.OpAtr
    if type == 'if' : return TokenCategory.InsSIf
    if type == 'elseif' : return  TokenCategory.InsSIf
    if type == 'else' : return  TokenCategory.InsSElse
    if type == 'while' : return TokenCategory.InsInWh
    if type == 'do' : return TokenCategory.InsInDo
    if type == 'for' : return  TokenCategory.InsInfor
    if type == '(' : return TokenCategory.BeginP
    if type == ')' : return  TokenCategory.EndP
    if type == '[' : return  TokenCategory.BeginC
    if type == ']' : return TokenCategory.EndC
    if type == '{' : return  TokenCategory.BeginCh
    if type == '}' : return  TokenCategory.EndCh
    if isRegex(type, digit) : return TokenCategory.ConstInt
    if isRegex(type, decimal) : return  TokenCategory.ConstFlaot
    if type == 'false' or type == 'true' : return TokenCategory.ConstBool
    if isRegex(type, char) : return  TokenCategory.ConstChar
    if isRegex(type, word) : return TokenCategory.ConstString
    if type == ',' : return  TokenCategory.SepV
    if type == ';' : return TokenCategory.SepPV
    if type == 'void' : return TokenCategory.void
    if type == 'to' : return TokenCategory.IntTo
    if type == 'rate' : return TokenCategory.IntRate
    if isRegex(type, id) : return  TokenCategory.id
    return None
