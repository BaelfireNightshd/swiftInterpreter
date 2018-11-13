#!/usr/bin/env python3

from rply import LexerGenerator

lg = LexerGenerator()


lg.add("SEMICOLON", r";")
lg.add("TRUE", r"true")
lg.add("FALSE", r"false")
lg.add("NIL-LITERAL", r"nil")
lg.add("BINARY-LITERAL", r"0b[01][01_]*")
lg.add("OCTAL-LITERAL", r"0o[0-7][0-7_]*")
lg.add("DECIMAL-LITERAL", r"\d[\d_]*")
lg.add("HEXADECIMAL-LITERAL", r"0x[0-9a-fA-F][0-9a-fA-F_]*")


lexer = lg.build()
