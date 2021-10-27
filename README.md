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

## Quick Sort
Total Time Complexity = O(N*LogN)

## Heap Sort
Total Time Complexity = O(N*LogN)

## Radix Sort
Total Time Complexity = O(N)
