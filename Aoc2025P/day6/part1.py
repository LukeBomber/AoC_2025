from functools import reduce
import numpy as np
import operator

TEST = False
PATH = "test6.txt" if TEST else "input6.txt"

with open(PATH) as f:
    input = f.read().split()
    i = 0
    while(input[i].isnumeric()):
        i+=1
    print(i)
    ratio = i//(len(input)-i)
    symbol_cnt = (len(input)-i)
    table = np.zeros((symbol_cnt,ratio),dtype=int)
    symbols = input[i:]
    print(symbols)
    print(table)
    print(symbol_cnt,ratio)
    for (i,entry) in enumerate(input[:-symbol_cnt]):
        table[i%symbol_cnt, i//symbol_cnt] = entry

        print(i%symbol_cnt, i//symbol_cnt)
    print(table)
#print(np.where(table == 0).shape(0))

ops = {"*": operator.mul,
       "+": operator.add,
       }

def toCephalopod(entry, op):
    urdumb = []
    
    return 

acc = 0
for i in range(symbol_cnt):
    acc+= toCephalopod(table[i], ops[symbols[i]])
print(acc)


#print(input, i, input[i])
#assert(i % (len(input)-i) == 0)
#ratio = i//(len(input)-i)
#print(ratio)
