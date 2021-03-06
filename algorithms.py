import sys
import time
import random

sys.setrecursionlimit(1000)

mi = 0
ma = 10
#N = [10,50,100,500,1000,5000,10000]
N = [1000,2000,3000,4000,5000,7000,9000,10000]

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
    newList = alist[:]
    for passnum in range(len(newList)-1,0,-1):
        for i in range(passnum):
            if newList[i]>newList[i+1]:
                temp = newList[i]
                newList[i] = newList[i+1]
                newList[i+1] = temp
    return newList

def selectionSort(alist):
    newList = alist[:]
    for fillslot in range(len(newList)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if newList[location]>newList[positionOfMax]:
                positionOfMax = location
        temp = newList[fillslot]
        newList[fillslot] = newList[positionOfMax]
        newList[positionOfMax] = temp
    return newList

def insertion_sort(ar, simulation=False):
    arr = ar[:]
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        while pos > 0 and arr[pos - 1] > cursor:
            # Swap the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        # Break and do the final swap
        arr[pos] = cursor
    return arr

## Merge Sort functions
def merge_sort(ar):
    arr = ar[:]
    # The last array split
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # Perform merge_sort recursively on both halves
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    # Merge each side together
    return merge(left, right, list(arr))


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
            
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
        
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]
    return merged

## Quick Sort functions
def partition(arr,l,h): 
    i = ( l - 1 ) 
    x = arr[h] 
  
    for j in range(l , h): 
        if   arr[j] <= x: 
  
            # increment index of smaller element 
            i = i+1
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[h] = arr[h],arr[i+1] 
    return (i+1) 

def quickSort(ar,l=0,h=None):
    arr = ar[:]
    if h == None:
        h = len(arr)-1
    size = h - l + 1
    stack = [0] * (size)
    top = -1
    top = top + 1
    stack[top] = l 
    top = top + 1
    stack[top] = h
    while top >= 0:
        h = stack[top] 
        top = top - 1
        l = stack[top] 
        top = top - 1
        p = partition( arr, l, h )
        if p-1 > l: 
            top = top + 1
            stack[top] = l 
            top = top + 1
            stack[top] = p - 1
        if p+1 < h: 
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h 
    return arr

# Run an algorithm with each list we've created and store the results
def algo(name, f):
    print("Running: " +name)
    results[name] = []
    for l in lis:
        start = time.time()
        f(l[:])
        stop = time.time()
        results[name].append((len(l), stop - start))

# Run all the algorithms
def runAlgorithms():
    algo("Bubble Sort", bubbleSort)
    algo("Selection Sort", selectionSort)
    algo("Insertion Sort", insertion_sort)
    algo("Merge Sort", merge_sort)
    algo("Quick Sort", quickSort)
    return results

#print runAlgorithms()
