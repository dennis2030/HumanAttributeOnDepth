#!/usr/bin/env python

# convert collar related files
# +1 means round shape
# +2 means v shape
# +3 means other type


def __main__():
    
    nameList = ['prefix', 'valid', 'roundShape', 'vShape', 'otherC', 'shirt', 'sweater', 'tShirt', 'tankTop', 'outerwear', 'hoodies', 'othersCate', 'shortSleeve', 'longSleeve', 'noSleeve', 'longHair', 'handHold', 'glass', 'bag', 'shortHair']

    round_f = open('roundShape.svm','r')
    v_f = open('vShape.svm','r')
    otherC_f = open('otherC.svm','r')    
    feat = open('combine.feat','r')
    collar_f = open('collarType.svm','w')
    gt = open('../../groundTruth/tagged.txt','r')
    label = open('../450/validLabels.txt','r')
        
    gt_lines = gt.readlines()
    feat_lines = feat.readlines()
    round_lines = round_f.readlines()
    v_lines = v_f.readlines()
    otherC_lines = otherC_f.readlines()
    label_lines = label.readlines()

    # parse groundtruth to dict
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

        roundInt = int(round_lines[i].split(' ')[0].strip())
        vInt = int(v_lines[i].split(' ')[0].strip())
        otherInt = int(otherC_lines[i].split(' ')[0].strip())
        tmp = roundInt + vInt + otherInt
        tmpS = ""
        if tmp != -1:
            print tmp
            count += 1
            continue
        if roundInt == 1:
            tmpS += '+1 ' + feat_lines[i].strip()
        elif vInt == 1:
            tmpS += '+2 ' + feat_lines[i].strip()
        else:
            tmpS += '+3 ' + feat_lines[i].strip()

        collar_f.write(tmpS + '\n')    

    print count

if __name__ == '__main__':
    __main__()
