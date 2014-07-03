#!/usr/bin/env python
import shutil

def __main__():

    random_f = open('randomSet.txt','r')
    fname_f = open('correspond_fname.txt','r')

    random_lines = random_f.readlines()
    random_lines = [int(tmp.strip()) for tmp in random_lines] 
    fname_lines = fname_f.readlines()
    fname_dict = {}

    # construct corresponds fname dict
    for line in fname_lines:
        tmp_list = line.split('\t')
        origin_fname = tmp_list[0].strip()
        mapped_idx = int(tmp_list[1].strip().split('.')[0])
        fname_dict[mapped_idx] = origin_fname
    
    srcDir = '/home/master/02/bean/research/depth_attribute/data/color/'
    trainDir = './images/train/'
    testDir = './images/test/'
    for i in range(451):
        if i in random_lines:
#            print i, fname_dict[i+1]
            shutil.copy2( srcDir + fname_dict[i+1], testDir+'%06d.jpg' % i)
        else:
            shutil.copy2( srcDir + fname_dict[i+1], trainDir+'%06d.jpg' % i)

if __name__ == '__main__':
    __main__()
