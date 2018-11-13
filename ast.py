#!/usr/bin/env python3

from rply.token import BaseBox

class Block(BaseBox):
    def __init__(self, statements):
        self.statements = statements
