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

if __name__ == '__main__':
    unittest.main()
