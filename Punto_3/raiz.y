/* simplest version of calculator */
%{
#include <stdio.h>
%}
/* declare tokens */
%token NUMBER
%token ADD SUB MUL DIV ABS
%token EOL
%%
calclist: /* nothing */                       
 | calclist exp EOL { printf("= %d\n", $2); } /* EOL is end of an expression */
 ;
exp: factor       
 | exp ADD factor { $$ = $1 + $3; }
 | exp SUB factor { $$ = $1 - $3; }
 ;
factor: term       
 | factor MUL term { $$ = $1 * $3; }
 | factor DIV term { if ($3 != 0 ) { $$ = $1 / $3;
         } else { 
            yyerror("División por cero");
            $$ = 0;
           }  }
 ;
term: NUMBER  
 | NOT term   { $$ = ~$2; }
 | '(' orbit ')' { $$ = $2; }
 | '|' orbit '|'  { $$ = $2 >= 0? $2 : - $2; }
;
%%
int main(int argc, char **argv)
{
  yyparse();
}
yyerror(char *s)
{
  fprintf(stderr, "error: %s\n", s);
}
