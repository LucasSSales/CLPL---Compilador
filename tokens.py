from enum import  Enum
from Regex import  *
class TokenCategory(Enum):
    id, Init, TypeInt, TypeFloat, TypeBool, TypeChar, TypeString, TypeConst, OpArAd, OpArMult, OpArdiv, OpArMod, OpArExp, OpReD, OpReI, OpLogAnd, OpLogOr, OpLogNot, OpLogBand, OpLogBor, OpConcac, OpAtr, InsSIf, InsSElseif, InsSElse, InsInWh, InsInDo, InsInfor, BeginP, EndP, BeginC, EndC, BeginCh, EndCh, ConstInt, ConstFlaot, ConstBool, ConstChar, ConstString, SepV, SepPV, void, IntTo, IntRate = list(range(44))

class TokenStructure() :
    def __init__(self, token, value):
        this.token = token
        this.value = value
    def __str__(self):
        return "<" + this.token.name + " : " + this.value + ">"

def defineTokenCategory(type) :
    if type == 'int' :
        return  TokenCategory.TypeInt
    if type == 'Init' :
        return TokenCategory.Init
    if type == 'float' :
        return TokenCategory.TypeFloat
    if type == 'bool' :
        return TokenCategory.TypeBool
    if type == 'char' :
        return  TokenCategory.TypeChar
    if type == 'String' :
        return TokenCategory.TypeString
    if type == 'const' :
        return TokenCategory.TypeConst
    if type == '+' or type == '-' :
        return  TokenCategory.OpArAd
    if type == '*' :
        return  TokenCategory.OpArMult
    if type == '/' :
        return TokenCategory.OpArdiv
    if type == '%' :
        return TokenCategory.OpArMod
    if type == '^' :
        return  TokenCategory.OpArExp
    if type == '>' or type == '>=' or type == '<' or type == '<=' :
        return  TokenCategory.OpReD
    if type == '=' or type == '!=' :
        return  TokenCategory.OpReI
    if type == 'and' :
        return TokenCategory.OpLogAnd
    if type == 'or' :
        return  TokenCategory.OpLogOr
    if type == 'not' :
        return  TokenCategory.OpLogNot
    if type == 'bitand' :
        return  TokenCategory.OpLogBand
    if type == 'bitor' :
        return TokenCategory.OpLogBor
    if type == '==' :
        return TokenCategory.OpConcac
    if type == '=' :
        return  TokenCategory.OpAtr
    if type == 'if' :
        return TokenCategory.InsSIf
    if type == 'elseif' :
        return  TokenCategory.InsSIf
    if type == 'else' :
        return  TokenCategory.InsSElse
    if type == 'while' :
        return TokenCategory.InsInWh
    if type == 'do' :
        return TokenCategory.InsInDo
    if type == 'for' :
        return  TokenCategory.InsInfor
    if type == '(' :
        return TokenCategory.BeginP
    if type == ')' :
        return  TokenCategory.EndP
    if type == '[' :
        return  TokenCategory.BeginC
    if type == ']' :
        return TokenCategory.EndC
    if type == '{' :
        return  TokenCategory.BeginCh
    if type == '}' :
        return  TokenCategory.EndCh
    if isDigit(type) :
        return TokenCategory.ConstInt
    return TokenCategory.id
