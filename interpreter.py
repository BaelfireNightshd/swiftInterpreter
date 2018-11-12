#!/usr/bin/env python3

# import parts of the swift language
from swiftLang import *

# import an implementation of the swift standard library
from stdlib.public.core import *

# import regex
import re

class Interpreter:

    variables = {}

    def __init__(self):
        variables = {}

    def run(self, source):
        srcPos = 0
        while (srcPos < len(source)):
            # if we come across a single line comment
            if re.match(r'^//', source[srcPos:]):
                srcPos = lang_whitespace.comment(source, srcPos)
                continue

            # TODO: multiline comments

            # if we come across var creation
            if re.match(r'^var', source[srcPos:]):
                srcPos = lang_variableDeclaration.var(source, srcPos)
                continue

            # TODO: let creation

            if re.match(r'^print\(', source[srcPos:]):
                srcPos = core_print.swiftPrint(source, srcPos, self.variables)
                continue

            print("invalid syntax")
            exit()
