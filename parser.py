#!/usr/bin/env python3

from rply import ParserGenerator

from ast import *

pg = ParserGenerator([
'SEMICOLON',
'TRUE',
'FALSE',
'NIL-LITERAL'
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
@pg.production("numeric-literal : floating-point-literal")

@pg.production("boolean-literal : TRUE")
@pg.production("boolean-literal : FALSE")

# GRAMMAR OF AN INTEGER LITERAL
@pg.production("integer-literal : BINARY-LITERAL")
@pg.production("integer-literal : OCTAL-LITERAL")
@pg.production("integer-literal : DECIMAL-LITERAL")
@pg.production("integer-literal : HEXADECIMAL-LITERAL")

# GRAMMAR OF A FLOATING-POINT LITERAL
@pg.production("floating-point-literal : ")

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
