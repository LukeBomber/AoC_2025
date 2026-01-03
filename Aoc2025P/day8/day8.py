from functools import reduce
import time
import math

TEST = False
PATH = "test8.txt" if TEST else "input8.txt"

with open(PATH) as f:
    input = []
    for ranges in f.read().split("\n"):
        temp = ranges.split(",")
        input.append((int(temp[0]),int(temp[1]),int(temp[2])))
    
def dist(p):
    p1, p2 = p
    x1,y1,z1 = p1 
    x2,y2,z2 = p2 

    return math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)

def combine(list, i, j):
    fst, snd = (i,j) if i>j else (j,i)
    c1 = list.pop(fst)
    c2 = list.pop(snd)
    list.append(c1+c2)
    return list 

'''
def part1(input, runs):
    ok = []
    for i in range (len(input)):
        for j in range (i+1,len(input)):
            p1 = input[i]
            p2 = input[j]
            if not p1 == p2:
                ok.append((p1,p2))
    ok.sort(key=dist)
    curcuits = []
    for closest in ok[:runs]:
        j1 = closest[0]
        j2 = closest[1]
        j1index = None
        j2index = None 
        for (i,curcuit) in enumerate(curcuits):
            if j1 in curcuit:
                j1index = i
            if j2 in curcuit:
                j2index = i
        if j1index == None and j2index == None:
            curcuits.append([j1,j2])
        elif (j1index == None):
            curcuits[j2index].append(j1)
        elif (j2index == None):
            curcuits[j1index].append(j2)
        else:
            if not (j1index == j2index):
                curcuits = combine(curcuits, j1index, j2index)
    curcuits.sort(key=len, reverse=True)
    return len(curcuits[0])*len(curcuits[1])*len(curcuits[2])

print(part1(input, 1000))
'''

def part2(input):

    ok = []
    for i in range (len(input)):
        for j in range (i+1,len(input)):
            p1 = input[i]
            p2 = input[j]
            ok.append((p1,p2))
            
    ok = list(filter(lambda x: not x[0] == x[1], ok))
    ok.sort(key=dist)
    curcuits = []
    for closest in ok:
        j1 = closest[0]
        j2 = closest[1]
        j1index = None
        j2index = None 
        for (i,curcuit) in enumerate(curcuits):
            if j1 in curcuit:
                j1index = i
            if j2 in curcuit:
                j2index = i
        if j1index == None and j2index == None:
            curcuits.append([j1,j2])
        elif (j1index == None):
            curcuits[j2index].append(j1)
        elif (j2index == None):
            curcuits[j1index].append(j2)
        else:
            if not (j1index == j2index):
                curcuits = combine(curcuits, j1index, j2index)
        if len(curcuits) == 1 and sum(list(map(len,curcuits))) == len(input):
            return j1[0]*j2[0], (slut-start)*1000000.0
    return None 

initial = time.time()
res = part2(input)
after = time.time()
print(res[0])
print("time of pairs (microseconds): ", res[1])
print("time elapsed (microseconds):", (after-initial)*1000000.0)