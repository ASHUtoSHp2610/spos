%{
#include<stdio.h>
void yyerror();
int yylex();
%}
%token NOUN PRONOUN ADJECTIVE VERB ADVERB CONJUNCTION PREPOSITION NL
%%
sentence: compound NL { printf("COMPOUND SENTENCE\n");}
	|
	simple NL {printf("SIMPLE SENTENCE\n");}
	;
simple: subject VERB object;

compound: subject VERB object CONJUNCTION subject VERB object;

subject: NOUN|PRONOUN;

object: NOUN|ADJECTIVE NOUN|ADVERB NOUN|PREPOSITION NOUN;
%%
void yyerror()
{
printf("ERROR");
}
int main()
{
yyparse();
}

