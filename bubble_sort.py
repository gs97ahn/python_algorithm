# 버블 정렬(bubble sort)
def bubbleSort(a, n):
    for i in range(n, 0, -1):
        for j in range(1, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

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

N = 5000
a = []
a.append(None)
for i in range(N):
    a.append(random.randint(1, N))
start_time = time.time()
bubbleSort(a, N)
end_time = time.time() - start_time
print('Bubble sort process time (N=%d) : %0.3f'%(N, end_time))
checkSort(a, N)