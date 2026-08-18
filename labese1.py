import time
import os

def clear_terminal():
    # Clears the terminal for an animation effect
    os.system('cls' if os.name == 'nt' else 'clear')

def print_table(dp, current_i, current_w, weights, values, capacity):
    # We only print columns that are multiples of 10 so it fits in the terminal
    columns = list(range(0, capacity + 1, 10))
    
    print("\n--- 0/1 Knapsack DP Table ---")
    
    # Print Header
    header = "       " + "".join([f" W={c:<3} " for c in columns])
    print(header)
    print("      " + "-" * (len(header) - 5))
    
    for i in range(len(dp)):
        if i == 0:
            row_str = "i=0  | "
        else:
            row_str = f"i={i}  | "
            
        for w in columns:
            val = dp[i][w]
            # Highlight the cell currently being calculated in Green
            if i == current_i and w == current_w:
                row_str += f"\033[92m{val:^6}\033[0m" # \033[92m is ANSI Green
            else:
                row_str += f"{val:^6}"
        print(row_str)
    print("\n")

def knapsack_01_visualized(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                # Include or leave
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                # Leave
                dp[i][w] = dp[i-1][w]
            
            # Update the visualization ONLY for multiples of 10 to avoid terminal spam
            if w % 10 == 0:
                clear_terminal()
                print(f"Current Item: {i} (Weight: {weights[i-1]}, Value: {values[i-1]})")
                print(f"Checking Capacity: {w}")
                
                # Check which decision was made to explain the logic on screen
                if weights[i-1] <= w:
                    take_val = values[i-1] + dp[i-1][w-weights[i-1]]
                    leave_val = dp[i-1][w]
                    if take_val > leave_val:
                        print(f"Decision: \033[92mTAKE IT\033[0m (Max value becomes {take_val})")
                    else:
                        print(f"Decision: \033[93mLEAVE IT\033[0m (Previous max {leave_val} is better)")
                else:
                    print(f"Decision: \033[91mTOO HEAVY\033[0m (Must leave it)")

                print_table(dp, i, w, weights, values, capacity)
                time.sleep(0.8) # Pause for 0.8 seconds to create animation

    return dp[n][capacity]

# Run the visualization
if __name__ == "__main__":
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50

    print("Starting Knapsack Visualization in 3 seconds...")
    time.sleep(3)
    
    max_value = knapsack_01_visualized(weights, values, capacity)
    
    print("="*40)
    print(f"\033[92mCOMPLETE! The maximum value is: {max_value}\033[0m")
    print("="*40)