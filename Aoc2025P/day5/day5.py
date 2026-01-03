
TEST = False
PATH = "test5.txt" if TEST else "input5.txt"
from functools import reduce

with open(PATH) as f:
    input = f.read().split("\n")
    data = []
    for i,line in enumerate(input):
        if line == '':
            ingredients = list(map(int,input[i+1:]))
            break
        ranged = line.split('-')
        data.append((int(ranged[0]),int(ranged[1])))
        #data.sort(key=lambda t: t[0])

def flatten(xss):
    return [x for xs in xss for x in xs]
'''
def checkRange(arange, item):
    lb,ub=arange 
    return lb <= item <= ub

def part1(ranges,ingredients):
    #res = 
    #print(reduce(lambda acc, elem: acc or elem, ranges, False))
    #return 0
    return list(map(lambda x: 1 if reduce(lambda acc, elem: acc or checkRange(elem,x), ranges, False) else 0,ingredients))

print(sum(part1(data,ingredients)))
'''

def trimRange(aRange, trimmed):
    lb1,ub1 = aRange
    for (lb2,ub2) in trimmed:
        if (lb1 > ub2 or lb2 > ub1):
            continue 
        if (lb1 >= lb2 and ub1 <= ub2):
            return trimmed
        if (lb1 <= lb2 and ub1 >= ub2):
            trimmed.remove((lb2,ub2))
            continue
        if (lb1 <= lb2 <= ub1):
            ub1 = lb2-1
        if (lb1 <= ub2 <= ub1):
            lb1 = ub2+1

        #cleanup
        if (lb1 > ub1):
            return trimmed
    trimmed.append((lb1,ub1))

    return trimmed 
        


def part2(ranges):
    trimmed = []
    for aRange in ranges:
        #print(aRange)
        trimmed = trimRange(aRange,trimmed)
        print(trimmed, " <- ", aRange)
    return list(map(lambda tup: tup[1]-tup[0]+1 , trimmed))
        
print(sum(part2(data)))