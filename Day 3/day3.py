#!/usr/bin/env python
import re

from itertools import product

def daythree():

    with open (r"C:\Users\giuse\Desktop\file") as input:

        input = input.read().strip().split('\n')   #read file, remove blank, splitting by line

        input = [[int(n) for n in re.findall('\d+',l)] for l in input] #regular expression to extract only numbers and put it in "input"

    fabric = {}  #declaring dictionary

    for id,x,y,sx,sy in input:

        patches = product(range(x,x+sx),range(y,y+sy)) #cartesian product of two ranges

        for p in patches:
            print(p)
            if p not in fabric: #insert in dictionary if not present
                fabric[p] = 0

            else:
                fabric[p] += 1 #incrementing value if overlapped
                
    overlapping=0
    for k in fabric:
        if fabric[k]>0:
            overlapping+=1    #counting overlapped cells

    print('Part 1: ' + str(overlapping))

    for id,x,y,sx,sy in input:

        patches = product(range(x,x+sx),range(y,y+sy))
        
        overlapping=0
        for p in patches:
            if fabric[p]>0:  #counting the overlapping of each room
              overlapping+=1
        if overlapping==0:   #if not overlapped room found, i won
            break
            
    print('Part 2: ' + str(id))