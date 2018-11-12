#!/usr/bin/env python3

def comment(source, srcPos):
    while (srcPos < len(source)) and (source[srcPos] != '\n'):
        srcPos += 1
    srcPos += 1
    return srcPos
