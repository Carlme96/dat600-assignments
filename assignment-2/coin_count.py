def coin_count(coins, value):
    num_coins = [float('inf') for _ in range(value + 1)]
    num_coins[0] = 0
    
    for i in range(1, value + 1):
        for coin in coins:
            if i - coin >= 0:
                num_coins[i] = min(num_coins[i], num_coins[i - coin] + 1)

    
    
    return num_coins[-1]


if __name__ == '__main__':
    coins = [1, 5, 11]
    value = 15
    print(coin_count(coins, value)) # 2