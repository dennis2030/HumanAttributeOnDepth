#!/usr/bin/env python

import sys

class Record:
    def __init__(self, prefix, roundShape, vShape, otherC, shirt, sweater, tShirt, hoodies, tankTop, othersCate, shortSleeve, longSleeve, noSleeve, shortHair, longHair, outerwear, glasses, handHold, bag):
        self.prefix = prefix
        self.roundShape = roundShape
        self.vShape = vShape
        self.otherC = otherC
        self.shirt = shirt
        self.sweater = sweater
        self.tShirt = tShirt
        self.hoodies = hoodies
        self.tankTop = tankTop
        self.othersCate = othersCate
        self.shortSleeve = shortSleeve
        self.longSleeve = longSleeve
        self.noSleeve = noSleeve
        self.shortHair = shortHair
        self.longHair = longHair
        self.outerwear = outerwear
        self.glasses = glasses
        self.handHold = handHold
        self.bag = bag
    def __str__(self):
        return 'prefix:{0}, roundShape:{1}, vShape:{2}, otherCollar:{3}, shirt:{4}, sweater:{5}, t-shirt:{6}, hoodies:{7}, tank-top:{8}, others category:{9}, shortSleeve:{10}, longSleeve:{11}, noSleeve:{12}, shortHair:{13}, longHair:{14}, outerwear:{15}, glasses:{16}, handHold:{17}, bag:{18}'.format(self.prefix, self.roundShape, self.vShape, self.otherC, self.shirt, self.sweater, self.tShirt, self.hoodies, self.tankTop, self.othersCate, self.shortSleeve, self.longSleeve, self.noSleeve, self.shortHair, self.longHair, self.outerwear, self.glasses, self.handHold, self.bag)


def Usage():
    print 'Usage: ./parseGrondTruth.py GroundTruth.txt'

def __main__():
    if len(sys.argv) < 2:
        Usage()
        return

    inputPath = sys.argv[1]
    
    f = open(inputPath, 'r')
    lines = f.readlines()
    recordList = []
    for line in lines:
        tmp_list = line.split(',')
        valid_bit = tmp_list[1]
        
        if(valid_bit == '0'):
            continue
        record = Record(tmp_list[0], tmp_list[2], tmp_list[3], tmp_list[4], tmp_list[5], tmp_list[6], tmp_list[7], tmp_list[8], tmp_list[9], tmp_list[10], tmp_list[11], tmp_list[12], tmp_list[13], tmp_list[14], tmp_list[15], tmp_list[16], tmp_list[17], tmp_list[18], tmp_list[19])
        recordList.append(record)
    print len(recordList)
    roundShapeCount = 0
    vShapeCount = 0
    otherCCount = 0
    for record in recordList:
        if record.roundShape =='1':
            roundShapeCount += 1
        elif record.vShape == '1':
            vShapeCount += 1
        elif record.otherC == '1':
            otherCCount += 1
    print '# roundShape = ' + str(roundShapeCount)
    print '# vShape = ' + str(vShapeCount)
    print '# otherC = ' + str(otherCCount)
if __name__ == '__main__':
    __main__()
