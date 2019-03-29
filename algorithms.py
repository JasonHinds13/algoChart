import time
import random

mi = 0
ma = 10
N = [10,50,100,500,1000,5000,10000]

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

def selectionSort(alist):
    newList = alist
    for fillslot in range(len(newList)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if newList[location]>newList[positionOfMax]:
                positionOfMax = location
        temp = newList[fillslot]
        newList[fillslot] = newList[positionOfMax]
        newList[positionOfMax] = temp
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
    algo("Selection Sort", selectionSort)
    return results

#print runAlgorithms()
