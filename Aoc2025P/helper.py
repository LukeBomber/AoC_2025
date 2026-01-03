from itertools import accumulate
import math

#assumes sorted, then done in O(m+n)
def listDiff(listA, listB):
    match (listA, listB):
        case ([],_):
            return []
        case (xs,[]):
            return xs
        case _:
            if listA[0] == listB[0]:
                return listDiff(listA[1:],listB)
            elif listA[0] > listB[0]:
                return listDiff(listA,listB[1:])
            else:
                return [listA[0]] + listDiff(listA[1:],listB)

def combinations(listOfUB):
    res = []
    scanOfUB = list(accumulate(listOfUB, lambda x,y: x*y, initial=1))[:-1]
    for c in range(math.prod(listOfUB)):
        step = []
        for i in range(len(listOfUB)):
            step.append(c//scanOfUB[i] % listOfUB[i])
        res.append(list(reversed(step)))
    return res

# "Tests"
# print(listDiff([1,2,3,4,5,6,7,8,9,10],[1,5,6,9,11]))
print(combinations([10,2,10,2]))