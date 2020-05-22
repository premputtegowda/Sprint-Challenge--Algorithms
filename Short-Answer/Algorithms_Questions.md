# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```


```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

base case: if we have one egg the worst case scenario is n tries ( n floors)

otherwise it leaves with two possibilities in each floor:
case 1: egg breaks
case 2: egg doesn't break

### case 1:

if egg breaks on the fth floor(n is total number of floor)
    floors to work with: (f-1), eggs = eggs-1

### case 2:
    if egg doesn't break we will have:
    floors: (n-f), eggs: eggs

each floor will have these case and generalizint it
f(floors, eggs) =minimum of (sum of (1 + max(f(floor # -1, eggs), f(Floors-f), eggs-1)))

1 is added to the function max( of the function given above) since throwing an egg is considered as 1 attemp..
max value is derived from (case1, case2) because we need the worst possible case

time complexity O(N log n) since we need to traverse through each floor and each floor is cut in half ( case 1 where the egg breaks, case 2: egg doesn't break)
space O(C)? 
