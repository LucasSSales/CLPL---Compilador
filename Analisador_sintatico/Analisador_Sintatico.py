from Analizador_Lexico import *
import sys

class SlrParse():
    def __init__(self):
        self.table = self.getTable()
        self.actions = self.getActions()
        self.stack = ['0']
        #self.myreader = reader(filename)
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
        op = open("Actions.txt", 'r').read()
        op = op.split('\n')
        t = []
        for i in op:
            t.append(i.split(" "))
        return t

    def prints(self):
        print(self.actions)

    def analyse(self):
        token = self.myreader.nextToken()
        while token.token.value != TokenCategory.EOF.value:
            action = self.table[token][self.stack[-1]] #pega acao na tabela
            print("              " + str(token)) #listando tokens
            if(action[0] == "e"):
                stack.append(token) #empilha token
                stack.append(action[1:]) #empilha valor
            elif(action[0] == "s"):
                print("          " + str(self.actions[ action[1:] ]))  # imprimir producao
                n = 2 * (len(self.actions[ action[1:] ])-2) #num de simbolos no lado direito da producao
                for i in range(n):
                    stack.pop(-1)  #desempilha as producoes que serao reduzidas
                y = stack[-1] #novo topo -> numero empilhado anteriormente
                x = self.actions[ action[1:] ][0] #simbolo do lado esquerdo da producao reduzida
                stack.append( x ) #empilha o simbolo do lado esquerdo da producao
                stack.append( self.table[y][x] ) #empilha o valor da transicao
            else:
                print("ERRO")
            token = myreader.nextToken()
        #print("              " + str(token))  # listando tokens




