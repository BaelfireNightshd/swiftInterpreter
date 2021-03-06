#!/usr/bin/env python3

from lexer import lexer
import unittest

class TestLexerWhitespace(unittest.TestCase):

    def test_whitespace_character(self):
        stream = lexer.lex("\u0000")
        t = stream.next()
        self.assertEqual(t.name, "WHITESPACE-CHARACTER")
        self.assertEqual(t.value, '\u0000')

        stream = lexer.lex("\u0009")
        t = stream.next()
        self.assertEqual(t.name, "WHITESPACE-CHARACTER")
        self.assertEqual(t.value, '\u0009')

        stream = lexer.lex("\u000B")
        t = stream.next()
        self.assertEqual(t.name, "WHITESPACE-CHARACTER")
        self.assertEqual(t.value, '\u000B')

        stream = lexer.lex("\u000C")
        t = stream.next()
        self.assertEqual(t.name, "WHITESPACE-CHARACTER")
        self.assertEqual(t.value, '\u000C')

        stream = lexer.lex("\u0020")
        t = stream.next()
        self.assertEqual(t.name, "WHITESPACE-CHARACTER")
        self.assertEqual(t.value, '\u0020')

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

    def test_comment(self):
        testString = "// this is a comment \n// this is another comment"
        stream = lexer.lex(testString)
        t = stream.next()
        self.assertEqual(t.name, "COMMENT")
        self.assertEqual(t.value, "// this is a comment ")
        t = stream.next()
        self.assertEqual(t.name, "LINE-BREAK")
        t = stream.next()
        self.assertEqual(t.name, "COMMENT")
        self.assertEqual(t.value, "// this is another comment")

    def test_multiline_comment_head_and_tail(self):
        stream = lexer.lex("/*")
        t = stream.next()
        self.assertEqual(t.name, "MULTILINE-COMMENT-HEAD")
        self.assertEqual(t.value, "/*")

        stream = lexer.lex("*/")
        t = stream.next()
        self.assertEqual(t.name, "MULTILINE-COMMENT-TAIL")
        self.assertEqual(t.value, "*/")



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

        # stream = lexer.lex("a")
        # t = stream.next()
        # self.assertNotEqual(t.name, "DECIMAL-LITERAL")

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




    def test_hexadecimal_literal(self):
        stream = lexer.lex("0x")
        t = stream.next()
        self.assertNotEqual(t.name, "HEXADECIMAL-LITERAL")

        stream = lexer.lex("0x_")
        t = stream.next()
        self.assertNotEqual(t.name, "HEXADECIMAL-LITERAL")

        stream = lexer.lex("0x0")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0x0")

        stream = lexer.lex("0x1")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0x1")

        stream = lexer.lex("0x2")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0x2")

        stream = lexer.lex("0x3")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0x3")

        stream = lexer.lex("0x4")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0x4")

        stream = lexer.lex("0x5")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0x5")

        stream = lexer.lex("0x6")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0x6")

        stream = lexer.lex("0x7")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0x7")

        stream = lexer.lex("0x8")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0x8")

        stream = lexer.lex("0x9")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0x9")

        stream = lexer.lex("0xa")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0xa")

        stream = lexer.lex("0xb")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0xb")

        stream = lexer.lex("0xc")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0xc")

        stream = lexer.lex("0xd")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0xd")

        stream = lexer.lex("0xe")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0xe")

        stream = lexer.lex("0xf")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0xf")

        stream = lexer.lex("0xA")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0xA")

        stream = lexer.lex("0xB")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0xB")

        stream = lexer.lex("0xC")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0xC")

        stream = lexer.lex("0xD")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0xD")

        stream = lexer.lex("0xE")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0xE")

        stream = lexer.lex("0xF")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0xF")

        stream = lexer.lex("0x0__________")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0x0__________")

        stream = lexer.lex("0x00000000000")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0x00000000000")

        stream = lexer.lex("0x11111111111")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0x11111111111")

        stream = lexer.lex("0x22222222222")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0x22222222222")

        stream = lexer.lex("0x33333333333")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0x33333333333")

        stream = lexer.lex("0x44444444444")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0x44444444444")

        stream = lexer.lex("0x55555555555")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0x55555555555")

        stream = lexer.lex("0x66666666666")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0x66666666666")

        stream = lexer.lex("0x77777777777")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0x77777777777")

        stream = lexer.lex("0x88888888888")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0x88888888888")

        stream = lexer.lex("0x99999999999")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0x99999999999")

        stream = lexer.lex("0xaaaaaaaaaaa")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0xaaaaaaaaaaa")

        stream = lexer.lex("0xbbbbbbbbbbb")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0xbbbbbbbbbbb")

        stream = lexer.lex("0xccccccccccc")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0xccccccccccc")

        stream = lexer.lex("0xddddddddddd")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0xddddddddddd")

        stream = lexer.lex("0xeeeeeeeeeee")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0xeeeeeeeeeee")

        stream = lexer.lex("0xfffffffffff")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0xfffffffffff")

        stream = lexer.lex("0xAAAAAAAAAAA")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0xAAAAAAAAAAA")

        stream = lexer.lex("0xBBBBBBBBBBB")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0xBBBBBBBBBBB")

        stream = lexer.lex("0xCCCCCCCCCCC")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0xCCCCCCCCCCC")

        stream = lexer.lex("0xDDDDDDDDDDD")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0xDDDDDDDDDDD")

        stream = lexer.lex("0xEEEEEEEEEEE")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0xEEEEEEEEEEE")

        stream = lexer.lex("0xFFFFFFFFFFF")
        t = stream.next()
        self.assertEqual(t.name, "HEXADECIMAL-LITERAL")
        self.assertEqual(t.value, "0xFFFFFFFFFFF")



class TestLexerFloatingPointLiteral(unittest.TestCase):

    def test_decimal_floating_point_literal(self):
        stream = lexer.lex("_.0")
        t = stream.next()
        self.assertNotEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")

        stream = lexer.lex("0._")
        t = stream.next()
        self.assertNotEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")

        stream = lexer.lex(".0")
        t = stream.next()
        self.assertNotEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")

        stream = lexer.lex("0.")
        t = stream.next()
        self.assertNotEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")

        stream = lexer.lex("0.0")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "0.0")

        stream = lexer.lex("1.1")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "1.1")

        stream = lexer.lex("2.2")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "2.2")

        stream = lexer.lex("3.3")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "3.3")

        stream = lexer.lex("4.4")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "4.4")

        stream = lexer.lex("5.5")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "5.5")

        stream = lexer.lex("6.6")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "6.6")

        stream = lexer.lex("7.7")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "7.7")

        stream = lexer.lex("8.8")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "8.8")

        stream = lexer.lex("9.9")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "9.9")

        stream = lexer.lex("0_.0_")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "0_.0_")

        stream = lexer.lex("0e0")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "0e0")

        stream = lexer.lex("0e+0")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "0e+0")

        stream = lexer.lex("0e-0")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "0e-0")

        stream = lexer.lex("1e1")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "1e1")

        stream = lexer.lex("2e2")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "2e2")

        stream = lexer.lex("3e3")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "3e3")

        stream = lexer.lex("4e4")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "4e4")

        stream = lexer.lex("5e5")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "5e5")

        stream = lexer.lex("6e6")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "6e6")

        stream = lexer.lex("7e7")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "7e7")

        stream = lexer.lex("8e8")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "8e8")

        stream = lexer.lex("9e9")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "9e9")

        stream = lexer.lex("0E0")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "0E0")

        stream = lexer.lex("0.0e0")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "0.0e0")

        stream = lexer.lex("1.1e1")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "1.1e1")

        stream = lexer.lex("2.2e2")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "2.2e2")

        stream = lexer.lex("3.3e3")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "3.3e3")

        stream = lexer.lex("4.4e4")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "4.4e4")

        stream = lexer.lex("5.5e5")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "5.5e5")

        stream = lexer.lex("6.6e6")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "6.6e6")

        stream = lexer.lex("7.7e7")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "7.7e7")

        stream = lexer.lex("8.8e8")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "8.8e8")

        stream = lexer.lex("9.9e9")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "9.9e9")

        stream = lexer.lex("0.0E0")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "0.0E0")

        stream = lexer.lex("0.0e+0")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "0.0e+0")

        stream = lexer.lex("0.0e-0")
        t = stream.next()
        self.assertEqual(t.name, "DECIMAL-FLOATING-POINT-LITERAL")
        self.assertEqual(t.value, "0.0e-0")

    def test_hexadecimal_floating_point_literal(self):
        goodCharacters = "0123456789abcdefABCDEF"
        goodExponents = "0123456789"
        stream = lexer.lex("0x_.0")
        t = stream.next()
        self.assertNotEqual(t.name, "HEXADECIMAL-FLOATING-POINT-LITERAL")

        stream = lexer.lex("0x0._")
        t = stream.next()
        self.assertNotEqual(t.name, "HEXADECIMAL-FLOATING-POINT-LITERAL")

        stream = lexer.lex("0x.0")
        t = stream.next()
        self.assertNotEqual(t.name, "HEXADECIMAL-FLOATING-POINT-LITERAL")

        stream = lexer.lex("0x0.")
        t = stream.next()
        self.assertNotEqual(t.name, "HEXADECIMAL-FLOATING-POINT-LITERAL")

        stream = lexer.lex("0x_.0p0")
        t = stream.next()
        self.assertNotEqual(t.name, "HEXADECIMAL-FLOATING-POINT-LITERAL")

        stream = lexer.lex("0x0._p0")
        t = stream.next()
        self.assertNotEqual(t.name, "HEXADECIMAL-FLOATING-POINT-LITERAL")

        stream = lexer.lex("0x.0p0")
        t = stream.next()
        self.assertNotEqual(t.name, "HEXADECIMAL-FLOATING-POINT-LITERAL")

        stream = lexer.lex("0x0.p0")
        t = stream.next()
        self.assertNotEqual(t.name, "HEXADECIMAL-FLOATING-POINT-LITERAL")

        for c in goodCharacters:
            for e in goodExponents:
                testString = "0x" + c + "p" + e
                with self.subTest(i=testString):
                    stream = lexer.lex(testString)
                    t = stream.next()
                    self.assertEqual(t.name, "HEXADECIMAL-FLOATING-POINT-LITERAL")
                    self.assertEqual(t.value, testString)

                testString = "0x" + c + "p+" + e
                with self.subTest(i=testString):
                    stream = lexer.lex(testString)
                    t = stream.next()
                    self.assertEqual(t.name, "HEXADECIMAL-FLOATING-POINT-LITERAL")
                    self.assertEqual(t.value, testString)

                testString = "0x" + c + "p-" + e
                with self.subTest(i=testString):
                    stream = lexer.lex(testString)
                    t = stream.next()
                    self.assertEqual(t.name, "HEXADECIMAL-FLOATING-POINT-LITERAL")
                    self.assertEqual(t.value, testString)

                testString = "0x" + c * 2 + "p" + e * 2
                with self.subTest(i=testString):
                    stream = lexer.lex(testString)
                    t = stream.next()
                    self.assertEqual(t.name, "HEXADECIMAL-FLOATING-POINT-LITERAL")
                    self.assertEqual(t.value, testString)

                testString = "0x" + c + "_p" + e + "_"
                with self.subTest(i=testString):
                    stream = lexer.lex(testString)
                    t = stream.next()
                    self.assertEqual(t.name, "HEXADECIMAL-FLOATING-POINT-LITERAL")
                    self.assertEqual(t.value, testString)

                testString = "0x" + c + "P" + e
                with self.subTest(i=testString):
                    stream = lexer.lex(testString)
                    t = stream.next()
                    self.assertEqual(t.name, "HEXADECIMAL-FLOATING-POINT-LITERAL")
                    self.assertEqual(t.value, testString)

                testString = "0x" + c + "." + c + "p" + e
                with self.subTest(i=testString):
                    stream = lexer.lex(testString)
                    t = stream.next()
                    self.assertEqual(t.name, "HEXADECIMAL-FLOATING-POINT-LITERAL")
                    self.assertEqual(t.value, testString)

                testString = "0x" + c * 2 + "." + c * 2 + "p" + e * 2
                with self.subTest(i=testString):
                    stream = lexer.lex(testString)
                    t = stream.next()
                    self.assertEqual(t.name, "HEXADECIMAL-FLOATING-POINT-LITERAL")
                    self.assertEqual(t.value, testString)

                testString = "0x" + c + "_." + c + "_p" + e + "_"
                with self.subTest(i=testString):
                    stream = lexer.lex(testString)
                    t = stream.next()
                    self.assertEqual(t.name, "HEXADECIMAL-FLOATING-POINT-LITERAL")
                    self.assertEqual(t.value, testString)

if __name__ == '__main__':
    unittest.main()
