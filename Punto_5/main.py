from antlr4 import *
from MaclaurinLexer import MaclaurinLexer
from MaclaurinParser import MaclaurinParser
from MyVisitor import MyVisitor

def main():
    entrada = input("Ingresa la expresión (ej: EXP(2, 10)): ")
    
    stream  = InputStream(entrada)
    lexer   = MaclaurinLexer(stream)
    tokens  = CommonTokenStream(lexer)
    parser  = MaclaurinParser(tokens)
    tree    = parser.prog()
    
    visitor = MyVisitor()
    visitor.visit(tree)

main()
