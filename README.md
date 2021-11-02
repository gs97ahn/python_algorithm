# python_sorting_algorithm
## Selection Sort
Total Time Complexity = O(N<sup>2</sup>)

### Selection Sort ADL
```
selectionSort(a[], n)
  for (i <- 1, i < n; i <- i + 1) do {
    minIndex <- i;
    for (j <- i + 1; j <= n; j <- j + 1) do
      if (a[minIndex] > a[j]) then
        minIndex <- j;
    swap a[minIndex] and a[i];
  }
end selectionSort()
```

## Bubble Sort
Total Time Complexity = O(N<sup>2</sup>)

### Bubble Sort ADL
```
bubbleSort(a[], n)
  for (i <- n; i > 1; i <- i - 1) do
    for (j <- 1; j < i; j <- j + 1) do
      if (a[j] > a[j + 1]) then
        swap a[j] and a[j + 1];
end bubbleSort()
```

## Insertion Sort
Total Time Complexity = O(N<sup>2</sup>)

### Insertion Sort ADL
```
insertionSort(a[], n)
  for(i <- 2; i <= n; i <- i + 1) do {
    v <- a[i];
    j <- i;
    while(a[j - 1] > v) do {
      a[j] <- a[j - 1];
      j <- j - 1;
    }
    a[j] <- v;
  }
end insertionSort()
```
## Shell Sort
Total Time Complexity = O(N<sup>2</sup>)
### Shell Sort ADL
```
shellSort(a[], n)
  for(h <- 1; 3 * h + 1 < n; h <- 3 * h + 1) do { };
  for ( ; h > 0; h <- h / 3) do {
    for (i <- h + 1; i <= n; i <- i + 1) do {
      v <- a[i];
      j <- i;
      while(j > h and a[j - h] > v) do {
        a[j] <- a[j - h];
        j <- j - h;
      }
      a[j] <- v;
    }
  }
 end shellSort()
```

## Merege Sort
Total Time Complexity = O(N*LogN)
### Merge Sort ADL
```
mergeSort(a[], l, r)
  if (r > l) then {
    m <- (l + r) / 2;
    mergeSort(a[], l, m);
    mergeSort(a[], m + 1, r);
    merge(a[], l, m, r);
  }
end meregeSort()

merge(a[], l, m, r)
  i <- l; j <- m + 1; k <- l;
  while (i <= m and j <= r) do {
    if (a[i] < a[j]) then {
      b[k] <- a[i];
      k <- k + 1; i <- i + 1;
    }
    else {
      b[k] <- a[j];
      k <- k + 1; j <- j + 1;
    }
  }
  if (i > m) then
    for (p <- j; p <= r; p <- p + 1) do {
      b[k] <- a[p];
      k <- k + 1;
    }
    else
      for (p <- i; p <= m; p <- p + 1;) do {
        b[k] <- a[p];
        k <- k + 1;
      }
    for (p <- 1; p <= r; p <- p + 1) do
      a[p] <- b[p];
end merge()
```

## Quick Sort
Total Time Complexity = O(N*LogN)
### Quick Sort ADL
```
quickSort(a[], l, r)
  if (r > l) then {
    i <- partition(a[], l, r);
    quickSort(a[], l, i - 1);
    quickSort(a[], i + 1, r);
  }
end quickSort()

partition(a[], l, r)
  v <- a[r],
  i <- l - 1;
  j <- r;
  for ( ; ; ) do {
    do {i <- i + 1} while(a[i] < v);
    do {j <- j - 1} while(a[j] > v);
    if (i >= j) then break;
    swap a[i] and a[j];
  }
  swap a[i] and a[r];
  return i;
end partition()
```

## Heap Sort
Total Time Complexity = O(N*LogN)
### Heap Sort ADL
```
shellSort(a[], n)
  for (h <- 1; 3 * h + 1 < n; h <- 3 * h + 1) do { };
  for ( ; h > 0; h <- h / 3) do {
    for (i <- h + 1; i <= n; i <- i + 1) do {
      v <- a[i];
      j <- i;
      while (j > h and a [j - h] > v) do {
        a[j] <- a[j - h];
        j <- j - h;
      }
      a[j] <- v;
    }
  }
end shellSort()
```

## Radix Sort
Total Time Complexity = O(N)

## Counting Sort
Total Time Complexity = O(N + K)
