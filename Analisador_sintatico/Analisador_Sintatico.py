from Analisador_Lexico.Analizador_Lexico import *
class SlrParse():
    def __init__(self, filename):
        self.table = self.getTable()
        self.actions = self.getActions()
        self.stack = []
        self.myreader = reader(filename)
    def getTable(self):
        op = open("SLRTable.csv", 'r').read()
        op = op.split('\n')
        op = op[2:]
        t = []
        for i in op:
            o = i.split(",")
            t.append(o[1:])
        table = {}
        k = t.pop(0)
        for i in k:
            table[i] = []
        for i in t:
            for j in table.keys():
                table[j].append(i.pop(0))
        return table
    def getActions(self):
        op = open("SLRTable.csv", 'r').read()
        op = op.split('\n')
        t = []
        for i in op:
            t.append(i.split(" "))
        return  t