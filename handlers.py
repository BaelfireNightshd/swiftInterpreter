#!/usr/bin/env python3

class Handlers:

    def comment(source, srcPos):
        while (srcPos < len(source)) and (source[srcPos] != '\n'):
            srcPos += 1
        srcPos += 1
        return srcPos

    # TODO: unstub var creation.
    def var(source, srcPos):
        pass

    def swiftPrint(source, srcPos, variables):
        # move srcPos past print(
        srcPos += 6

        
