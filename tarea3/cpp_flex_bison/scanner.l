%option c++
%option noyywrap
 
%{
#include <sstream>
#include <cstdlib>
#include "parser.h"
using namespace std;
%}
 
DIGIT   [0-9]
DIGIT1  [1-9]
 
%%
 
{DIGIT1}{DIGIT}*  {
                   cout << "Lexer: " << yytext << endl;
                   return Parser::NUMBER;
                  }
 
.                 {
                   return Parser::UNKNOWN;
                  }
 
<<EOF>>           {
                   yyterminate();
                  }
%%