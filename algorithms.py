import time
import random

mi = 0
ma = 10
N = [10,100,1000,10000]

# Will hold the lists of numbers to run algorithms on
# e.g. lis = [[1,2,3,...], [4,7,3,...], ...]
lis = []

# Will hold the results of each run for each algorithm
# e.g. results = {'nameOfAlgo': [(numOfElements, timeRan),...]}
results = {}

# Generate Lists of numbers each with a different number of elements
for n in N:
    lis.append([random.randint(mi,ma) for x in range(n)])

def bubbleSort(alist):
    newList = alist
    for passnum in range(len(newList)-1,0,-1):
        for i in range(passnum):
            if newList[i]>newList[i+1]:
                temp = newList[i]
                newList[i] = newList[i+1]
                newList[i+1] = temp
    return newList

# Run an algorithm with each list we've created and store the results
def algo(name, f):
    results[name] = []
    for l in lis:
        start = time.time()
        f(l)
        stop = time.time()
        results[name].append((len(l), stop - start))

# Run all the algorithms
def runAlgorithms():
	algo("Bubble Sort", bubbleSort)
	return results

#print runAlgorithms()