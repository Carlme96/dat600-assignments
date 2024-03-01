import random

def knapsack01(items, W):
    n = len(items)
    m = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(1, n+1):
        for w in range(1, W+1):
            if items[i-1]['weight'] <= w:
                m[i][w] = max(m[i-1][w], m[i-1][w-items[i-1]['weight']] + items[i-1]['value'])
            else:
                m[i][w] = m[i-1][w]
    
    solution_items = []
    w = W
    for i in range(n, 0, -1):
        if m[i][w] != m[i-1][w]:
            solution_items.append(i-1)
            w -= items[i-1]['weight']
    
    return m[n][W], solution_items

def knapsackfrac(items, W):
    items = sorted(items, key=lambda x: x['value']/x['weight'], reverse=True)
    total = 0
    solution_items = []
    
    for i, item in enumerate(items):
        if W >= item['weight']:
            total += item['value']
            solution_items.append((i, 1))
            W -= item['weight']
        else:
            total += item['value'] * (W / item['weight'])
            solution_items.append((i, W / item['weight']))
            break
    
    return total, solution_items

def knapsack(wunit, vunit, max_capacity, num_items):
    items = [{id: i, 'weight': random.randint(1, max_capacity*1), 'value': random.randint(1, 1000)} for i in range(num_items)]
    total_01, solution_01 = knapsack01(items, max_capacity)
    total_frac, solution_frac = knapsackfrac(items, max_capacity)

    for i, item in enumerate(items):
        print(f"Item {item[id]}: {item['weight']:.2f} {wunit}, ${item['value']} {vunit}") 

    print(f"\n0-1 Knapsack: Total value = ${total_01}\n")
    for i in solution_01:
        print(f"Item {items[i][id]}: {items[i]['weight']:.2f} {wunit}, ${items[i]['value']} {vunit}\n")

    print(f"\nFractional Knapsack: Total value = ${total_frac:.2f}\n")
    for i, fraction in solution_frac:
        print(f"Item {items[i][id]}: {items[i]['weight']:.2f} {wunit}, ${items[i]['value']} {vunit} ({fraction:.2f})\n")
    




if __name__ == "__main__":
    knapsack("kg", "$", 15, 5)