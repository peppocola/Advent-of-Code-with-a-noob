#!/usr/bin/env python
from collections import defaultdict
from itertools import product

def taxi(i, j):
    return abs(i[0]-j[0])+abs(i[1]-j[1])

def daysix():
    listy=[]
    for line in open(r"/home/peppocola/Scrivania/file"):
        x, y=[int(s.strip()) for s in line.split(',')]
        listy.append((x,y))

    maxx=listy[0][0]
    maxy=listy[0][1]
    minx=listy[0][0]
    miny=listy[0][1]
    for x, y in listy:
        if x>maxx:
            maxx=x
        elif x<minx:
            minx=x
        if y>maxy:
            maxy=y
        elif y<miny:
            miny=y
    #created a list of the coordinates
    #found min and max for x and y

    dicty=defaultdict(int)
    for i in range(minx, maxx+1):
        for j in range (miny, maxy+1):
            bestdist=taxi((maxx+1, maxy+1), (minx,miny))
            bestx=(-1,-1)
            doubt=False
            for x in listy:
                newdist=taxi((i,j),x)
                if newdist<bestdist:
                    bestdist=newdist
                    bestx=x
                    doubt=False
                elif newdist==bestdist:
                    doubt=True
            if doubt==True:
                dicty[(i,j)]=(-1,-1)
                doubt=False
                bestx=(-1,-1)
            else:
                dicty[(i,j)]=bestx
                bestx=(-1,-1)

    #used a dictionary to make a matrix with coordinates as key and value as closer point of the list

    edges=[]
    print (minx, miny, maxx, maxy)
    for x,y in dicty.keys():
        if x==minx or x==maxx or y==miny or y==maxy:
            edges.append(dicty[(x,y)])

    #made a list of edges, so i can ignore the points of listy when i go counting the finite spaces

    counter=defaultdict(int)

    for i in listy:
        if i not in edges:
            for x in dicty.values():
                if x==i:
                    counter[i]+=1
    print (max(counter.values()))

    #again used a dictionary to save the sizes of the spaces and to take the max

    size=0
    for i in range(minx, maxx+1):
        for j in range (miny, maxy+1):
            totaldist=0
            for x in listy:
                if totaldist<10000:
                    totaldist+=taxi(x, (i,j))
                else:
                    break
            if totaldist<10000:
                size+=1
    print (size)

    #made a sum of the total distance and then ++size if totaldist<10000




if __name__ == '__main__':
    daysixpart()
