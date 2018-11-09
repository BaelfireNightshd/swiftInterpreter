#!/usr/bin/env python3

from handlers import Handlers
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
                srcPos = Handlers.comment(source, srcPos)
                continue

            # TODO: multiline comments

            # if we come across var creation
            if re.match(r'^var', source[srcPos:]):
                srcPos = Handlers.var(source, srcPos)
                continue

            # TODO: let creation

            if re.match(r'^print\(', source[srcPos:]):
                srcPos = Handlers.swiftPrint(source, srcPos, self.variables)
                continue

            print("invalid syntax")
            exit()
