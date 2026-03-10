%{
#include <stdio.h>
int yylex();
void yyerror(char *s);
extern FILE *yyin;  /* Variable que Flex usa para la entrada */
%}
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
  | RAIZ '(' exp ')' {
      double x = $3 / 2.0;
      double tolerancia = 1e-10;
      double x_nuevo = x;
      for (int i = 0; i < 1000; i++) {
          x_nuevo = 0.5 * (x + $3 / x);
          double diff = x_nuevo - x;
          double t = diff >=  0 ? diff : -diff;
          if (t < tolerancia) break;
          x = x_nuevo;
      }
      $$ = (int)x_nuevo;
  }
  ;

term: NUMBER
  | '(' exp ')'       { $$ = $2; }
  | '|' exp '|'       { $$ = $2 >= 0 ? $2 : -$2; }
  ;
%%
int main(int argc, char **argv) {
    if (argc > 1) {
        /* Si hay argumento, abrir el archivo */
        yyin = fopen(argv[1], "r");
        if (!yyin) {
            fprintf(stderr, "Error: No se puede abrir el archivo '%s'\n", argv[1]);
            return 1;
        }
        printf("Procesando archivo: %s\n\n", argv[1]);
    } else {
        /* Si no hay argumento, usar entrada estándar */
        printf("Calculadora con raiz - Ctrl+D para salir\n");
        yyin = stdin;
    }
    
    yyparse();
    
    if (yyin != stdin) {
        fclose(yyin);
    }
    
    return 0;
}

void yyerror(char *s) {
    fprintf(stderr, "Error: %s\n", s);
}
