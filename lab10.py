def print_matrix(matrix, n, step_name):
    """Prints the distance matrix with clear formatting and step labeling."""
    print(f"\nMatrix {step_name}:")
    header = "      " + "   ".join([f"V{i}" for i in range(n)])
    print(header)
    print("   " + "-" * (len(header)))
    for i in range(n):
        row = f"V{i} | "
        for j in range(n):
            val = matrix[i][j]
            if val == float("inf"):
                row += f"{'INF':>4} "
            else:
                row += f"{val:>4} "
        print(row)
    print("   " + "-" * (len(header)))

def floyd_warshall():
    """
    Floyd-Warshall Algorithm with Step-by-Step Matrix Visualization.
    - Time Complexity: O(V^3)
    - Space Complexity: O(V^2)
    - Optimization: Matrix D(k) depends only on D(k-1).
    """
    print("=" * 50)
    print("   FLOYD-WARSHALL ALL-PAIRS SHORTEST PATH")
    print("=" * 50)
    
    try:
        n = int(input("Enter number of vertices: "))
        if n <= 0:
            print("Error: Number of vertices must be positive.")
            return

        # Step 1: Initialize Distance Matrix D(0)
        # 0 for self-loops, weight for edges, INF for no direct path
        dist = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        e = int(input("Enter number of edges: "))
        print("\nEnter edges as (source destination weight).")
        print("Example: '0 1 5' is an edge from V0 to V1 with weight 5.")
        
        for i in range(e):
            try:
                u, v, w = map(int, input(f"Edge {i+1}: ").split())
                if 0 <= u < n and 0 <= v < n:
                    dist[u][v] = w
                else:
                    print(f"Skipping invalid edge: V{u}->V{v} (Valid range: 0 to {n-1})")
            except ValueError:
                print("Invalid format. Please enter three integers.")
                return

        # Show initial state (D0)
        print_matrix(dist, n, "D(0) - Initial Direct Distances")

        # Step 2: Dynamic Programming Passes
        # Iterate through every vertex k as an intermediate point
        for k in range(n):
            print(f"\nIterating with intermediate vertex V{k}...")
            
            # Update paths: dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            for i in range(n):
                for j in range(n):
                    if dist[i][k] != float("inf") and dist[k][j] != float("inf"):
                        if dist[i][k] + dist[k][j] < dist[i][j]:
                            dist[i][j] = dist[i][k] + dist[k][j]
            
            # Print intermediate matrix for the lab record
            print_matrix(dist, n, f"D({k+1})")

        # Step 3: Check for Negative Cycles
        for i in range(n):
            if dist[i][i] < 0:
                print("\n[!] Error: Graph contains a negative weight cycle.")
                print(f"Vertex V{i} can reach itself with negative cost {dist[i][i]}.")
                return

        print("\n" + "=" * 50)
        print("ALGORITHM COMPLETE: All-pairs shortest paths found.")
        print("=" * 50)

    except ValueError:
        print("\nError: Please enter integer values.")

if __name__ == "__main__":
    floyd_warshall()
