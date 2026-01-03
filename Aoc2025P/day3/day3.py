
from functools import reduce
PATH = "input3.txt"

with open(PATH) as f:
    items = []
    t = f.read().split("\n")
    for string in t:
        items.append(list(map(int,list(string))))


def argmax(lst, startIndex=0):
    def inner(lst, max, argmax,curr):
        if lst == []:
            return argmax
        if lst[0] > max:
            return inner(lst[1:],lst[0],curr, curr+1)
        return inner(lst[1:], max, argmax,curr+1)
    return inner(lst,lst[startIndex],startIndex,startIndex)
'''
def part1(range):
    maxElem = max(range[:-1])
    argMax = argmax(range[:-1])
    maxElem2 = max(range[argMax+1:])
    return 10*maxElem+maxElem2
'''
def part2(bank, batteries=12):
    sol = []
    where_max = 0
    new_space = bank
    for i in range(batteries):
        new_space = bank[where_max:] if ((batteries-i-1) == 0) else bank[where_max:-(batteries-i-1)]
        what_max = max(new_space)
        where_max += argmax(new_space)+1
        sol.append(what_max)
    return int(reduce(lambda acc,elem: acc+str(elem), sol,""))

print(sum(list(map(part2,items))))
