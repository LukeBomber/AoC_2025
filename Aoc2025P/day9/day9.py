from functools import reduce
import time
TEST = True
PATH = "test9.txt" if TEST else "input9.txt"

with open(PATH) as f:
    input = []
    for ranges in f.read().split("\n"):
        temp = ranges.split(",")
        input.append((int(temp[0]),int(temp[1])))

#bruteforce
'''
def part1(input):
    res = 0
    for (x1,y1) in input:
        for (x2,y2) in input:
            res = max(res, (x1-x2+1)*(y1-y2+1))
    return res 

initial = time.time()
print(part1(input))
after = time.time()
print("time elapsed (microseconds):", (after-initial)*1000000.0)
'''
def part2(input):
    res = 0
    for (x1,y1) in input:
        for (x2,y2) in input:
            if (x1-x2+1)*(y1-y2+1) > res:
                xmax,xmin = (x1,x2) if x1>=x2 else (x2,x1)
                ymax,ymin = (y1,y2) if y1>=y2 else (y2,y1)
                temp = list(filter(lambda coords: xmin < coords[0] < xmax and ymin < coords[1] < ymax ,input))
                if temp == []:
                    res = (x1-x2+1)*(y1-y2+1)
    return res 


initial = time.time()
print(part2(input))
after = time.time()
print("time elapsed (microseconds):", (after-initial)*1000000.0)
'''
def test(input):
    first = input[0][0] == input[1][0]
    results = []
    for i in range (len(input)-1):
        x1, y1 = input[i]
        x2, y2 = input[i+1]
        results.append((x1 == x2 if first else y1 == y2))
        first = not first 
    return results

print(len(list(filter(lambda x: not x, test(input)))) == 0)
'''