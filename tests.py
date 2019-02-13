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
        self.assertNotEqual(t.value, "0b")

        stream = lexer.lex("0b_")
        t = stream.next()
        self.assertNotEqual(t.name, "BINARY-LITERAL")
        self.assertNotEqual(t.value, "0b_")

        stream = lexer.lex("0b0")
        t = stream.next()
        self.assertEqual(t.name, "BINARY-LITERAL")
        self.assertEqual(t.value, "0b0")

        stream = lexer.lex("0b1")
        t = stream.next()
        self.assertEqual(t.name, "BINARY-LITERAL")
        self.assertEqual(t.value, "0b1")

        stream = lexer.lex("0b0_")
        t = stream.next()
        self.assertEqual(t.name, "BINARY-LITERAL")
        self.assertEqual(t.value, "0b0_")

        stream = lexer.lex("0b1_")
        t = stream.next()
        self.assertEqual(t.name, "BINARY-LITERAL")
        self.assertEqual(t.value, "0b1_")

        stream = lexer.lex("0b0_1____")
        t = stream.next()
        self.assertEqual(t.name, "BINARY-LITERAL")
        self.assertEqual(t.value, "0b0_1____")

        stream = lexer.lex("0b1_0______")
        t = stream.next()
        self.assertEqual(t.name, "BINARY-LITERAL")
        self.assertEqual(t.value, "0b1_0______")




    def test_octal_literal(self):
        stream = lexer.lex("0o")
        t = stream.next()
        self.assertNotEqual(t.name, "OCTAL-LITERAL")
        self.assertNotEqual(t.value, "0o")

        stream = lexer.lex("0o_")
        t = stream.next()
        self.assertNotEqual(t.name, "OCTAL-LITERAL")
        self.assertNotEqual(t.value, "0o_")

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
        self.assertNotEqual(t.value, "0o8")

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

if __name__ == '__main__':
    unittest.main()
