from collections import defaultdict


def findTime(line):
    numbers=line.split()
    time=numbers[1][:-1]
    return int(time.split(':')[1])

def maxvalue(dicty):
    max=None
    for key, value in dicty.items():
        if max is None or value>dicty[max]:
            max=key
    return max

def dayfour_part1():
    input=open(r"C:\Users\giuse\Desktop\file.txt").read().split('\n')
    input.sort()

    tot_minutes=defaultdict(int)
    minutes_asleep=defaultdict(lambda:defaultdict(int))

    guard=None
    asleep=None

    for line in input:
        if line:
            time=findTime(line)
            if 'begins shift' in line:
                guard=int(line.split()[3][1:])
                asleep=None
            if 'falls asleep' in line:
                asleep=findTime(line)
            if 'wakes up' in line:
                for temp in range (asleep, time):
                    tot_minutes[guard]+=1
                    minutes_asleep[guard][temp]+=1
    
    sleepy_guard=maxvalue(tot_minutes)
    best_minute=maxvalue(minutes_asleep[sleepy_guard])
    
    print(sleepy_guard*best_minute)
        
def dayfour_part2():
    input=open(r"C:\Users\giuse\Desktop\file.txt").read().split('\n')
    input.sort()

    tot_minutes=defaultdict(int)
    minutes_asleep=defaultdict(int)

    guard=None
    asleep=None

    for line in input:
        if line:
            time=findTime(line)
            if 'begins shift' in line:
                guard=int(line.split()[3][1:])
                asleep=None
            if 'falls asleep' in line:
                asleep=findTime(line)
            if 'wakes up' in line:
                for temp in range (asleep, time):
                    minutes_asleep[(guard, temp)]+=1
    
    sleepy_guard, best_minute=maxvalue(minutes_asleep)
    
    print(sleepy_guard*best_minute)
