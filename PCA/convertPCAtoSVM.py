#!/usr/bin/env python

import sys

def __main__():
    fname = sys.argv[1]

    f = open(fname,'r')

    lines = f.readlines()

    for i in range(0,len(lines)):
        line = lines[i]
        tmpS = ""
        tmp_list = line.strip().split(',')
        for j in range(0,len(tmp_list)):
            tmpS += str(j+1)+':'+tmp_list[j] + ' '
        print tmpS
            

if __name__ == '__main__':
    __main__()
