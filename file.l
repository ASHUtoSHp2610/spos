%{
  #include<stdio.h>
  #include "y.tab.h"
%}
verb am|is|are|have|has|can|will|shall|eat|sing|go|goes|be|play
adverb very|simply|gently|calmly
preposition in|on|to|from|above|behind|before
conjuction and|or|also|so|but|if|then
adjective fast|good|honest|their|my|your|its|her|his
pronoun I|he|she|we|they|you|this
noun [A-Za-z]+
%%
{verb} return VERB;
{adverb} return ADVERB; 
{preposition} return PREPOSITION;
{conjuction} return CONJUNCTION;
{adjective} return ADJECTIVE;
{pronoun} return PRONOUN;
{noun} return NOUN;
"\n" return NL; 
%%
int yywrap()
{
 return 1;
}
