# Generated from Maclaurin.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,22,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,2,3,2,18,8,2,1,2,1,2,1,2,0,0,3,0,2,4,0,1,1,0,5,6,19,0,
        6,1,0,0,0,2,9,1,0,0,0,4,17,1,0,0,0,6,7,3,2,1,0,7,8,5,0,0,1,8,1,1,
        0,0,0,9,10,5,4,0,0,10,11,5,1,0,0,11,12,3,4,2,0,12,13,5,2,0,0,13,
        14,5,6,0,0,14,15,5,3,0,0,15,3,1,0,0,0,16,18,5,7,0,0,17,16,1,0,0,
        0,17,18,1,0,0,0,18,19,1,0,0,0,19,20,7,0,0,0,20,5,1,0,0,0,1,17
    ]

class MaclaurinParser ( Parser ):

    grammarFileName = "Maclaurin.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "EXP", "DECIMAL", "ENTERO", "SIGNO", "WS" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_numero = 2

    ruleNames =  [ "prog", "expr", "numero" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    EXP=4
    DECIMAL=5
    ENTERO=6
    SIGNO=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MaclaurinParser.ExprContext,0)


        def EOF(self):
            return self.getToken(MaclaurinParser.EOF, 0)

        def getRuleIndex(self):
            return MaclaurinParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = MaclaurinParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.expr()
            self.state = 7
            self.match(MaclaurinParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.n = None # Token

        def EXP(self):
            return self.getToken(MaclaurinParser.EXP, 0)

        def numero(self):
            return self.getTypedRuleContext(MaclaurinParser.NumeroContext,0)


        def ENTERO(self):
            return self.getToken(MaclaurinParser.ENTERO, 0)

        def getRuleIndex(self):
            return MaclaurinParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MaclaurinParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self.match(MaclaurinParser.EXP)
            self.state = 10
            self.match(MaclaurinParser.T__0)
            self.state = 11
            self.numero()
            self.state = 12
            self.match(MaclaurinParser.T__1)
            self.state = 13
            localctx.n = self.match(MaclaurinParser.ENTERO)
            self.state = 14
            self.match(MaclaurinParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumeroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTERO(self):
            return self.getToken(MaclaurinParser.ENTERO, 0)

        def DECIMAL(self):
            return self.getToken(MaclaurinParser.DECIMAL, 0)

        def SIGNO(self):
            return self.getToken(MaclaurinParser.SIGNO, 0)

        def getRuleIndex(self):
            return MaclaurinParser.RULE_numero

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumero" ):
                listener.enterNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumero" ):
                listener.exitNumero(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)




    def numero(self):

        localctx = MaclaurinParser.NumeroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_numero)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 16
                self.match(MaclaurinParser.SIGNO)


            self.state = 19
            _la = self._input.LA(1)
            if not(_la==5 or _la==6):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





