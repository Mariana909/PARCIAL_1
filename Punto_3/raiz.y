/* declare tokens */
%token NUMBER
%token ADD SUB MUL DIV RAIZ
%token EOL

%%
calclist:
  | calclist exp EOL { printf("= %d\n", $2); }
  ;

exp: factor
  | exp ADD factor { $$ = $1 + $3; }
  | exp SUB factor { $$ = $1 - $3; }
  ;

factor: raiz
  | factor MUL raiz { $$ = $1 * $3; }
  | factor DIV raiz { if ($3 != 0) { $$ = $1 / $3; }
                      else { yyerror("División por cero"); $$ = 0; } }
  ;

raiz: term
  | RAIZ '(' exp ')' { ; }  
  ;

term: NUMBER
  | '(' exp ')'       { $$ = $2; }
  | '|' exp '|'       { $$ = $2 >= 0 ? $2 : -$2; }
  ;
