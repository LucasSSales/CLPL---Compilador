from enum import  Enum
from Analisador_Lexico.Regex import  *
class TokenCategory(Enum):
    Id, Init, TypeInt, TypeFloat, TypeBool, TypeChar, TypeString, TypeConst, OpArAd, OpArMult, OpArdiv, OpArMod, OpArExp, OpReD, OpReI, OpLogAnd, OpLogOr, OpLogNot, OpLogBand, OpLogBor, OpConcac, OpAtr, InsSIf, InsSElseif, InsSElse, InsInWh, InsInDo, InsInfor, BeginP, EndP, BeginC, EndC, BeginCh, EndCh, ConstInt, ConstFlaot, ConstBool, ConstChar, ConstString, SepV, SepPV, void, IntTo, IntRate, Out, In, Global, SepPont, Return, EOF = list(range(50))

class Token() :
    def __init__(self, token, value, line, column):
        self.token = token
        self.value = value
        self.line = line
        self.column = column
    def __str__(self):
        return  "              [%04d, %04d] (%04d, %10s) {%s}" %(self.line+1,self.column+1, self.token.value, self.token.name, self.value)



def defineTokenCategory(type) :
    if type == 'output' : return TokenCategory.Out
    if type == 'input' : return TokenCategory.In
    if type == 'return' : return TokenCategory.Return
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
    if type == '==' or type == '!=' : return  TokenCategory.OpReI
    if type == 'and' : return TokenCategory.OpLogAnd
    if type == 'or' : return TokenCategory.OpLogOr
    if type == 'not' : return TokenCategory.OpLogNot
    if type == 'bitand' : return TokenCategory.OpLogBand
    if type == 'bitor' : return TokenCategory.OpLogBor
    if type == '++' : return TokenCategory.OpConcac
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
    if isRegex(type, id) : return  TokenCategory.Id
    if isRegex(type, Global) : return TokenCategory.Global
    if type == ':' : return TokenCategory.SepPont
    if type == "" : return TokenCategory.EOF
    return None
