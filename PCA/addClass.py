#!/usr/bin/env python
import sys


def __main__():
    
    
    nameList = ['prefix', 'valid', 'roundShape', 'vShape', 'otherC', 'shirt', 'sweater', 'tShirt', 'tankTop', 'outerwear', 'hoodies', 'othersCate', 'shortSleeve', 'longSleeve', 'noSleeve', 'longHair', 'handHold', 'glass', 'bag', 'shortHair']
    gt = open('../../groundTruth/tagged.txt','r')
    label = open('../450/validLabels.txt','r')
    feat = open('combine.feat','r')

    gt_lines = gt.readlines()
    label_lines = label.readlines()
    feat_lines = feat.readlines()

    # parse groundtruth to dict
    recorddict = {}
    for line in gt_lines:
        tmp_list = line.split(',')
        valid_bit = tmp_list[1]
        
        if(valid_bit == '0'):
            continue
        recorddict[tmp_list[0]] = tmp_list

    fileList = []
    counterList = []
    for i in range(0,len(nameList)):
        f = open(nameList[i] + '.svm','w')
        fileList.append(f)
        counter = 0
        counterList.append(counter)

    for i in range(0,len(label_lines)):

        tmp_list = recorddict[label_lines[i].strip()]
        for j in range(0,len(tmp_list)):
            tmpS = ""
            if tmp_list[j].strip() == '0':
                tmpS += '-1 ' + feat_lines[i].strip()
            else:
                tmpS += '+1 ' + feat_lines[i].strip()
            tmp_f = fileList[j]
            tmp_f.write(tmpS +'\n')


if __name__ == '__main__':
    __main__()
