# Umesh Dhakal
# MSCS532A4
# Comparison of Heap sort to Merge Sort and Quick Sort

import random
import time
import tracemalloc
import sys
sys.setrecursionlimit(5000)

#Merge Sort Implementation
def Mergesort(arraylist):
    if len(arraylist) <= 1:
        return arraylist
    middlelocation = len(arraylist) // 2
    lefthalf = Mergesort(arraylist[:middlelocation])
    righthalf = Mergesort(arraylist[middlelocation:])
    return merge(lefthalf, righthalf)

def merge(lefthalf, righthalf):
    output = []
    a = b = 0
    while a < len(lefthalf) and b < len(righthalf):
        if lefthalf[a] >= righthalf[b]:
            output.append(lefthalf[a]); a += 1
        else:
            output.append(righthalf[b]); b += 1
    output.extend(lefthalf[a:]); output.extend(righthalf[b:])
    return output

#Quick sort Implementation
def partition(arraylist, low, high):
    pivot = arraylist[high]
    i = low - 1
    for j in range(low, high):
        if arraylist[j] <= pivot:
            i += 1
            arraylist[i], arraylist[j] = arraylist[j], arraylist[i]
    arraylist[i+1], arraylist[high] = arraylist[high], arraylist[i+1]
    return i+1

def Quicksort(arraylist, low=0, high=None):
    if high is None: high = len(arraylist)-1
    if low < high:
        p = partition(arraylist, low, high)
        Quicksort(arraylist, low, p-1)
        Quicksort(arraylist, p+1, high)
    return arraylist

#Heap sort Implementation
def heapify(arraylist, number, a):
    parent = a
    left = 2*a + 1
    right = 2*a + 2
    if left < number and arraylist[left] > arraylist[parent]:
        parent = left
    if right < number and arraylist[right] > arraylist[parent]:
        parent = right
    if parent != a:
        arraylist[a], arraylist[parent] = arraylist[parent], arraylist[a]
        heapify(arraylist, number, parent)

def Heapsort(arraylist):
    number = len(arraylist)
    for a in range(number//2 - 1, -1, -1):
        heapify(arraylist, number, a)
    for a in range(number-1, 0, -1):
        arraylist[0], arraylist[a] = arraylist[a], arraylist[0]
        heapify(arraylist, a, 0)
    return arraylist
# Performance Measurement
def run(algorithm, dataset, dataset_name):
    tracemalloc.start()
    starttime = time.time()
    if algorithm.__name__ == "Quicksort":
        algorithm(dataset[:], 0, len(dataset)-1)
    else:
        algorithm(dataset[:])
    endtime = time.time()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"{algorithm.__name__} on {dataset_name} took {endtime-starttime:.4f} seconds with memory usage {peak/1024:.2f} KB")

# Testing Data
test_data = 2000
datasets = {
    "Sorted Data": list(range(test_data, 0, -1)),
    "Reverse Data": list(range(1, test_data+1)),
    "Random Data": [random.randint(1, test_data) for _ in range(test_data)]
}

print("\nComparing Heapsort, Mergesort and Quicksort")
for dataset_name, dataset in datasets.items():
    run(Heapsort, dataset, dataset_name)
    run(Mergesort, dataset, dataset_name)
    run(Quicksort, dataset, dataset_name)