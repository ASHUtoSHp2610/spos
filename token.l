%{
  #include <stdlib.h>
 
%}

letter [A-Z a-z]
digit [0-9]
identifier {letter}({letter}|{digit})
number {digit}+(\.{digit}+)?
punctuation [;|:|,|.|"|'|()|{}]
operators [+|-|*|=|<|>]
keywords if|else|for|int|while|do|void
literal \".*\"
comment "//".*
headerfile "#".*
multicomment "/*".*"*/"
%%
{headerfile} {printf("\nHeaderfile %s found", yytext);}
{keywords} {printf("\nKeyword %s found", yytext);}
{comment} {printf("\nComment %s found", yytext);}
{multicomment} {printf("\nMulti-line comment %s found", yytext);}
{literal} {printf("\nLiteral %s found", yytext);}
{operators} {printf("\nOperators %s found", yytext);}
{punctuation} {printf("\nPunctuation %s found",yytext);}
{number} {printf("\nNumber %s found", yytext);}
{identifier} {printf("\nIdentifier %s found", yytext);}
%%

int main()
{
yylex(); }

int yywrap()
{
return 1;
}
