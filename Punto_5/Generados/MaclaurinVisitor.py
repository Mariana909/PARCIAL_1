# Generated from Maclaurin.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MaclaurinParser import MaclaurinParser
else:
    from MaclaurinParser import MaclaurinParser

# This class defines a complete generic visitor for a parse tree produced by MaclaurinParser.

class MaclaurinVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MaclaurinParser#prog.
    def visitProg(self, ctx:MaclaurinParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaclaurinParser#expr.
    def visitExpr(self, ctx:MaclaurinParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaclaurinParser#numero.
    def visitNumero(self, ctx:MaclaurinParser.NumeroContext):
        return self.visitChildren(ctx)



del MaclaurinParser