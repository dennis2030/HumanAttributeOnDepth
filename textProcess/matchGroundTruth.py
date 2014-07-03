#!/usr/bin/env python
import sys

def __main__():
    groundTruth = sys.argv[1]
    inputFname = sys.argv[2]
    
    gt_f = open(groundTruth,'r')
    input_f = open(inputFname,'r')

    gt_lines = gt_f.readlines()
    input_lines = input_f.readlines()

    gt_names = []
    for line in gt_lines:
        gt_names.append(line.strip().split(',')[0].strip())

    print >> sys.stderr, len(gt_names)
    print >> sys.stderr, len(input_lines)
    for line in input_lines:
        prefix = line.strip().split(' ')[0].strip()
        if prefix in gt_names:
            print line.strip()



if __name__ == '__main__':
    __main__()
