import sys
# matrix chain multiplicaton
def print_table(m, n):
    print("\nCurrent DP Table (m):")
    for i in range(1, n):
        for j in range(1, n):
            if j < i:
                print("   -   ", end="")
            else:
                print(f"{m[i][j]:6}", end=" ")
        print()
    print()


# Function to find minimum number of multiplications
def matrix_chain_order(p, n):
    m = [[0 for _ in range(n)] for _ in range(n)]
    s = [[0 for _ in range(n)] for _ in range(n)]

    for L in range(2, n):
        print(f"\n🔹 Computing chain length L = {L}")

        for i in range(1, n - L + 1):
            j = i + L - 1
            m[i][j] = sys.maxsize

            print(f"\nEvaluating m[{i}][{j}]:")

            for k in range(i, j):
                q = (m[i][k] + m[k + 1][j] +
                     p[i - 1] * p[k] * p[j])

                print(f"  Split at k={k}: Cost = {m[i][k]} + {m[k+1][j]} + "
                      f"{p[i-1]}*{p[k]}*{p[j]} = {q}")

                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

            print(f"Minimum cost for m[{i}][{j}] = {m[i][j]}")

        print_table(m, n)

    return m, s


# Function to print optimal parenthesization
def print_optimal_parens(s, i, j):
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")


# Driver Code
if __name__ == "__main__":
    p = [30, 35, 15, 5, 10, 20, 25]
    n = len(p)

    m, s = matrix_chain_order(p, n)

    print("\n Final DP Table:")
    print_table(m, n)

    print("Minimum number of multiplications:", m[1][n - 1])
    print("Optimal Parenthesization:", end=" ")
    print_optimal_parens(s, 1, n - 1)