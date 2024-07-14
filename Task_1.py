import time

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        if amount >= coin:
            num_coins = amount // coin
            amount -= num_coins * coin
            result[coin] = num_coins

    return result

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    min_coins = [0] + [float('inf')] * amount
    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

# Performance measurement
def measure_performance(amount):
    start_time = time.time()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.time() - start_time

    start_time = time.time()
    dp_result = find_min_coins(amount)
    dp_time = time.time() - start_time

    return greedy_time, dp_time

# Measure performance for different amounts
amounts = [100, 1000, 5000, 10000, 20000, 50000, 100000]
performance_results = {}

for amount in amounts:
    greedy_time, dp_time = measure_performance(amount)
    performance_results[amount] = (greedy_time, dp_time)

# Print performance results
for amount, times in performance_results.items():
    print(f"Amount: {amount}, Greedy Time: {times[0]:.6f}s, DP Time: {times[1]:.6f}s")

print (find_coins_greedy(amount))
print (find_min_coins(amount))