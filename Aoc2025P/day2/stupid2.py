import re
import time

filename = "example2.txt"

with open(filename) as f:
    split = f.read().split(",")
    items = []
    for ranges in split:
        temp = ranges.split("-")
        items.append((int(temp[0]),int(temp[1])))

def digits(x): 
    return len(str(x))

def part2(pair):
    item,ub = pair
    res = []
    for i in range(item, ub+1):
        #print(i, width)
        if re.fullmatch(r"(\d+)\1+",str(i)):
            res.append(i)
    return sum(res)


initial = time.time()
res = sum(list(map(part2,items)))
end = time.time()
print(res)
print("Time elapsed: ",(end-initial)*1000000.0,"microseconds")
