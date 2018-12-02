#!/usr/bin/env python
def filescan(fname):
    with open (fname, "r") as f:
        return f.read().strip().splitlines()
#reads the lines of a file, removes whitespaces, splits the lines;

def daytwo_part1():
    ch=filescan("/home/peppocola/Scrivania/file")

    twice=0
    three=0

    for i in ch: #taking one string per time
        countedtwo=0 #temporary counters
        countedthree=0
        for e in i: #taking one char per time and checking how much time it's in the string
            c=i.count(e) #counting occurences for e (that is a char)
            if c==3:
                countedthree+=1
            elif c==2:
                countedtwo+=1

        countedtwo=countedtwo/2 #dividing by two because every char repeated twice is counted two times
        countedthree=countedthree/3 #dividing by three because every char repeated twice is counted two times
        if countedtwo==1 and countedthree==1:
            twice+=1
            three+=1
        elif countedtwo>0 and countedthree==0:
            twice+=1
        elif countedtwo==0 and countedthree>0:
            three+=1

    print 'checksum is',
    print (twice*three);

def similiar(i, j): #checking if strings have distance=1
    difference=0
    for e in range(0, len(i)-1):
        if i[e]!=j[e]:
            if difference==1: #if the difference is already one, i don't need to go on, i don't like this string
                return 0
            difference=difference+1

    if difference==1:
        return 1
    elif difference==0: #if they are equal i don't need 'em, i only want distance=1
        return -1

def removeDifference(i, j): #removing the wrong char, i suppose that the string have distance=1, with more distance it will remove only the first wrong char

    for e in range(0, len(i)-1):
        if i[e]!=j[e]:
            c=i[:e]+i[(e+1):] #c is the left part of the string plus the right part of the string without e
            return c #if i removed i don't need to go on

def daytwo_part2():

    ch=filescan("/home/peppocola/Scrivania/file")
    for i in ch:
        for j in ch:
            if similiar(i,j)==1: #if similiar i print and remove the wrong char
                print 'strings found:'
                print(i)
                print(j)
                c=removeDifference(i, j)
                print 'result:',
                print(c)
                return c

#ggez

if __name__=="__main__":
    daytwo_part1()
    daytwo_part2()
