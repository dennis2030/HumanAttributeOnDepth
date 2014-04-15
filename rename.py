#!/usr/bin/env python

import os
import sys

def helper():
    print 'Usage: ./rename.py renameDir/'


def __main__():
    if len(sys.argv) < 2:
        helper()
        return

    renameDir = sys.argv[1]

    rename_list = os.listdir(renameDir)

    for fname in rename_list:
        if not fname.endswith(".jpeg"):
            continue
        prefix = fname.split('.')[0]
        os.rename(renameDir+fname, renameDir+prefix+'.jpg')


if __name__ == '__main__':
    __main__()
