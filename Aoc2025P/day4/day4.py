
TEST = False
PATH = "test4.txt" if TEST else "input4.txt"
from itertools import product


def printDiagram(diagram):
    for lines in diagram:
        print(lines)

with open(PATH) as f:
    input = []
    for lines in f.read().split("\n"):
        input.append(list(lines))

def searchSpace(diagram,i,j,patterns,searchedFor):
    count = 0
    for pattern in patterns:
        x = i+pattern[0]
        y = j+pattern[1]
        if (0 <= x < len(diagram) and 0 <= y < len(diagram[0])):
            count += (1 if (diagram[x][y] in searchedFor) else 0)
    return count 

def copyListList(input):
    new = []
    for lists in input:
        inner = []
        for item in lists:
            inner.append(item)
        new.append(inner)
    
    return new

def part2(diagram): 
    count = 0
    patterns = list(product((-1, 0, 1), repeat=2))
    patterns.remove((0,0))
    old = []
    while(old != diagram):
        old = copyListList(diagram)
        for i,lines in enumerate(diagram):
            for j in range(len(lines)):
                if (diagram[i][j] == '@'):
                    if (searchSpace(diagram,i,j,patterns, ('@')) < 4):
                        diagram[i][j] = 'x'
                        count+=1
    
    return count

print(part2(input))
'''
def part1(diagram): 
    count = 0
    patterns = list(product((-1, 0, 1), repeat=2))
    patterns.remove((0,0))
    #print(patterns)
    for i,lines in enumerate(diagram):
        for j, element in enumerate(lines):
            if (diagram[i][j] == '@'):
                if (searchSpace(diagram,i,j,patterns, ('@','x')) < 4):
                    #diagram[i][j] = 'x'
                    count+=1
    #printDiagram(diagram)
    return count

    
print(part1(input))
'''