#!/usr/bin/env python

# convert sleeve related files
# +1 means short shape
# +2 means v shape
# +3 means other type


def __main__():
    
    nameList = ['prefix', 'valid', 'shortShape', 'vShape', 'otherC', 'shirt', 'sweater', 'tShirt', 'tankTop', 'outerwear', 'hoodies', 'othersCate', 'shortSleeve', 'longSleeve', 'noSleeve', 'longHair', 'handHold', 'glass', 'bag', 'shortHair']

    short_f = open('shortSleeve.svm','r')
    long_f = open('longSleeve.svm','r')
    feat = open('combine.feat','r')
    sleeve_f = open('sleeveType.svm','w')
    gt = open('../../groundTruth/tagged.txt','r')
    label = open('../450/validLabels.txt','r')
        
    gt_lines = gt.readlines()
    feat_lines = feat.readlines()
    short_lines = short_f.readlines()
    long_lines = long_f.readlines()
    label_lines = label.readlines()

    # parse gshorttruth to dict
    recorddict = {}
    for line in gt_lines:
        tmp_list = line.split(',')
        valid_bit = tmp_list[1]
        
        if(valid_bit == '0'):
            continue
        recorddict[tmp_list[0]] = tmp_list

    count = 0
  
    for i in range(0,len(label_lines)):

        tmp_list = recorddict[label_lines[i].strip()]

        shortInt = int(short_lines[i].split(' ')[0].strip())
        longInt = int(long_lines[i].split(' ')[0].strip())
        tmp = shortInt + longInt
        tmpS = ""
        if shortInt == 1:
            tmpS += '+1 ' + feat_lines[i].strip()
        elif longInt == 1:
            tmpS += '+2 ' + feat_lines[i].strip()
        else:
            tmpS += '+3 ' + feat_lines[i].strip()

        sleeve_f.write(tmpS + '\n')    


if __name__ == '__main__':
    __main__()
