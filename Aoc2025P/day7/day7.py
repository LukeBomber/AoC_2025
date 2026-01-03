from functools import reduce
import time
TEST = False
PATH = "test7.txt" if TEST else "input7.txt"

with open(PATH) as f:
    lines = f.read().split("\n")
    table = []
    for line in lines:
        table.append(list(line))

'''
def part1(table):
    count = 0
    beams = [table[0].index('S')]
    toRemove = []
    toAdd = []
    for i in range(1,len(table)-1):
        
        for beam in beams:
            if table[i+1][beam] == '^':
                count +=1
                toAdd.append(beam+1)
                toAdd.append(beam-1)
                toRemove.append(beam)
        beams = beams + toAdd
        beams = list(set(beams)-set(toRemove))
        toRemove = []
        toAdd = []
    return(count)
res = part1(table)
print(res)
'''
'''
def part2(table):
    table[len(table)-1][:] = [1]*len(table[len(table)-1])

    rev = list(reversed(table))
    for (i,line) in enumerate(rev):
        for j in range(len(line)):
            if rev[i][j] == '.':
                if rev[i-1][j] == '^':
                    rev[i][j] = rev[i-1][j-1] + rev[i-1][j+1]    
                else:
                    rev[i][j] = rev[i-1][j]
            elif rev[i][j] == 'S':
                return rev[i-1][j]
    return None


def part2(table):
    mid = table[0].index('S')
    rev = list(reversed(table))

    def imadeDis(lst):
        match lst:
            case([h1,h2,h3,*t]):
                h2 = h1+h3 if h2 == 0 else h2 
                return [h1] + imadeDis([h2] +lst[2:])
            case(_):
                return lst 

    def inner(last_row, table):
        #print(last_row)
        if table[0][mid] == 'S':
            return last_row[mid]
        temp =  list(map(lambda elem : 0 if elem[1] == '^' else elem[0] ,zip(last_row, table.pop(0))))
        added = imadeDis(temp)
        return inner(added,table)
    
    return inner([1]*len(table[len(table)-1]), rev[1:])
'''
'''
def part2(table):
    mid = table[0].index('S')
    rev = list(reversed(table))
    
    def helper(row, data):
        match (row, data):
            case([h1,h2,h3,*_],[_,sym,*_]):
                h2 = h1+h3 if sym == '^' else h2 
                return [h1] + helper([h2] + row[2:],data[1:])
            case(_):
                return row
    def inner(last_row, table):
        return (last_row[mid] 
                if table[0][mid] == 'S'
                else inner(helper(last_row, table[0]),table[1:]))

    return inner([1]*len(table[len(table)-1]), rev[1:])
'''

#top down, TODO
def part2(table):
    start = table[0].index('S')
    end = len(table)
    def inner(dict, i, beam):
        if i == end-1:
            return (1, dict)
        if (i,beam) in dict:
            return dict[(i, beam)], dict
        if table[i][beam] == '.':
            res1, newdict = inner(dict,i+1,beam)
            newdict[(i,beam)] = res1
            return res1, newdict
        else:
            res1, dict1 = inner(dict,i+1,beam-1)
            res2, dict2 = inner(dict1,i+1,beam+1)
            dict2[(i,beam)] = res1+res2
            return (res1+res2,dict2)

    (res,_) = inner({}, 1, start)
    return res

initial = time.time()
print(part2(table))
after = time.time()
print("time elapsed (microseconds):", (after-initial)*1000000.0)
