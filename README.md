# python_algorithm
## Selection Sort
Total Time Complexity = O(N<sup>2</sup>)

```python
ADL
selectionSort(a[], n)
  for (i <- 1, i < n; i <- i + 1) do {
    minIndex <- i;
    for (j <- i + 1; j <= n; j <- j + 1) do
      if (a[minIndex] > a[j]) then
        minIndex <- j;
    swap a[minIndex] and a[i];
  }
```

## Bubble Sort
Total Time Complexity = O(N<sup>2</sup>)

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
