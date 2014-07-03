#!/usr/bin/env python
import sys

def __main__():

    fname = sys.argv[1]
    f = open(fname,'r')
    lines = f.readlines()

    for line in lines:
        tmp_list = line.split(' ')
        tmp_list = tmp_list[1:-1]
        line_list = []
        for tmp in tmp_list:
            seg_list = tmp.strip().split(':')
            value = seg_list[1]
            line_list.append(value)
        result = line_list[0]
        for tmp in line_list[1:-1]:
            result += ',' + tmp
        print result


if __name__ == '__main__':
    __main__()

