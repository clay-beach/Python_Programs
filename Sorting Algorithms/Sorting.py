# Import Statements
import random
import time

# Question 10/11 Bubble sort algorithm
def bubbleSort(ll):
    for i in range(len(ll)-1, 0, -1):
        for j in range(i):
            if ll[j] > ll[j + 1]:
                ll[i] = ll[j]
                ll[j] = ll[j + 1]
                ll[j + 1] = ll[i]
# End BubbleSort

# Question 12 Implement the selection sort using simultaneous assignment.
def selectionSort(ll):
    for i in range(len(ll)-1, 0, -1):
        max = 0
        for location in range(1, i + 1):
            if ll[location] > ll[max]:
                max = location
        temp = ll[i]
        ll[i] = ll[max]
        ll[max] = temp
# End selectionSort

# Question 14 Implement the mergeSort function without using the slice operator.
def mergeSort(ll):
    if len(ll) > 1:
        # find midpoint of list
        mid = len(ll) // 2
        # Splits list to left and right of mid
        left = ll[:mid]
        right = ll[mid:]
        # Calls mergeSort Function on splits
        mergeSort(left)
        mergeSort(right)
        # Ordering the lists
        # K is counter, I is left, j is right
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                ll[k] = left[i]
                i += 1
            else:
                ll[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            ll[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            ll[k] = right[j]
            j += 1
            k += 1

# Main
n = 1000
min, max = 0, n
trials = 10
sumTime = 0
exe = 0

random.seed(1234)
for i in range(trials):
    testList = [random.randint(min, max) for num in range(n)]
    start = time.time()
    bubbleSort(testList)
    end = time.time()
    exe = end - start
    sumTime += exe
print("Sorting took exe%.2f" % exe + "Seconds on average for BubbleSort")

for j in range(trials):
    testList = [random.randint(min, max) for number in range(n)]
    start = time.time()
    selectionSort(testList)
    end = time.time()
    exe = end - start
    sumTime += exe
print("Sorting took exe%.2f" % exe + "Seconds on average for selectionSort")

for k in range(trials):
    testList = [random.randint(min, max) for numeral in range(n)]
    start = time.time()
    mergeSort(testList)
    end = time.time()
    exe = end - start
    sumTime += exe
print("Sorting took exe%.2f" % exe + "Seconds on average for mergeSort")
