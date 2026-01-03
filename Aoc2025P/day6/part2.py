from functools import reduce
import numpy as np
import operator

#Hold kæft where is he da ugly

TEST = False
PATH = "test6.txt" if TEST else "input6.txt"

with open(PATH) as f:
    table = []
    lines = f.read().split("\n")
    for line in lines:
        table.append(list(line))
print(table)
transposed = list(map(list, zip(*table)))
print(transposed)

ops = {"*": operator.mul,
       "+": operator.add,
       }

initial = True
res = 0
elems = []
op = operator.add
for i in range(len(transposed)):
    
    #print(i,"4")
    if initial:
        op = ops[transposed[i][4]]
        initial = False
    if(all(elem == ' ' for elem in transposed[i])):
        res+=(reduce(op,elems))
        print(res)
        initial = True
        elems = []
        continue
    acc = ""
    for j in range(4):
        acc += transposed[i][j]
    elem = int(acc.strip())
    elems.append(elem)
print(res)
    #if(i > 100):
    #    break

        