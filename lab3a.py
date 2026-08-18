def calculate_knapsack():
    # Setup the problem variables
    budget_capacity = 5
    weights = [2, 1, 3, 2]       # Cost Units
    values = [30, 20, 40, 25]    # Importance
    items = ["E1", "E2", "E3", "E4"]
    n = len(values)

    # Initialize a 2D DP table with 0s
    dp_table = [[0 for _ in range(budget_capacity + 1)] for _ in range(n + 1)]

    # Build the table in a bottom-up manner
    for i in range(n + 1):
        for w in range(budget_capacity + 1):
            if i == 0 or w == 0:
                dp_table[i][w] = 0
            elif weights[i - 1] <= w:
                # Max of including the item vs excluding it
                dp_table[i][w] = max(values[i - 1] + dp_table[i - 1][w - weights[i - 1]], dp_table[i - 1][w])
            else:
                # Item weight exceeds current capacity, exclude it
                dp_table[i][w] = dp_table[i - 1][w]

    # Print the DP Table
    print("DP Table:")
    for row in dp_table:
        # Format the row with tabs for clean alignment
        print("\t".join(map(str, row)))

    # Backtrack to find the selected items
    max_value = dp_table[n][budget_capacity]
    current_capacity = budget_capacity
    selected_items = []

    for i in range(n, 0, -1):
        if max_value <= 0:
            break
        # If the value is different from the row directly above, the item was included
        if max_value != dp_table[i - 1][current_capacity]:
            selected_items.append(items[i - 1])
            max_value -= values[i - 1]
            current_capacity -= weights[i - 1]

    # The items are found in reverse order during backtracking, so we reverse the list
    selected_items.reverse()

    # Print the final results
    print("\nSelected Items:", " ".join(selected_items))
    print("Maximum Total Value:", dp_table[n][budget_capacity])

if __name__ == "__main__":
    calculate_knapsack()