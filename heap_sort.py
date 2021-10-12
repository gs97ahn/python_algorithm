# 히프 정렬(heap sort)
def heapify(a, h, m):
    v, j = a[h], 2 * h
    while j <= m:
        if j < m and a[j] < a[j + 1]:
            j += 1
        if v >= a[j]:
            break
        else:
            a[int(j/2)] = a[j]
        j *= 2
    a[int(j/2)] = v

def heapSort(a, n):
    for i in range(int(n / 2), 0, -1):
        heapify(a, i, n)
    for i in range(n - 1, 0, -1):
        a[1], a[i + 1] = a[i + 1], a[1]
        heapify(a, 1, i)

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

N = 100000
a = []
a.append(None)
for i in range(N):
    a.append(random.randint(1, N))
b = a.copy()
start_time = time.time()
heapSort(a, N)
end_time = time.time() - start_time
print("Heap sort process times (N=%d) : %0.3f" %(N, end_time))
checkSort(a, N)