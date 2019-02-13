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



if __name__ == '__main__':
    unittest.main()
