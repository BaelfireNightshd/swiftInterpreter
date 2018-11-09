#!/usr/bin/env python3

import os
import sys
from interpreter import Interpreter

interp = Interpreter()

def repl():
    print("Starting Swift REPL.")
    source = input(">")
    interp.run(source)
    pass

def run():
    pass

if __name__ == '__main__':
    if len(sys.argv) < 2:
        repl()
    else:
        run()
