#!/usr/bin/env python

# convert collar related files
# +1 means shirt
# +2 means t shirt
# +3 means sweater
# +4 means tank top
# +5 means hoodies
# +6 means other category


def __main__():
    
    nameList = ['prefix', 'valid', 'roundShape', 'vShape', 'otherC', 'shirt', 'sweater', 'tShirt', 'tankTop', 'outerwear', 'hoodies', 'othersCate', 'shortSleeve', 'longSleeve', 'noSleeve', 'longHair', 'handHold', 'glass', 'bag', 'shortHair']

    shirt_f = open('shirt.svm','r')
    sweater_f = open('sweater.svm','r')
    otherCate_f = open('othersCate.svm','r')
    tshirt_f = open('tShirt.svm','r')
    tankTop_f = open('tankTop.svm','r')
    hoodies_f = open('hoodies.svm','r')
    

    feat = open('combine.feat','r')
    dressType_f = open('dressType.svm','w')
    gt = open('../../groundTruth/tagged.txt','r')
    label = open('../450/validLabels.txt','r')
        
    gt_lines = gt.readlines()
    feat_lines = feat.readlines()
    shirt_lines = shirt_f.readlines()
    tShirt_lines = tshirt_f.readlines()
    otherCate_lines = otherCate_f.readlines()
    sweater_lines = sweater_f.readlines()
    tankTop_lines = tankTop_f.readlines()
    hoodies_lines = hoodies_f.readlines()
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

        shirtInt = int(shirt_lines[i].split(' ')[0].strip())
        tShirtInt = int(tShirt_lines[i].split(' ')[0].strip())
        otherCateInt = int(otherCate_lines[i].split(' ')[0].strip())
        sweaterInt = int(sweater_lines[i].split(' ')[0].strip())
        tankTopInt = int(tankTop_lines[i].split(' ')[0].strip())
        hoodiesInt = int(hoodies_lines[i].split(' ')[0].strip())

        tmp = shirtInt + tShirtInt + otherCateInt + sweaterInt + tankTopInt + hoodiesInt

        tmpS = ""
        if tmp != -4:
            print tmp
            count += 1
            continue
        if shirtInt == 1:
            tmpS += '+1 ' + feat_lines[i].strip()
        elif tShirtInt == 1:
            tmpS += '+2 ' + feat_lines[i].strip()
        elif sweaterInt == 1:
            tmpS += '+3 ' + feat_lines[i].strip()
        elif tankTopInt == 1:
            tmpS += '+4 ' + feat_lines[i].strip()
        elif hoodiesInt == 1:
            tmpS += '+5 ' + feat_lines[i].strip()
        else:
            tmpS += '+6 ' + feat_lines[i].strip()

        dressType_f.write(tmpS + '\n')    

    print count

if __name__ == '__main__':
    __main__()
