# 계수 정렬(counting sort)
def countingSort(a, n, m):
    b = [0] * (n + 1)
    count = [0] * (m + 1)
    for j in range(1, m + 1):
        count[j] = 0
    for i in range(1, n + 1):
        count[a[i]] += 1
    for j in range(2, m + 1):
        count[j] += count[j - 1]
    for i in range(n, 0, -1):
        b[count[a[i]]] = a[i]
        count[a[i]] -= 1
    for i in range(1, n + 1):
        a[i] = b[i]

def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if (a[i] > a[i + 1]):
            isSorted = False
        if (not isSorted):
            break
    if isSorted:
        print("Sorting complete")
    else:
        print("Sorting error occurred")

import random, time

M = 1000
N = 300000
a = []
a.append(None)
for i in range(N):
    a.append(random.randint(1, M))
start_time = time.time()
countingSort(a, N, M)
end_time = time.time() - start_time
print('Counting Sort process time (N=%d) : %0.3f' %(N, end_time))
checkSort(a, N)