grammar Anatomy;

ID:[a-zA-Z_][a-zA-Z0-9_]*;
TYPE: 'entero'|'flotante';
BOL: 'Negativo'|'Positivo';
NEWLINE: '\r'? '\n' ;
TK_PAR_IZQ: '(';
TK_PAR_DER: ')';
TK_CORCHETE_IZQ: '[';
TK_CORCHETE_DER: ']';
TK_LLAVE_IZQ: '{';
TK_LLAVE_DER: '}';
TK_DOS_PUNTOS: ':';
SQRT: 'math.sqrt';
STR: '"' (~["])* '"';
COMENTARIO: '/*'  ~[\n]* -> skip ;
FLOAT_LITERAL: [0-9]* '.' [0-9]+;
IMAGINARY_LITERAL: [0-9]+('j'|'i')
	| [0-9]* '.' [0-9]+('j'|'i');
INTEGER_LITERAL: [0-9]+;
HEX :   '0x' [a-fA-F0-9]+ ; //lo devuelve como num decimal
LINE_JOIN: '\\';
EXPONENT: [0-9]+ [eE] [-+]? [0-9]+;
OPERADOR_SUMA: '+';
OPERADOR_RESTA: '-';
OPERADOR_MULTIPLICACION: '*';
OPERADOR_DIVISION: '/';
OPERADOR_DIVISION_ENTERA: '//';
OPERADOR_ARROBA: '@';
OPERADOR_LEFT_SHIFT: '<<';
Tk_Menor_Que: '<';
OPERADOR_RIGHT_SHIFT: '>>';
Tk_Mayor_Que: '>';
OPERADOR_WALRUS: ':=';
OPERADOR_MODULO: '%';
OPERADOR_POTENCIA: '**';
OPERADOR_IGUAL: '==';
TK_ASIGN: '=';
OPERADOR_DIFERENTE: '!=';
OPERADOR_MENOR_IGUAL: '<=';
OPERADOR_MAYOR_IGUAL: '>=';
OPERADOR_DISTINTO: '<>';
OPERADOR_AND: '&';
OPERADOR_OR: '|';
OPERADOR_Negacion: '!';
COMMA: ',';
SEMICOLON: ';';
OPERADOR_DOUBLE_COLON: '::';
DOT: '.';
FLECHA: '->';
OPERADOR_BACKTICK: '\'' '\'';
TK_INVERT: '~';
TK_XOR: '^';
TK_SUMA_IN_PLACE: '+=';
TK_RESTA_IN_PLACE: '-=';
TK_MULT_IN_PLACE: '*=';
TK_DIV_IN_PLACE: '/=';
TK_DIV_ENTERA_IN_PLACE: '//=';
TK_MODULO_IN_PLACE: '%=';
TK_MATRIX_IN_PLACE: '@=';
TK_AND_IN_PLACE: '&=';
TK_OR_IN_PLACE: '|=';
TK_XOR_IN_PLACE: '^=';
TK_RIGHT_IN_PLACE: '>>=';
TK_LEFT_IN_PLACE: '<<=';
TK_EXP_IN_PLACE: '**=';
WS  :   [ \t]+ -> skip ; 



program: stat+ ;

stat:	expr NEWLINE		                                        #expression
     |  assignment NEWLINE                                          # statement
     |  print NEWLINE                                               # show
     |  structureControl NEWLINE                                    # control
     |  functionProc NEWLINE                                        # function
     |  fileOperation NEWLINE                                       # fileOp
     |  NEWLINE                                                     # blank
    ;
    
assignment: ID '=' (expr|reading)	#assign;

functionProc : 'funcion' ID '(' parametros ')' '{' stat*  '}'       # functionStatement;

parametros : 
           | ID (',' ID)* 
           ;
           
args  : 
      | expr (',' expr)* 
      ;

structureControl  : ifStatement      
                  | whileStatement   
                  | forStatement
                  ;

ifStatement: 'evaluar' '(' exprL ')' '{' stat* '}'                  # if
           | 'evaluar' '(' exprL ')' '{' stat* '}' NEWLINE 'evaluar_denuevo' '{' stat* '}' # ifElse 
           ;
whileStatement : 'receta' '(' exprL ')' '{' stat* '}'               # while
           ;

forStatement : 'monitoreo' '(' assignment ';' exprL ';' assignment ')' '{' stat* '}' # for
           ;

print : ID '=' 'leer(' TYPE  ')'                                    # read
      | 'preescripcion(' (|expr (',' expr)*) ')'                    # printExpr
      | 'graficas' graphType '(' graphParams ')'                    # graph
      ; 

graphType: 'barras_pensalas'
         | 'linea'
         | 'scatter'
         | 'histograma'
         ;

graphParams:  ID (|','  ID) (|',' STR (|',' INTEGER_LITERAL) );
      
fileOperation: 'abrir(' ID ',' STR ')'                              # openFile
             | 'cerrar(' ID ')'                                     # closeFile
             | 'escribir(' ID ',' STR ')'                           # writeFile
             | 'borrar(' ID ')'                                     # deleteFile
             | reading                                              # readingFile
             ;
             
reading: 'leerLinea(' ID ',' (INTEGER_LITERAL|exprA) ')'   # readLine
       | 'leerTodo(' ID ')'                                         # readAll
       ;
      
expr: exprL                                                         # Logic
    | exprA                                                         # Aritmetic
    | 'emitir' expr                                                 # return
    ;


exprL: exprL op=('&' | '|') exprL                                   # andOr
     | '!' exprL                                                    # negation
     | exprA op=('<<' | '<=') exprA                                 # minor
     | exprA op=('>>' | '>=') exprA                                 # greater
     | exprA '==' exprA                                             # equals
     | exprL '==' exprL                                             # equalsL
     |   '(' exprL ')'                                              # parensL
     | BOL                                                          # bool
     | ID                                                           # idL
     ;

exprA:  'Punto(' exprA ',' exprA ')'                                # dot
    |   'Cruz(' exprA ',' exprA ')'                                 # cross
    |   'Inversa(' exprA ')'                                        # reverse
    |   'Transpuesta(' exprA ')'                                    # transpose
    |   '-' exprA                                                   # negative
    |   exprA '^' exprA                                             # power
    |   'raiz(' exprA ',' INTEGER_LITERAL ')'                       # rooti
    |   'raiz(' exprA')'                                            # root
    |   exprA op=('%'|'//') exprA                                   # modDivent
    |   exprA op=('*'|'/') exprA                                    # mulDiv
    |   exprA op=('+'|'-') exprA                                    # addSub
    |   trigFunc                                                    # trigFunction
    |   '|' exprA '|'		                                        # abs
    |   ID '(' args ')'                                             # functionCall
    |   INTEGER_LITERAL                                             # int
    |   'entero(' exprA ')'                                         # castInt
    |   FLOAT_LITERAL                                               # float
    |   complex                                                     # comp
    |   ID                                                          # id
    |   HEX			                                                # hex
    |   STR                                                         # str
    |   exprA '.separar()'                                          # split
    |   dataFrame                                                   # dfAssign
    |   array                                                       # arrayAssign
    |   dict                                                        # dictAssign
    |   list                                                        # listAssign
    |   '(' exprA ')'                                               # parens
    ;


list: '[' ( | expr (',' expr)* ) ']'                                # lists
    | ID '.agregar(' expr ')'                                       # listAppend
    | ID ('[' exprA ']')+                                           # listElement
    | ID ('[' exprA ']')+ '=' expr                                  # listElementassign
    | ID '.indice(' expr ')'                                        # listIndex
    | ID '.tam()'                                                   # listLen
    | ID '.borrar(' expr ')'                                        # listRemove
    | ID '.eliminar()'                                              # listClear
    | ID                                                            # listId
    ;

dict: '{' ( | dictItem (',' dictItem)* ) '}'                        # dicts
    | ID '[' expr ']'                                               # dictElement
    | ID '[' expr ']' '=' expr                                      # dictElementassign
    | ID '.llaves()'                                                # dictKeys
    | ID '.valores()'                                               # dictValues
    | ID '.actualizar(' dict ')'                                    # dictUpdate
    ;

dictItem: expr ':' expr                  
    ;
    
array: 'tag(' exprA ')'                  # arrays
     | 'arr.' ID '[' INTEGER_LITERAL (',' INTEGER_LITERAL)* ']'     # arrayElement    
     ;


dataFrame: 'mc(' (list | dict | ID) ')'                             # createDataFrame
         | 'cargarCSV(' STR ')'                                     # loadCSV
         | ID '.guardarCSV(' STR ')'                                # saveCSV
         | column                                                   # columnDataFrame
         | ID '.fila(' INTEGER_LITERAL ')'                          # selectRow
         | ID '.filtrar(' filter ')'                                # filterRows
         | ID '.agregarColumna(' STR ',' expr ')'                   # addColumn
         | ID '.eliminarColumna(' STR ')'                           # dropColumn
         | ID '.descripcion()'                                      # describeDataFrame
         | ID '.cabeza(' INTEGER_LITERAL ')'                        # headDataFrame
         | ID '.unir(' ID ',' STR ')'                               # mergeDataFrames
         ;

column: ID '.columna(' (STR | ID) ')'                               # selectColumn;
         
filter: filter op=('&' | '|') filter                                # andOrF
      | column op=('<<' | '<=') exprA                               # minorF
      | column op=('>>' | '>=') exprA                               # greaterF
      | column '==' exprA                                           # equalsF
      |   '(' filter ')'                                            # parensF
      ;

complex: INTEGER_LITERAL op=('+'|'-') IMAGINARY_LITERAL             # complejo
       | IMAGINARY_LITERAL                                          # img
       ;

trigFunc : 'cos(' exprA ')'                                         # CosFunc
         | 'sen(' exprA ')'                                         # SenFunc
         | 'tan(' exprA ')'                                         # TanFunc
         ;


