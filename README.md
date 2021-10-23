# python_algorithm
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

## Shell Sort
Total Time Complexity = O(N<sup>2</sup>)

## Merege Sort
Total Time Complexity = O(N*LogN)

## Quick Sort
Total Time Complexity = O(N*LogN)

## Heap Sort
Total Time Complexity = O(N*LogN)

## Radix Sort
Total Time Complexity = O(N)
