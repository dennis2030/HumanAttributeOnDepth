#!/usr/bin/env python
import sys
import random
import collections

def Usage():
    print './genRandom.py num'
    print 'It would generate a random set in range 0 ~ num'
    print 'Total number of generate int is num/5'

def __main__():
    
    # if no argument, print usage for user
    if len(sys.argv) < 2:
        Usage()
        return

    num = int(sys.argv[1])
    randomSet = set()

    for i in range(0,num/5):
        randomSet.add(random.randint(0,num))
    for r in randomSet:
        print r


if __name__ == '__main__':
    __main__()
