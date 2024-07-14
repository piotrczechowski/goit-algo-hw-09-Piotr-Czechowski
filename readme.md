# Cash Register System

This project includes two functions to determine the best way to give change to a customer using a set of coin denominations [50, 25, 10, 5, 2, 1].

## Functions

### `find_coins_greedy`

This function implements a greedy algorithm to give change. It takes the largest available coin denominations first.

- **Input**: An integer representing the amount of change to be given.
- **Output**: A dictionary with the number of coins of each denomination used to make up the amount.

**Example**:
```python
amount = 113
result = find_coins_greedy(amount)
print(result)  # Output: {50: 2, 10: 1, 2: 1, 1: 1}

# Recomendation 

For large sums, the dynamic programming approach ensures the minimum number of coins, but it is computationally expensive. The greedy algorithm, while faster, may not always yield the optimal solution for all coin sets but is very efficient in terms of execution time.

Recommendations
Use the greedy algorithm for quick, efficient solutions where coin denominations are favorable.
Use the dynamic programming approach when the optimal solution is required, and computational resources allow for it.