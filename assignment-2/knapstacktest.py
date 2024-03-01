from typing import List, Tuple
import random

def generate_items(num_items: int) -> List[Tuple[int, int]]:
    """Generate a list of items represented as (weight, value) tuples."""
    return [(random.randint(1, 10), random.randint(10, 100)) for _ in range(num_items)]

def knapsack_01_dp(items: List[Tuple[int, int]], max_capacity: int) -> Tuple[int, List[int]]:
    """Solve the 0-1 knapsack problem using dynamic programming."""
    n = len(items)
    dp = [[0 for x in range(max_capacity + 1)] for x in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, max_capacity + 1):
            if items[i-1][0] <= w:
                dp[i][w] = max(items[i-1][1] + dp[i-1][w-items[i-1][0]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
                
    # Find the items included in the optimal solution
    solution_items = []
    w = max_capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            solution_items.append(i-1)
            w -= items[i-1][0]
    
    return dp[n][max_capacity], solution_items

def knapsack_fractional_greedy(items: List[Tuple[int, int]], max_capacity: int) -> Tuple[float, List[Tuple[int, float]]]:
    """Solve the fractional knapsack problem using a greedy algorithm."""
    # Sort items by value-to-weight ratio in descending order
    items_sorted = sorted(items, key=lambda x: x[1]/x[0], reverse=True)
    total_value = 0.0
    capacity_remaining = max_capacity
    solution_items = []
    
    for i, (weight, value) in enumerate(items_sorted):
        if capacity_remaining >= weight:
            # Take the whole item
            total_value += value
            solution_items.append((i, 1.0))  # (item index, fraction taken)
            capacity_remaining -= weight
        else:
            # Take a fraction of the item
            fraction = capacity_remaining / weight
            total_value += value * fraction
            solution_items.append((i, fraction))
            break  # The knapsack is full
    
    return total_value, solution_items

# Example usage
num_items = 5
max_capacity = 15
items = generate_items(num_items)

# Solve 0-1 Knapsack
value_01, solution_01 = knapsack_01_dp(items, max_capacity)

# Solve Fractional Knapsack
value_frac, solution_frac = knapsack_fractional_greedy(items, max_capacity)

items, (value_01, solution_01), (value_frac, solution_frac)
