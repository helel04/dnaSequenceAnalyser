import time

# -------------------------------
# Fractional Knapsack
# -------------------------------
def fractional_knapsack(capacity, items):
    items = sorted(items, key=lambda x: x[0]/x[1], reverse=True)
    total_value = 0.0

    for value, weight in items:
        if capacity >= weight:
            capacity -= weight
            total_value += value
        else:
            total_value += value * (capacity / weight)
            break

    return total_value


# -------------------------------
# Greedy 0/1 Knapsack
# -------------------------------
def greedy_01_knapsack(capacity, items):
    items = sorted(items, key=lambda x: x[0]/x[1], reverse=True)
    total_value = 0

    for value, weight in items:
        if capacity >= weight:
            capacity -= weight
            total_value += value

    return total_value


# -------------------------------
# Dynamic Programming 0/1 Knapsack
# -------------------------------
def dp_knapsack(capacity, values, weights):
    n = len(values)
    dp = [[0]*(capacity+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, capacity+1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]],
                               dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]


# -------------------------------
# Case Testing Function
# -------------------------------
def run_case(items, capacity):
    values = [i[0] for i in items]
    weights = [i[1] for i in items]

    print("\nItems:", items)
    print("Capacity:", capacity)

    # Fractional
    start = time.time()
    frac_profit = fractional_knapsack(capacity, items)
    frac_time = time.time() - start

    # Greedy 0/1
    start = time.time()
    greedy_profit = greedy_01_knapsack(capacity, items)
    greedy_time = time.time() - start

    # DP 0/1
    start = time.time()
    dp_profit = dp_knapsack(capacity, values, weights)
    dp_time = time.time() - start

    print("\n--- Results ---")
    print(f"Fractional Knapsack Profit: {frac_profit:.2f}, Time: {frac_time:.6f}s")
    print(f"Greedy 0/1 Profit: {greedy_profit}, Time: {greedy_time:.6f}s")
    print(f"DP 0/1 Profit: {dp_profit}, Time: {dp_time:.6f}s")


# -------------------------------
# Test Cases
# -------------------------------
case1 = [(60, 10), (100, 20), (120, 30)]
capacity1 = 50

case2 = [(10, 5), (40, 4), (30, 6), (50, 3)]
capacity2 = 10

# Run cases
run_case(case1, capacity1)
run_case(case2, capacity2)