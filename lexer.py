#!/usr/bin/env python3

from rply import LexerGenerator

lg = LexerGenerator()


lg.add("SEMICOLON", r";")
lg.add("TRUE", r"true")
lg.add("FALSE", r"false")
lg.add("NIL-LITERAL", r"nil")
lg.add("BINARY-LITERAL-PREFIX", r"0b")
lg.add("BINARY-LITERAL-DIGIT", r"[01]")
lg.add("UNDERSCORE", r"_")
lg.add("OCTAL-LITERAL-PREFIX", r"0o")
lg.add("OCTAL-LITERAL-DIGIT", r"[0-7]")
lg.add("DECIMAL-LITERAL-DIGIT", r"\d")
lg.add("HEXADECIMAL-LITERAL-PREFIX", r"0x")
lg.add("HEXADECIMAL-LITERAL-DIGIT", r"[0-9a-fA-F]")


lexer = lg.build()
