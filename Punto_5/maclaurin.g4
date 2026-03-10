grammar Maclaurin;

// ─── PARSER ───
prog   : expr EOF ;
expr   : EXP '(' numero ',' ENTERO ')' ;
numero : SIGNO? (ENTERO | DECIMAL) ;

// ─── LÉXICO ───
EXP     : 'EXP' | 'exp' ;
DECIMAL : [0-9]+ '.' [0-9]+ ;
ENTERO  : [0-9]+ ;
SIGNO   : [+\-] ;
WS      : [ \t\n\r]+ -> skip ;
