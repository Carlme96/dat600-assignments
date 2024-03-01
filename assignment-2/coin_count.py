def coin_count(coins, value):
    coins = sorted(coins, reverse=True)
    m = [0 for _ in range(value+1)]