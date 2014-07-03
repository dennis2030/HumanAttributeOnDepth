#!/usr/bin/env python

import sys


def __usage__():
    print 'Usage: ./convertGT.py groundtruth.txt'

def __main__():

    inputFname = sys.argv[1]
    gt_f = open(inputFname,'r')

    nameList = ['prefix', 'valid', 'roundShape', 'vShape', 'otherC', 'shirt', 'sweater', 'tShirt', 'tankTop', 'outerwear', 'hoodies', 'othersCate', 'shortSleeve', 'longSleeve', 'noSleeve', 'longHair', 'handHold', 'glass', 'bag', 'shortHair']
#    att_list = ['black_GT','blue_GT','brown_GT','cyan_GT','gender_GT','gray_GT','green_GT', 'many_colors_GT', 'neckline_GT', 'pattern_floral_GT','pattern_graphics_GT','pattern_plaid_GT','pattern_solid_GT','pattern_spot_GT','placket_GT','purple_GT','red_GT', 'scarf_GT', 'skin_exposure_GT','white_GT','yellow_GT']

    attIndex_list = [9,16,17,18]
    parts_list = ['head', 'torso', 'leftArm', 'rightArm']

    gt_lines = gt_f.readlines()
   
    for part in parts_list: 
        # for neckline && collar
        f_color = open('neckline_' + part + '_color_GT.txt','w')
        f_depth = open('neckline_' + part + '_depth_GT.txt','w')
        f_collar_color = open('collar_' + part + '_color_GT.txt','w')
        f_collar_depth = open('collar_' + part + '_depth_GT.txt','w')

        for line in gt_lines:
            tmp_list = line.split(',')
            fname = tmp_list[0]
            roundShape = int(tmp_list[2])
            vShape = int(tmp_list[3])
            other = int(tmp_list[4])
            result = 0;
            collar = 1;
            if roundShape == 1:
                result = 1
            elif vShape == 1:
                result = 2
                collar = 2
            else:
                result = 3
                collar = 2
            f_depth.write(fname + '.jpg ' + str(result)  + '\n')
            f_color.write(fname + '.jpg ' + str(result)  + '\n')
            f_collar_depth.write(fname + '.jpg ' + str(collar) + '\n')
            f_collar_color.write(fname + '.jpg ' + str(collar) + '\n')

        f_color.close()
        f_depth.close()
        f_collar_color.close()
        f_collar_depth.close()

        # for category
        f_color = open('category_' + part + '_color_GT.txt','w')
        f_depth = open('category_' + part + '_depth_GT.txt','w')
        
        for line in gt_lines:
            tmp_list = line.split(',')
            fname = tmp_list[0]
            shirt = int(tmp_list[5])
            sweater = int(tmp_list[6])
            tShirt = int(tmp_list[7])
            tankTop = int(tmp_list[8])
            hoodies = int(tmp_list[10])
            otherCate = int(tmp_list[11])
            category = 0
            if shirt == 1:
                category = 1
            elif tShirt == 1:
                category = 2
            elif sweater == 1:
                category = 3
            elif tankTop == 1:
                category = 3
            elif hoodies == 1:
                category = 3
            else:
                category = 3
            f_depth.write(fname + '.jpg ' + str(category) + '\n')
            f_color.write(fname + '.jpg ' + str(category) + '\n')

        f_depth.close()
        f_color.close()
        
        # for sleeve length
        f_color = open('sleevelength_' + part +'_color_GT.txt','w')
        f_depth = open('sleevelength_' + part +'_depth_GT.txt','w')
        
        for line in gt_lines:
            tmp_list = line.strip().split(',')
            fname = tmp_list[0]
            shortSleeve = int(tmp_list[12])
            longSleeve = int(tmp_list[13])
            noSleeve = int(tmp_list[14])
            sleeve = 0
            if shortSleeve == 1:
                sleeve = 1
            elif longSleeve == 1:
                sleeve = 2
            else:
                sleeve = 3
            f_depth.write(fname + '.jpg ' + str(sleeve) + '\n')
            f_color.write(fname + '.jpg ' + str(sleeve) + '\n')
        f_color.close()
        f_depth.close()

        # for hair length
        f_color = open('hairlength_' + part + '_color_GT.txt','w')
        f_depth = open('hairlength_' + part + '_depth_GT.txt','w')
        
        for line in gt_lines:
            tmp_list = line.strip().split(',')
            fname = tmp_list[0]
            longHair = int(tmp_list[15])
            shortHair = int(tmp_list[19])
            hairLength = 1
            if longHair == 1:
                hairLength = 2
            f_depth.write(fname + '.jpg ' + str(hairLength) +'\n' )
            f_color.write(fname + '.jpg ' + str(hairLength) +'\n' )
        f_color.close()
        f_depth.close()

        # for rest of attributes
        for idx in attIndex_list:
            f_color = open(nameList[idx]+ '_' + part + '_color_GT.txt','w')
            f_depth = open(nameList[idx]+ '_' + part + '_depth_GT.txt','w')
            for line in gt_lines:
                tmp_list = line.strip().split(',')
                att = 1
                if tmp_list[idx] == '1':
                    att = 2
                f_depth.write(fname + '.jpg ' + str(att)+'\n')
                f_color.write(fname + '.jpg ' + str(att)+'\n')
            f_color.close()
            f_depth.close()
        
if __name__ == '__main__':
    __main__()