class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = []    # List to store graph edges

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellman_ford(self, src):
        # Step 1: Initialize distances from src as infinite
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Step 2: Relax all edges |V| - 1 times
        # Optimization: If no distance is updated in an iteration, we can stop early.
        for i in range(self.V - 1):
            changed = False
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    changed = True
            
            if not changed:
                print(f"Algorithm converged early at iteration {i+1}.")
                break
        else:
            # Step 3: Check for negative-weight cycles
            # This only runs if the loop didn't break early
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    print("\nError: Graph contains a negative weight cycle!")
                    return

        self.print_solution(src, dist)

    def print_solution(self, src, dist):
        print(f"\nShortest Path Results (Source: Vertex {src})")
        print("-" * 40)
        print(f"{'Vertex':<10} {'Distance from Source':<20}")
        print("-" * 40)
        for i in range(self.V):
            d = dist[i] if dist[i] != float("Inf") else "Unreachable"
            print(f"{i:<10} {d:<20}")
        print("-" * 40)

def main():
    print("--- Bellman-Ford Shortest Path Solver ---")
    try:
        v_count = int(input("Enter number of vertices: "))
        e_count = int(input("Enter number of edges: "))
        g = Graph(v_count)

        print("\nEnter edges in format (source destination weight).")
        print("Example: '0 1 -5' means an edge from Vertex 0 to Vertex 1 with weight -5.")
        for i in range(e_count):
            try:
                u, v, w = map(int, input(f"Edge {i+1}: ").split())
                if u < 0 or u >= v_count or v < 0 or v >= v_count:
                    print(f"Error: Vertices must be between 0 and {v_count-1}. Please try again.")
                    # Restart the loop for this edge
                    u, v, w = map(int, input(f"Edge {i+1} (retry): ").split())
                g.add_edge(u, v, w)
            except ValueError:
                print("Invalid edge format. Please use 'u v w'.")
                return

        src = int(input("\nEnter the source vertex: "))
        if src < 0 or src >= v_count:
            print(f"Source vertex must be between 0 and {v_count-1}.")
            return
            
        g.bellman_ford(src)

    except ValueError:
        print("Invalid input. Please enter integers.")

if __name__ == "__main__":
    main()
