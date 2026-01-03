from functools import reduce, partial
from itertools import accumulate
from operator import add
import time
import numpy as np


TEST = False
PATH = "test10.txt" if TEST else "input10.txt"

with open(PATH) as f:
    input = []
    for ranges in f.read().split("\n"):
        buttons = ranges.split(" ")
        input.append(buttons)

def printBinaries(listOfBinary):
    print("[",end="")
    for bin in listOfBinary:
        print("{:06b},".format(bin),end="")
    print("]")
    
def printBinary(bin): print("{:06b}".format(bin))

def toNumpy(listoflist):
    allProblems = []
    for inst in listoflist:
        _ = inst.pop()
        machInst = inst.pop(0).strip("[]")
        machine_encoding = 0
        for (i,char) in enumerate(machInst):
            if char == '#':
                machine_encoding+=(1<<i)
        buttons = []
        #print("{:06b}".format(machine_encoding))
        for button_str in inst:
            digits = button_str.strip("()").split(',')
            button = 0
            for digit in digits:
                button+=(1<<int(digit))
            buttons.append(button)
        #printBinary(buttons)
        allProblems.append((machine_encoding,buttons))    
    return allProblems

items = (toNumpy(input))

def part1(item):
    desired, buttons = item 
    max = len(buttons)
    

    def inner(current, index, acc, best):
        if current == 0:return acc
        #Barely an optimization in this case, a huge optimization with more buttons
        #Simply, there aren't enough buttons to where this saves a lot of time because 2^n buttons is a small number
        if acc>=best: return best
        if index == max :return acc+999

        yes = inner(current^buttons[index],index+1,acc+1, best)
        no = inner(current,index+1,acc, yes)

        return min(yes,no)
    
    return inner(desired, 0, 0, 999)

initial = time.time()
res = (sum(map(part1,items)))
end = time.time()
print(res)
print("time elapsed (microsec):", (end-initial)*1000000.0)


with open(PATH) as f:
    input = []
    for ranges in f.read().split("\n"):
        buttons = ranges.split(" ")
        input.append(buttons)

def toNumpy1(listoflist):
    allProblems = []
    for inst in listoflist:
        machInst = inst.pop(0)
        machine = np.zeros(len(machInst)-2,dtype=int)
        lastly = inst.pop()
        for i,char in enumerate(machInst[1:-1]):
            machine[i] = 0 if char == '.' else 1 
        buttonList = []
        for buttons_str in inst:
            buttons = np.zeros(len(machInst)-2,dtype=int)
            for char in buttons_str:
                if char.isdigit():
                    buttons[int(char)] = 1
            buttonList.append(buttons)
        for char in lastly:
            desired = np.zeros(len(lastly))
            i = 0
            if char.isdigit():
                desired[i] = int(char)
                i = i+1
        allProblems.append((machine,buttonList, desired))
                     
    return allProblems

items = (toNumpy1(input))

#print(items)

#bruteforce
def slow(item):
    desired, buttons, _ = item 
    max = len(buttons)
    def inner(current, index):
        if np.all(np.equal(current % 2,desired)):
            return 0
        if index >= max:
            return 999
        #button = buttons[0]
        #buttons = buttons[1:]
        yes = 1 + inner(current+buttons[index],index+1)
        no = inner(current,index+1)
        return min(yes,no)
    return inner(np.zeros(desired.shape[0],dtype=int), 0)

initial = time.time()
res = (sum(map(slow,items)))
end = time.time()
print(res)
print("time elapsed (microsec):", (end-initial)*1000000.0)
