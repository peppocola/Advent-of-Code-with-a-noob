#!/usr/bin/env python
def filescan(fname):
    with open (fname, "r") as f:
        return f.read().strip().splitlines()
#reads the lines of a file, removes whitespaces, splits the lines;

def dayone_part1():
    str#!/usr/bin/env python=filescan("/home/peppocola/Scrivania") #string with all the file values, there is a number per line
    numbers=[int(e) for e in str] #array with every number from the file
    result=sum(numbers) #sum of every number in the array
    print(result)

def dayone_part2():
    str=filescan("/home/peppocola/Scrivania") #string with all the file values, there is a number per line
    numbers=[int(e) for e in str] #array with every number from the file
    freq=0 #the first frequency is 0
    dict={0:1} #dict is a map/dictionary, i assign the value 1 to the key 0

    index=0%
    while (true):
        freq=freq+numbers[index%len(numbers)]
        if freq in dict:
            print(freq)
            break
        else
            dict[freq]=1
        index+=1

    result=sum(numbers) #sum of every number in the array


if ___name___=="___main___":
    dayone_part1()
    dayone_part2()
