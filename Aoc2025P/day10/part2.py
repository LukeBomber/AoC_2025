from functools import reduce, partial
from itertools import accumulate
from operator import add
import time
import numpy as np
import math

eps = 1e-9

TEST = False
PATH = "test10.txt" if TEST else "input10.txt"

with open(PATH) as f:
    input = []
    for ranges in f.read().split("\n"):
        buttons = ranges.split(" ")
        input.append(buttons)

'''
def toNumpy(listoflist):
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

items = (toNumpy(input))

#print(items)

#bruteforce
def part1(item):
    desired, buttons, _ = item 
    def inner(current, buttons):
        if np.all(np.equal(current % 2,desired)):
            return 0
        if len(buttons) == 0:
            return 999
        button = buttons[0]
        buttons = buttons[1:]
        yes = 1 + inner(current+button,buttons)
        no = inner(current,buttons)
        return min(yes,no)
    return inner(np.zeros(desired.shape[0],dtype=int), buttons)

print(sum(map(part1,items)))
'''
# [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7} -> 
def part2Parse(input):
    _ = input.pop(0)
    
    volt = input.pop()
    xn = []
    for xi in input:
        xn.append(list(map(int, xi.strip("()").split(","))))
    #print(xn)
 
    jolt = list(map(int,volt.strip("{}").split(",")))
    count = len(jolt)
    
    button = 0
    #desired = np.zeros(count)
    matrix = np.zeros((count,len(input)+1), dtype=int)
    for jo in jolt:
        #desired[button] = char
        matrix[button,len(input)-1+1]=jo
            
        for (i,xi) in enumerate(xn):
            for elem in xi:
                if elem == button:
                    matrix[button,i] +=1
        button += 1
    return matrix, jolt

def findLeader(matrix, col, skipindex):
    for i in range(matrix.shape[0]):
        if (i == skipindex): continue
        if not matrix[i,col] == 0:
            return i
    return None

def findLeader2(matrix, col, limit):
    for i in range(limit+1, matrix.shape[0]):
        if not matrix[i,col] == 0:
            return i
    return None

def gausReduc(matrix):
    i = 0 #Row of current leader
    j = 0 #Column of current leader
    while (i<matrix.shape[0] and j<matrix.shape[1]):
        #print(matrix, i, j)
        #swap rows to make leader position have leader
        if matrix[i,j] == 0:
            index = findLeader2(matrix, j, i)
            if index == None:
                j+=1
                continue
            
            matrix[[i, index]] = matrix[[index,i]]

        #if leader is -1, make it 1. Just easier to read.
        if(matrix[i,j])<0:
            matrix[i] = matrix[i]*(-1)
        #if not (matrix[i,j])==1:
        #    matrix[i] = matrix[i]//matrix[i,j]
        
        #for other non-zeros in that column, eliminate them by either adding 
        #or subtracting the leader row
        index = findLeader(matrix, j, i) 
        while(not index == None):
            #make into ternary
            #if (matrix[i][j]*matrix[index][j]>0):
            #    matrix[index] -= matrix[i]
            #else:
                #matrix[i][j] = pivot = p
                #*matrix[index][j] = a 
            matrix[index] = matrix[i][j]*matrix[index]-matrix[index][j]*matrix[i]
            index = findLeader(matrix, j, i)
        i = i + 1
        j = j + 1

    #Identifies all free variables for later, by setting every to free
    #Then gradually deleting the columns with leaders from the list.
    free = [k for k in range (matrix.shape[1]-1)]
    i = 0
    j = 0
    while (i<matrix.shape[0] and j<matrix.shape[1]-1):
        #print(free, i, j)
        if not matrix[i,j] == 0:
            free.remove(j)
        else: 
            while (matrix[i,j] == 0 and j<matrix.shape[1]-1):
                j+=1
            #If we exited for the right reasons...
            if (j<matrix.shape[1]-1):
                free.remove(j)
        i+=1
        j+=1
         
            
    return (matrix,free)

def findUB(matrix, free):
    upper_bounds = []
    lower_bounds = []
    for row in matrix:
        zeros = list(map(lambda x: (row[x]), free))
        
        #If only one of the variables are relevant for this row
        if sum(1 for x in zeros if x != 0) == 1:
            free_ind = next(i for i, x in enumerate(zeros) if x != 0)
            b = row[row.shape[0]-1]
            f = row[free[free_ind]]
            if b > 0 and f>0:
                upper_bounds.append((free_ind, 1+(b//f)))
            elif b<0 and f<0:
                lower_bounds.append((free_ind, (b//f)))

    #print(upper_bounds)
    ub = []
    lb = []
    #print(lower_bounds)
    #print(upper_bounds)
    for j in range (len(free)):
        tu = (list(filter(lambda x: x[0] == j,upper_bounds)))
        tl = (list(filter(lambda x: x[0] == j,lower_bounds)))
        #print(tu)
        #print(tl)
        #Ugly, please change
        lb.append(max(map(lambda tup: tup[1], tl)) if not tl == [] else 0)
        ub.append(min(map(lambda tup: tup[1], tu)) if not tu == [] else 999999)
        
    #print(constraint, free)
    #print(constraint)
    return ub,lb

def computeLambdas(matrix, free):
    pivot_cols = [j for j in range(matrix.shape[1]-1) if j not in free]
    leaders = {}
    factorss = []

    for j in pivot_cols:
        for i in range(matrix.shape[1]):
            if matrix[i,j] != 0:
                leaders[i] = j
                factorss.append(matrix[i,j])
                break
    #print(leaders)
    #print(factorss)

    def sub(pivot, goal, args, factors):
        for i in range (len(args)):
            goal-=args[i]*factors[i]
        if goal % pivot == 0:
            return goal 
        #print("how the fuck", goal, pivot)
        return 999999
    
    lambdas = []
    for (ii,row) in enumerate(matrix):
        x  = (lambda pivot, goal,factors, args: sub(pivot, goal,args,factors) )
        factors = [row[free[k]]for k in range(len(free))]
        
        #Could seek to remove
        if ii in leaders.keys():
            lambdas.append(partial(x, row[leaders[ii]], row[matrix.shape[1]-1], factors))
    return lambdas, factorss
    


def combinations(listOfUB, listOfLB):
    #print(listOfLB)
    res = []
    scanOfUB = list(accumulate(listOfUB, lambda x,y: x*y, initial=1))[:-1]
    
    for c in range(math.prod(listOfUB)):
        step = []
        valid = True
        for i in range(len(listOfUB)):
            num = c//scanOfUB[i] % listOfUB[i]
            step.append(num)
            if num < listOfLB[i]:
                valid = False
                break
            
        #print(c,step)
        if valid:
            res.append(step)
        #else:
            #print(step)
    return res

def solve(lambdas, factors,ubs, lbs):
    #assert(len(free) == len(ubs))
    #assert(len(free) == len(lbs))
    
    #all that may be valid
    #print(ubs)
    tries = (combinations(ubs,lbs))
    #print(tries[:100])

    #We try every combination
    min_sol = 99999999

    for attempt in tries:#tries:
        #We also count the buttons pressed of free variables
        res = sum(attempt)
        
        for (i,fun) in enumerate(lambdas):      
            x_i = fun(attempt)//factors[i]
            if x_i < 0:
                res = 999999
                break 
            res+=x_i
        #if res < min_sol:
            #print(attempt, res)
        min_sol = min(min_sol, res)
    return min_sol

initial = time.time()
d=[]
iter = 0
for inp in input:
#for inp in [input[3]]:
    
    m0, jolt = part2Parse(inp)
    #print(m0)
    m1,free = (gausReduc(m0))
#'ard
    lambdas, factors = computeLambdas(m1, free)

    ubs, lbs = findUB(m1,free)

    safe_ub = [min(ub,max(jolt)) for ub in ubs]

    sol= solve(lambdas, factors, safe_ub, lbs)

    d.append(sol)
    #print("sol for", iter+1, "is", sol)
    iter+=1
end = time.time()
print("time elapsed (microseconds):", (end-initial)*1000000.0)

#print(d)
print(sum(d))
    


#def part2(item):


#todo, handle numbers of >1 ciphers
#also todo: Clean the hell up, also part 1 maybe sound sun honestly
#Maybe?: Implement fun solution using optimized part 1 preferably.