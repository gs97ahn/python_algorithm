# 삽입 정렬(insertion sort)
def insertionSort(a, n):
    for i in range(2, n+1):
        v, j = a[i], i
        while a[j-1] > v:
            a[j] = a[j-1]
            j -= 1
        a[j] = v

def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if (a[i] > a[i+1]):
            isSorted = False
        if (not isSorted):
            break
    if isSorted:
        print("Sorting complete")
    else:
        print("Sorting error occurred")

import random, time

N = 10000
a = []
a.append(-1)
for i in range(N):
    a.append(random.randint(1, N))
start_time = time.time()
insertionSort(a, N)
end_time = time.time() - start_time
print('Insertion sort process time (N=%d) : %0.3f'%(N, end_time))
checkSort(a, N)