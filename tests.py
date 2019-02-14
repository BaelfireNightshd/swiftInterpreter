#!/usr/bin/env python3

from lexer import lexer
import unittest

class TestLexerWhitespace(unittest.TestCase):

    def test_line_break(self):
        stream = lexer.lex("\u000a")
        t = stream.next()
        self.assertEqual(t.name, "LINE-BREAK")
        self.assertEqual(t.value, '\u000a')

        stream = lexer.lex("\u000d")
        t = stream.next()
        self.assertEqual(t.name, "LINE-BREAK")
        self.assertEqual(t.value, '\u000d')

        stream = lexer.lex("\u000d\u000a")
        t = stream.next()
        self.assertEqual(t.name, "LINE-BREAK")
        self.assertEqual(t.value, "\u000d\u000a")




class TestLexerIntegerLiteral(unittest.TestCase):

    def test_binary_literal(self):
        stream = lexer.lex("0b")
        t = stream.next()
        self.assertNotEqual(t.name, "BINARY-LITERAL")

        stream = lexer.lex("0b_")
        t = stream.next()
        self.assertNotEqual(t.name, "BINARY-LITERAL")

        stream = lexer.lex("0b0")
        t = stream.next()
        self.assertEqual(t.name, "BINARY-LITERAL")
        self.assertEqual(t.value, "0b0")

        stream = lexer.lex("0b1")
        t = stream.next()
        self.assertEqual(t.name, "BINARY-LITERAL")
        self.assertEqual(t.value, "0b1")

        stream = lexer.lex("0b2")
        t = stream.next()
        self.assertNotEqual(t.name, "BINARY-LITERAL")

        stream = lexer.lex("0ba")
        t = stream.next()
        self.assertNotEqual(t.name, "BINARY-LITERAL")

        stream = lexer.lex("0b0__________")
        t = stream.next()
        self.assertEqual(t.name, "BINARY-LITERAL")
        self.assertEqual(t.value, "0b0__________")

        stream = lexer.lex("0b00000000000")
        t = stream.next()
        self.assertEqual(t.name, "BINARY-LITERAL")
        self.assertEqual(t.value, "0b00000000000")

        stream = lexer.lex("0b11111111111")
        t = stream.next()
        self.assertEqual(t.name, "BINARY-LITERAL")
        self.assertEqual(t.value, "0b11111111111")




    def test_octal_literal(self):
        stream = lexer.lex("0o")
        t = stream.next()
        self.assertNotEqual(t.name, "OCTAL-LITERAL")

        stream = lexer.lex("0o_")
        t = stream.next()
        self.assertNotEqual(t.name, "OCTAL-LITERAL")

        stream = lexer.lex("0o0")
        t = stream.next()
        self.assertEqual(t.name, "OCTAL-LITERAL")
        self.assertEqual(t.value, "0o0")

        stream = lexer.lex("0o1")
        t = stream.next()
        self.assertEqual(t.name, "OCTAL-LITERAL")
        self.assertEqual(t.value, "0o1")

        stream = lexer.lex("0o2")
        t = stream.next()
        self.assertEqual(t.name, "OCTAL-LITERAL")
        self.assertEqual(t.value, "0o2")

        stream = lexer.lex("0o3")
        t = stream.next()
        self.assertEqual(t.name, "OCTAL-LITERAL")
        self.assertEqual(t.value, "0o3")

        stream = lexer.lex("0o4")
        t = stream.next()
        self.assertEqual(t.name, "OCTAL-LITERAL")
        self.assertEqual(t.value, "0o4")

        stream = lexer.lex("0o5")
        t = stream.next()
        self.assertEqual(t.name, "OCTAL-LITERAL")
        self.assertEqual(t.value, "0o5")

        stream = lexer.lex("0o6")
        t = stream.next()
        self.assertEqual(t.name, "OCTAL-LITERAL")
        self.assertEqual(t.value, "0o6")

        stream = lexer.lex("0o7")
        t = stream.next()
        self.assertEqual(t.name, "OCTAL-LITERAL")
        self.assertEqual(t.value, "0o7")

        stream = lexer.lex("0o8")
        t = stream.next()
        self.assertNotEqual(t.name, "OCTAL-LITERAL")

        stream = lexer.lex("0oa")
        t = stream.next()
        self.assertNotEqual(t.name, "OCTAL-LITERAL")

        stream = lexer.lex("0o0__________")
        t = stream.next()
        self.assertEqual(t.name, "OCTAL-LITERAL")
        self.assertEqual(t.value, "0o0__________")

        stream = lexer.lex("0o00000000000")
        t = stream.next()
        self.assertEqual(t.name, "OCTAL-LITERAL")
        self.assertEqual(t.value, "0o00000000000")

        stream = lexer.lex("0o11111111111")
        t = stream.next()
        self.assertEqual(t.name, "OCTAL-LITERAL")
        self.assertEqual(t.value, "0o11111111111")

        stream = lexer.lex("0o22222222222")
        t = stream.next()
        self.assertEqual(t.name, "OCTAL-LITERAL")
        self.assertEqual(t.value, "0o22222222222")

        stream = lexer.lex("0o33333333333")
        t = stream.next()
        self.assertEqual(t.name, "OCTAL-LITERAL")
        self.assertEqual(t.value, "0o33333333333")

        stream = lexer.lex("0o44444444444")
        t = stream.next()
        self.assertEqual(t.name, "OCTAL-LITERAL")
        self.assertEqual(t.value, "0o44444444444")

        stream = lexer.lex("0o55555555555")
        t = stream.next()
        self.assertEqual(t.name, "OCTAL-LITERAL")
        self.assertEqual(t.value, "0o55555555555")

        stream = lexer.lex("0o66666666666")
        t = stream.next()
        self.assertEqual(t.name, "OCTAL-LITERAL")
        self.assertEqual(t.value, "0o66666666666")

        stream = lexer.lex("0o77777777777")
        t = stream.next()
        self.assertEqual(t.name, "OCTAL-LITERAL")
        self.assertEqual(t.value, "0o77777777777")




    def test_decimal_literal(self):
        stream = lexer.lex("_")
        t = stream.next()
        self.assertNotEqual(t.name, "DECIMAL-LITERAL")

        stream = lexer.lex("_0")
        t = stream.next()
        self.assertNotEqual(t.name, "DECIMAL-LITERAL")

        stream = lexer.lex("0")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-LITERAL")
        self.assertEqual(t.value, "0")

        stream = lexer.lex("1")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-LITERAL")
        self.assertEqual(t.value, "1")

        stream = lexer.lex("2")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-LITERAL")
        self.assertEqual(t.value, "2")

        stream = lexer.lex("3")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-LITERAL")
        self.assertEqual(t.value, "3")

        stream = lexer.lex("4")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-LITERAL")
        self.assertEqual(t.value, "4")

        stream = lexer.lex("5")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-LITERAL")
        self.assertEqual(t.value, "5")

        stream = lexer.lex("6")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-LITERAL")
        self.assertEqual(t.value, "6")

        stream = lexer.lex("7")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-LITERAL")
        self.assertEqual(t.value, "7")

        stream = lexer.lex("8")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-LITERAL")
        self.assertEqual(t.value, "8")

        stream = lexer.lex("9")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-LITERAL")
        self.assertEqual(t.value, "9")

        stream = lexer.lex("a")
        t = stream.next()
        self.assertNotEqual(t.name, "DECIMAL-LITERAL")

        stream = lexer.lex("0__________")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-LITERAL")
        self.assertEqual(t.value, "0__________")

        stream = lexer.lex("00000000000")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-LITERAL")
        self.assertEqual(t.value, "00000000000")

        stream = lexer.lex("11111111111")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-LITERAL")
        self.assertEqual(t.value, "11111111111")

        stream = lexer.lex("22222222222")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-LITERAL")
        self.assertEqual(t.value, "22222222222")

        stream = lexer.lex("33333333333")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-LITERAL")
        self.assertEqual(t.value, "33333333333")

        stream = lexer.lex("44444444444")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-LITERAL")
        self.assertEqual(t.value, "44444444444")

        stream = lexer.lex("55555555555")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-LITERAL")
        self.assertEqual(t.value, "55555555555")

        stream = lexer.lex("66666666666")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-LITERAL")
        self.assertEqual(t.value, "66666666666")

        stream = lexer.lex("77777777777")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-LITERAL")
        self.assertEqual(t.value, "77777777777")

        stream = lexer.lex("88888888888")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-LITERAL")
        self.assertEqual(t.value, "88888888888")

        stream = lexer.lex("99999999999")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-LITERAL")
        self.assertEqual(t.value, "99999999999")

if __name__ == '__main__':
    unittest.main()
