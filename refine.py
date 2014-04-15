#!/usr/bin/env python
import os
import sys

def helper():
    print 'Usage: ./refine.py refineDir originDir'

def createFileList(inputPath):
    f_list = os.listdir(inputPath)
    return f_list
def __main__():
    if len(sys.argv) < 3:
        helper()
        return
    refineDir = sys.argv[1]
    originDir = sys.argv[2]

    refine_list = createFileList(refineDir)
    origin_list = createFileList(originDir)

    for fname in origin_list:
        if not fname.endswith(".jpg"):
            continue
        if fname not in refine_list:
            os.remove(originDir+fname)
            prefix = fname.split('.')[0]
            os.remove(originDir+prefix+'_color.txt')

if __name__ == '__main__':
    __main__()
