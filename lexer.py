#!/usr/bin/env python3

from rply import LexerGenerator

lg = LexerGenerator()

lg.add("WHITESPACE-CHARACTER", r"[\u0000\u0009\u000B\u000C\u0020]")
lg.add("LINE-BREAK", r"\u000D\u000A|\u000A|\u000D")     # U+000A or U+000D or U+000D U+000A
lg.add("COMMENT", r"\/\/.*")                            # //
lg.add("MULTILINE-COMMENT-HEAD", r"\/\*")               # /*
lg.add("MULTILINE-COMMENT-TAIL", r"\*\/")               # */
lg.add("SEMICOLON", r";")
lg.add("TRUE", r"true")
lg.add("FALSE", r"false")
lg.add("NIL-LITERAL", r"nil")
lg.add("BINARY-LITERAL", r"0b[01][01_]*")
lg.add("OCTAL-LITERAL", r"0o[0-7][0-7_]*")
lg.add("HEXADECIMAL-FLOATING-POINT-LITERAL", r"0x[0-9a-fA-F][0-9a-fA-F_]*(\.[0-9a-fA-F][0-9a-fA-F_]*)?[pP][+-]?\d[\d_]*")
lg.add("HEXADECIMAL-LITERAL", r"0x[0-9a-fA-F][0-9a-fA-F_]*")
#   Technically DECIMAL-LITERALS also qualify for DECIMAL-FLOATING-POINT-LITERALS
#   but that creates a conflict between two of the regex, so I will just exclude
#   them from the regex and take care of it in parser.
lg.add("DECIMAL-FLOATING-POINT-LITERAL", r"\d[\d_]*((\.\d[\d_]*[eE][+-]?\d[\d_]*)|(\.\d[\d_]*)|([eE][+-]?\d[\d_]*))")
lg.add("DECIMAL-LITERAL", r"\d[\d_]*")
lg.add("PLUS", r"\+")
lg.add("MINUS", r"-")
lg.add("UNDERSCORE", r"_")
lg.add("PERIOD", r"\.")

# constructing the identifier grammar

regex_identifier_head_options = r"a-zA-Z"
regex_identifier_head_options += r"_"
regex_identifier_head_options += r"\u00A8\u00AA\u00AD\u00AF\u00B2-\u00B5\u00B7-\u00BA"
regex_identifier_head_options += r"\u00BC-\u00BE\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u00FF"
regex_identifier_head_options += r"\u0100-\u02FF\u0370-\u167F\u1681-\u181D\u180F-\u1DBF"
regex_identifier_head_options += r"\u1E00-\u1FFF"
regex_identifier_head_options += r"\u200B-\u200D\u202A-\u202E\u203F-\u2040\u2054\u2060-\u206F"
regex_identifier_head_options += r"\u2070-\u20CF\u2100-\u218F\u2460-\u24FF\u2776-\u2793"
regex_identifier_head_options += r"\u2C00-\u2DFF\u2E80-\u2FFF"
regex_identifier_head_options += r"\u3004-\u3007\u3021-\u302F\u3031-\u303F\u3040-\uD7FF"
regex_identifier_head_options += r"\uF900-\uFD3D\uFD40-\uFDCF\uFDF0-\uFE1F\uFE30-\uFE44"
regex_identifier_head_options += r"\uFE47-\uFFFD"
regex_identifier_head_options += r"\U00010000-\U0001FFFD\U00020000-\U0002FFFD\U00030000-\U0003FFFD\U00040000-\U0004FFFD"
regex_identifier_head_options += r"\U00050000-\U0005FFFD\U00060000-\U0006FFFD\U00070000-\U0007FFFD\U00080000-\U0008FFFD"
regex_identifier_head_options += r"\U00090000-\U0009FFFD\U000A0000-\U000AFFFD\U000B0000-\U000BFFFD\U000C0000-\U000CFFFD"
regex_identifier_head_options += r"\U000D0000-\U000DFFFD\U000E0000-\U000EFFFD"

regex_identifier_character_options = r"0-9"
regex_identifier_character_options += r"\u0300-\u036F\u1DC0-\u1DFF\u20D0-\u20FF\uFE20-\uFE2F"
regex_identifier_character_options += regex_identifier_head_options

regex_identifier_partial_string = "[" + regex_identifier_head_options + "][" + regex_identifier_character_options + "]*"
regex_identifier_string = regex_identifier_partial_string + "|`" + regex_identifier_partial_string + "`"
lg.add("IDENTIFIER", regex_identifier_string)

lexer = lg.build()

if __name__ == '__main__':
    #provide ability to test tokenization
    while(True):
        text = input(">")
        for token in lexer.lex(text):
            print(token)
