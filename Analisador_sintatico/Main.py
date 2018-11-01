from Analisador_Sintatico import *
import sys

filename = sys.argv[1]
file = open(filename, "r")

analyser = SlrParse(file)
analyser.analyse()
