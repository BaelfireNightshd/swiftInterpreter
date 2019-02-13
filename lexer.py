#!/usr/bin/env python3

from rply import LexerGenerator

lg = LexerGenerator()

lg.add("LINE-BREAK", r"\u000D\u000A|\u000A|\u000D")     # U+000A or U+000D or U+000D U+000A
lg.add("SEMICOLON", r";")
lg.add("TRUE", r"true")
lg.add("FALSE", r"false")
lg.add("NIL-LITERAL", r"nil")
lg.add("BINARY-LITERAL", r"0b[01][01_]*")
lg.add("OCTAL-LITERAL", r"0o[0-7][0-7_]*")
lg.add("HEXADECIMAL-LITERAL", r"0x[0-9a-fA-F][0-9a-fA-F_]*")
lg.add("DECIMAL-LITERAL", r"\d[\d_]*")
lg.add("PLUS", r"\+")
lg.add("MINUS", r"-")
lg.add("UNDERSCORE", r"_")
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
