#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```
on(n) the number of operation increases to n-1 as the nu increases

b)
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```
Each element in i has to perform n operation in jloop. This n * n operations O(n2)

c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

n operations are formed since this is a recursive function ( bunnies-1).
O(n)

## Exercise II


