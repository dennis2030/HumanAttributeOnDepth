#!/usr/bin/env python
import sys
import random
import collections

def __main__():
    fname = sys.argv[1]
    f = open(fname,'r')
    lines = f.readlines()

    trainDir = 'GT/train/'
    testDir = 'GT/test/'

    prefix = fname.split('/')[-1].split('.')[0]
    f_train = open(trainDir + prefix+'.txt','w')
    f_test = open(testDir + prefix+'.txt','w')

    random_f = open('randomSet.txt','r')

    random_lines = random_f.readlines()
    random_lines = [tmp.strip() for tmp in random_lines] 
    print len(lines)

    for i in range(len(lines)):
        if str(i) in random_lines:
            f_test.write(lines[i])
        else:
            f_train.write(lines[i])

if __name__ == '__main__':
    __main__()
