import sys
import time

def print_board(board, n):
    """Prints the board with row and column labels."""
    header = "   " + " ".join([f"C{i+1}" for i in range(n)])
    print(header)
    for i in range(n):
        row_str = "  ".join(board[i])
        print(f"R{i+1}  {row_str}")
    print("-" * (len(header) + 2))

def solve_n_queens():
    try:
        n_input = input("Enter the value of N (e.g., 4): ")
        if not n_input: return
        n = int(n_input)
        
        show_steps_input = input("Show step-by-step process? (y/n): ").lower()
        show_steps = show_steps_input == 'y'
        
    except (ValueError, EOFError):
        print("\nInvalid input.")
        return

    solutions = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    cols, diag1, diag2 = set(), set(), set()

    def backtrack(row):
        if row == n:
            solutions.append([list(r) for r in board])
            if show_steps:
                print("\n*** SOLUTION FOUND! ***")
            return

        for col in range(n):
            if show_steps:
                print(f"\nTrying Row {row+1}, Column {col+1}...")

            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue

            # Place queen
            board[row][col] = 'Q'
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            if show_steps:
                print(f"Placed Queen at R{row+1}C{col+1}:")
                print_board(board, n)
                time.sleep(0.3) # Pause for readability

            backtrack(row + 1)

            # Backtrack: Remove queen
            board[row][col] = '.'
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

            if show_steps:
                print(f"Backtracking: Removing Queen from R{row+1}C{col+1}")
                print_board(board, n)

    print(f"\nSearching for solutions for {n}-Queens...")
    backtrack(0)

    print(f"\nSearch Complete. Total solutions found: {len(solutions)}")
    
    if not show_steps and solutions:
        print("\nFinal Solutions:")
        for i, sol in enumerate(solutions[:10]):
            print(f"\nSolution {i+1}:")
            print_board(sol, n)

if __name__ == "__main__":
    solve_n_queens()
