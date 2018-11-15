#!/usr/bin/env python3

from rply import ParserGenerator

from ast import *

pg = ParserGenerator([
'SEMICOLON',
'TRUE',
'FALSE',
'NIL-LITERAL',
'PLUS',
'MINUS',
'BINARY-LITERAL-PREFIX',
'BINARY-LITERAL-DIGIT',
'UNDERSCORE',
'OCTAL-LITERAL-PREFIX',
'OCTAL-LITERAL-DIGIT',
'DECIMAL-LITERAL-DIGIT',
'HEXADECIMAL-LITERAL-PREFIX',
'HEXADECIMAL-LITERAL-DIGIT',
'PERIOD',
'FLOATING-POINT-E',
'FLOATING-POINT-P',
], cache_id="swiftLang"
)

@pg.production("main : statements")
def main(s):
    return s[0]



#########################################
#                                       #
#   Lexical Structure                   #
#                                       #
#########################################

# GRAMMAR OF WHITESPACE
# GRAMMAR OF AN IDENTIFIER
# GRAMMAR OF A LITERAL
@pg.production("literal : numeric-literal")
@pg.production("literal : string-literal")
@pg.production("literal : boolean-literal")
@pg.production("literal : NIL-LITERAL")

@pg.production("numeric-literal : integer-literal")
@pg.production("numeric-literal : MINUS integer-literal")
@pg.production("numeric-literal : floating-point-literal")
@pg.production("numeric-literal : MINUS floating-point-literal")

@pg.production("boolean-literal : TRUE")
@pg.production("boolean-literal : FALSE")

# GRAMMAR OF AN INTEGER LITERAL
@pg.production("integer-literal : binary-literal")
@pg.production("integer-literal : octal-literal")
@pg.production("integer-literal : decimal-literal")
@pg.production("integer-literal : hexadecimal-literal")

@pg.production("binary-literal : BINARY-LITERAL-PREFIX BINARY-LITERAL-DIGIT")
@pg.production("binary-literal : BINARY-LITERAL-PREFIX BINARY-LITERAL-DIGIT binary-literal-characters")
# BINARY-DIGIT in lexer
@pg.production("binary-literal-character : BINARY-LITERAL-DIGIT")
@pg.production("binary-literal-character : UNDERSCORE")
@pg.production("binary-literal-characters : binary-literal-character")
@pg.production("binary-literal-characters : binary-literal-character binary-literal-characters")

@pg.production("octal-literal : OCTAL-LITERAL-PREFIX OCTAL-LITERAL-DIGIT")
@pg.production("octal-literal : OCTAL-LITERAL-PREFIX OCTAL-LITERAL-DIGIT octal-literal-characters")
# OCTAL-DIGIT in lexer
@pg.production("octal-literal-character : OCTAL-LITERAL-DIGIT")
@pg.production("octal-literal-character : UNDERSCORE")
@pg.production("octal-literal-characters : octal-literal-character")
@pg.production("octal-literal-characters : octal-literal-character octal-literal-characters")

@pg.production("decimal-literal : DECIMAL-LITERAL-DIGIT")
@pg.production("decimal-literal : DECIMAL-LITERAL-DIGIT decimal-literal-characters")
# DECIMAL-DIGIT in lexer
@pg.production("decimal-literal-digits : DECIMAL-LITERAL-DIGIT")
@pg.production("decimal-literal-digits : DECIMAL-LITERAL-DIGIT decimal-literal-digitis")
@pg.production("decimal-literal-character : DECIMAL-LITERAL-DIGIT")
@pg.production("decimal-literal-character : UNDERSCORE")
@pg.production("decimal-literal-characters : decimal-literal-character")
@pg.production("decimal-literal-characters : decimal-literal-character decimal-literal-characters")

@pg.production("hexadecimal-literal : HEXADECIMAL-LITERAL-PREFIX HEXADECIMAL-LITERAL-DIGIT")
@pg.production("hexadecimal-literal : HEXADECIMAL-LITERAL-PREFIX HEXADECIMAL-LITERAL-DIGIT hexadecimal-literal-characters")
# HEXADECIMAL-DIGIT in lexer
@pg.production("hexadecimal-literal-character : HEXADECIMAL-LITERAL-DIGIT")
@pg.production("hexadecimal-literal-character : UNDERSCORE")
@pg.production("hexadecimal-literal-characters : hexadecimal-literal-character")
@pg.production("hexadecimal-literal-characters : hexadecimal-literal-character hexadecimal-literal-characters")

# GRAMMAR OF A FLOATING-POINT LITERAL
@pg.production("floating-point-literal : decimal-literal")
@pg.production("floating-point-literal : decimal-literal decimal-fraction")
@pg.production("floating-point-literal : decimal-literal decimal-exponent")
@pg.production("floating-point-literal : decimal-literal decimal-fraction decimal-exponent")
@pg.production("floating-point-literal : hexadecimal-literal hexadecimal-exponent")
@pg.production("floating-point-literal : hexadecimal-literal hexadecimal-fraction hexadecimal-exponent")

@pg.production("decimal-fraction : PERIOD decimal-literal")
@pg.production("decimal-exponent : FLOATING-POINT-E decimal-literal")
@pg.production("decimal-exponent : FLOATING-POINT-E sign decimal-literal")

@pg.production("hexadecimal-fraction : PERIOD HEXADECIMAL-LITERAL-DIGIT")
@pg.production("hexadecimal-fraction : PERIOD HEXADECIMAL-LITERAL-DIGIT hexadecimal-literal-characters")
@pg.production("hexadecimal-exponent : FLOATING-POINT-P decimal-literal")
@pg.production("hexadecimal-exponent : FLOATING-POINT-P sign decimal-literal")
#FLOATING-POINT-E in lexer
#FLOATING-POINT-P in lexer
@pg.production("sign : PLUS")
@pg.production("sign : MINUS")

# GRAMMAR OF A STRING LITERAL
# GRAMMAR OF OPERATORS


#########################################
#                                       #
#   Types                               #
#                                       #
#########################################



#########################################
#                                       #
#   Expressions                         #
#                                       #
#########################################

# GRAMMAR OF AN EXPRESSION
# GRAMMAR OF A PREFIX EXPRESSION
# GRAMMAR OF A TRY EXPRESSION
# GRAMMAR OF A BINARY EXPRESSION
# GRAMMAR OF AN ASSIGNMENT OPERATOR
# GRAMMAR OF A CONDITIONAL OPERATOR
# GRAMMAR OF A TYPE-CASTING OPERATOR
# GRAMMAR OF A PRIMARY EXPRESSION
# GRAMMAR OF A LITERAL EXPRESSION
# GRAMMAR OF A SELF EXPRESSION
# GRAMMAR OF A SUPERCLASS EXPRESSION
# GRAMMAR OF A CLOSURE EXPRESSION
# GRAMMAR OF A IMPLICIT MEMBER EXPRESSION
# GRAMMAR OF A PARENTHESIZED EXPRESSION
# GRAMMAR OF A TUPLE EXPRESSION
# GRAMMAR OF A WILDCARD EXPRESSION
# GRAMMAR OF A KEY-PATH EXPRESSION
# GRAMMAR OF A SELECTOR EXPRESSION
# GRAMMAR OF A KEY-PATH STRING EXPRESSION
# GRAMMAR OF A POSTFIX EXPRESSION
# GRAMMAR OF A FUNCTION CALL EXPRESSION
# GRAMMAR OF AN INITIALIZER EXPRESSION
# GRAMMAR OF AN EXPLICIT MEMBER EXPRESSION
# GRAMMAR OF A SELF EXPRESSION
# GRAMMAR OF A SUBSCRIPT EXPRESSION
# GRAMMAR OF A FORCED-VALUE EXPRESSION
# GRAMMAR OF AN OPTIONAL-CHAINING EXPRESSION


#########################################
#                                       #
#   Statements                          #
#                                       #
#########################################

# GRAMMAR OF A STATEMENT

# @pg.production("statement : expression")
# @pg.production("statement : expression SEMICOLON")
#
# @pg.production("statement : declaration")
# @pg.production("statement : declaration SEMICOLON")
#
# @pg.production("statement : loop-statement")
# @pg.production("statement : loop-statement SEMICOLON")
#
# @pg.production("statement : branch-statement")
# @pg.production("statement : branch-statement SEMICOLON")
#
# @pg.production("statement : labeled-statement")
# @pg.production("statement : labeled-statement SEMICOLON")
#
# @pg.production("statement : control-transfer-statement")
# @pg.production("statement : control-transfer-statement SEMICOLON")
#
# @pg.production("statement : defer-statement")
# @pg.production("statement : defer-statement SEMICOLON")
#
# @pg.production("statement : do-statement")
# @pg.production("statement : do-statement SEMICOLON")
#
# @pg.production("statement : compiler-control-statement")
# def statement_compilerControlStatement(s):
#     pass

@pg.production("statements : statement statements")
def statements(s):
    return ast.Block(s[0].getastlist() + [s[1]])

@pg.production("statements : statement")
def statements_statement(s):
    return ast.Block([s[0]])



#########################################
#                                       #
#   Declarations                        #
#                                       #
#########################################



#########################################
#                                       #
#   Attributes                          #
#                                       #
#########################################



#########################################
#                                       #
#   Patterns                            #
#                                       #
#########################################



#########################################
#                                       #
#   Generic Parameters and Arguments    #
#                                       #
#########################################



parser = pg.build()
