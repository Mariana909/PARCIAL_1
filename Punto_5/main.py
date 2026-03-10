import sys
from antlr4 import *
from MaclaurinLexer import MaclaurinLexer
from MaclaurinParser import MaclaurinParser
from MyVisitor import MyVisitor

def procesar(entrada):
    stream  = InputStream(entrada)
    lexer   = MaclaurinLexer(stream)
    tokens  = CommonTokenStream(lexer)
    parser  = MaclaurinParser(tokens)
    tree    = parser.prog()
    visitor = MyVisitor()
    visitor.visit(tree)

try:
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            datos = f.read().splitlines()
            for linea in datos:
                if linea.strip():
                    print(f"\n── Entrada: {linea} ──")
                    try:                         
                        procesar(linea.strip())
                    except Exception:
                        print("Entrada inválida") 
    else:
        entrada = input()
        procesar(entrada)

except FileNotFoundError:
    print("No se encontró el archivo")
except Exception as e:
    print(f"Error: {e}")
