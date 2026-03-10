# Generated from Maclaurin.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MaclaurinParser import MaclaurinParser
else:
    from MaclaurinParser import MaclaurinParser

# This class defines a complete listener for a parse tree produced by MaclaurinParser.
class MaclaurinListener(ParseTreeListener):

    # Enter a parse tree produced by MaclaurinParser#prog.
    def enterProg(self, ctx:MaclaurinParser.ProgContext):
        pass

    # Exit a parse tree produced by MaclaurinParser#prog.
    def exitProg(self, ctx:MaclaurinParser.ProgContext):
        pass


    # Enter a parse tree produced by MaclaurinParser#expr.
    def enterExpr(self, ctx:MaclaurinParser.ExprContext):
        pass

    # Exit a parse tree produced by MaclaurinParser#expr.
    def exitExpr(self, ctx:MaclaurinParser.ExprContext):
        pass


    # Enter a parse tree produced by MaclaurinParser#numero.
    def enterNumero(self, ctx:MaclaurinParser.NumeroContext):
        pass

    # Exit a parse tree produced by MaclaurinParser#numero.
    def exitNumero(self, ctx:MaclaurinParser.NumeroContext):
        pass



del MaclaurinParser