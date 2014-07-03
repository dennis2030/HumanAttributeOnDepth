#!/usr/bin/env python
import os
import sys

def helper():
    print 'Usage: ./refine_depth.py colorDir depthDir'

def createFileList(inputPath):
    f_list = os.listdir(inputPath)
    return f_list

def convertToPrefix(inputList):
    prefix_list = []
    for element in inputList:
        prefix = element.split('.')[0]
        prefix_list.append(prefix)
    return prefix_list


def __main__():

    if len(sys.argv) <3:
        helper()
        return

    colorDir = sys.argv[1]
    depthDir = sys.argv[2]
    
        
    color_list = createFileList(colorDir)
    color_list = convertToPrefix(color_list)
    depth_list = createFileList(depthDir)

    for fname in depth_list:
        prefix = fname.split('.')[0]
        prefix = prefix.split('_')[0]
        if prefix not in color_list:
            os.remove(depthDir+fname)
 
if __name__ == '__main__':
    __main__()
