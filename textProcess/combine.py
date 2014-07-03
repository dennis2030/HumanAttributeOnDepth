#!/usr/bin/env python

def __main__():

    head_f = open('head.feat','r')
    torso_f = open('torso.feat','r')
    leftArm_f = open('leftArm.feat','r')
    rightArm_f = open('rightArm.feat','r')

    head_dict = parseToDict(head_f)
    torso_dict = parseToDict(torso_f)
    leftArm_dict = parseToDict(leftArm_f)
    rightArm_dict = parseToDict(rightArm_f)
    for key in head_dict.keys():
        result = key
        count = 1
        tmp_head_list = head_dict[key]
        tmp_torso_list = torso_dict[key]
        tmp_leftArm_list = leftArm_dict[key]
        tmp_rightArm_list = rightArm_dict[key]
        for tmp in tmp_head_list:
            result += " " + str(count) + ':'+ tmp
            count+=1
        for tmp in tmp_torso_list:
            result += " " + str(count) + ':'+ tmp
            count+=1
        for tmp in tmp_leftArm_list:
            result += " " + str(count) + ':'+ tmp
            count+=1
        for tmp in tmp_rightArm_list:
            result += " " + str(count) + ':'+ tmp
            count+=1
        print result

def parseToDict(input_f):
    lines = input_f.readlines()
    returnDict = {}
    for line in lines:
        tmp_list = line.split(' ')
        prefix = tmp_list[0]
        restData = tmp_list[1:-1]
        returnDict[prefix] = restData

    return returnDict


if __name__ == '__main__':
    __main__()
