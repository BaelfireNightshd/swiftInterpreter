#!/usr/bin/env python3

from rply import LexerGenerator

lg = LexerGenerator()


lg.add("SEMICOLON", r";")
lg.add("TRUE", r"true")
lg.add("FALSE", r"false")
lg.add("NIL-LITERAL", r"nil")
lg.add("PLUS", r"\+")
lg.add("MINUS", r"-")
lg.add("BINARY-LITERAL-PREFIX", r"0b")
lg.add("OCTAL-LITERAL-PREFIX", r"0o")
lg.add("HEXADECIMAL-LITERAL-PREFIX", r"0x")
lg.add("BINARY-LITERAL-DIGIT", r"[01]")
lg.add("UNDERSCORE", r"_")
lg.add("OCTAL-LITERAL-DIGIT", r"[0-7]")
lg.add("DECIMAL-LITERAL-DIGIT", r"\d")
lg.add("HEXADECIMAL-LITERAL-DIGIT", r"[0-9a-fA-F]")
lg.add("PERIOD", r"\.")
lg.add("FLOATING-POINT-E", r"[eE]")
lg.add("FLOATING-POINT-P", r"[pP]")


lexer = lg.build()

if __name__ == '__main__':
    #provide ability to test tokenization
    while(True):
        text = input(">")
        for token in lexer.lex(text):
            print(token)
