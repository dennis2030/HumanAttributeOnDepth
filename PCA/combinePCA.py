#!/usr/bin/env python

def __main__():
    f1 = open('head.pca','r')
    f2 = open('torso.pca','r')
    f3 = open('leftArm.pca','r')
    f4 = open('rightArm.pca','r')

    head_lines = f1.readlines()
    torso_lines = f2.readlines()
    leftArm_lines = f3.readlines()
    rightArm_lines = f4.readlines()

    for i in range(0,len(head_lines)):
        tmpS = ""
        tmpS = head_lines[i].strip() + ',' + torso_lines[i].strip() + ',' + leftArm_lines[i].strip() + ',' + rightArm_lines[i].strip()
        print tmpS

if __name__ == '__main__':
    __main__()
