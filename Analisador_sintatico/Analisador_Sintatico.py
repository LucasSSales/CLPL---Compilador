class AnalisadorSintatico():
    def __init__(self):
        self.table = self.getTable()
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