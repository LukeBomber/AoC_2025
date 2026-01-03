import numpy as np 
from functools import reduce
import time
import re


filename = "input2.txt"

with open(filename) as f:
    split = f.read().split(",")
    items = []
    for ranges in split:
        temp = ranges.split("-")
        items.append((int(temp[0]),int(temp[1])))

def digits(x): 
    return len(str(x))

def getStart(digits, width):
    mask = 0
    for i in range (width-1,digits,width):
        mask += (int(10**i)) 
    return mask 

def getMask(digits, width):
    mask = 0
    for i in range (0,digits,width):
        mask += (int(10**i)) 
    return mask 

def getNext(x, width):
    y = digits(x)+width  
    y = y-(y%width)   
    return getStart(y,width)


def findStart(item, width):
    if digits(item)<=1:
        return 11
    
    stritem = str(item)
    head = stritem[:width] 
    ratio = len(stritem)//width
    attempt = int(head*ratio)
    return (attempt if attempt>=item else int((str(int(head)+1))*ratio))
    
def inner(x, width,ub):
    sum = []

    if (digits(x) % width == 0):
        x = findStart(x, width)
        mask = getMask(digits(x),width)
    else:
        x = getNext(x,width)
        mask = getMask(digits(x),width)
        #mask = x


    while(True): 
        if (digits(x) > digits(x-mask)):
            if (digits(x) % width == 0):
                x = getStart(digits(x),width)
            else:
                x = getNext(x,width)
            mask = getMask(digits(x),width)
        if (x>ub):
            return sum
        if (digits(x) > width):
            sum.append(x)
        else:
            x = int(str(9)*digits(x))
        x+=mask 

        
            #mask = x
        
def flatten(xss):
    return [x for xs in xss for x in xs]

def part2(pair):
    item,ub = pair
    ids = []
    digit_count = digits(ub)
    for i in range (1,((digit_count)//2)+1,1):
        ids.append(inner(item,i,ub))
    return list(set(flatten(ids)))

#print(list(map(part2,items)))
initial = time.time()
res = sum(map(sum,(map(part2,items))))
end = time.time()
#print("result:", res, "actual:", 85513235135, res==85513235135, "diff:", res-85513235135)
print("reuslt:", res)
print("Time elapsed: ",(end-initial)*1000000.0,"microseconds")

'''
def part1(item):
    x,ub = item 
    ids = []
    digit_cnt = digits(x)
    if digit_cnt % 2 == 1:
        lower = int(10**((digit_cnt-1)/2))
        upper = lower 
        digit_cnt+=1
    else:
        lower = int(x % (10**(digit_cnt/2)))
        upper = int(x /(10**(digit_cnt/2)))
        if upper >= lower:
            lower = upper 
        else:
            upper=upper+1
            lower = upper 
    print(lower, upper)
    
    whole = lower + int(upper*(10**(digit_cnt/2)))
    #print(whole)
    
    while(True):
        #print(whole)
        if (ub < whole):
            return sum(ids)
        ids.append(whole)
        upper +=1
        lower +=1
        #print(lower, upper)
        dig = digits(lower)
        #print("dig is", dig)
        whole = lower + int(upper*(10**(dig)))

it = list(map(part1,items))
print(sum(it))

'''