import heapq
import random

class TSPSolver:
    def __init__(self, adj_matrix):
        self.matrix = adj_matrix
        self.n = len(adj_matrix)
        self.best_cost = float('inf')
        self.optimal_paths = []
        self.nodes_explored = 0
        self.nodes_pruned = 0

    def get_lower_bound(self, path):
        bound = 0
        for i in range(self.n):
            if i not in path or i == path[-1]:
                # Extract edges, ignoring self-loops (0 or INF)
                edges = sorted([self.matrix[i][j] for j in range(self.n) if i != j])
                if len(edges) >= 2:
                    bound += (edges[0] + edges[1])
        return (bound + 1) // 2

    def solve(self):
        pq = []
        start_node = 0
        initial_bound = self.get_lower_bound([start_node])
        heapq.heappush(pq, (initial_bound, 0, start_node, [start_node]))

        print(f"\n[SYSTEM] Starting Branch and Bound Exploration...")
        
        while pq:
            estimated_cost, current_cost, u, path = heapq.heappop(pq)
            self.nodes_explored += 1

            if estimated_cost > self.best_cost:
                self.nodes_pruned += 1
                continue

            if len(path) == self.n:
                total_cost = current_cost + self.matrix[u][start_node]
                full_path = path + [start_node]
                
                if total_cost < self.best_cost:
                    self.best_cost = total_cost
                    self.optimal_paths = [full_path]
                elif total_cost == self.best_cost:
                    if full_path not in self.optimal_paths:
                        self.optimal_paths.append(full_path)
                continue

            for v in range(self.n):
                if v not in path:
                    new_cost = current_cost + self.matrix[u][v]
                    new_path = path + [v]
                    # Simple heuristic bound
                    estimated_total = new_cost + (self.get_lower_bound(new_path) // 2)

                    if estimated_total <= self.best_cost:
                        heapq.heappush(pq, (estimated_total, new_cost, v, new_path))
                    else:
                        self.nodes_pruned += 1

    def display_report(self):
        print("\n" + "="*45)
        print("          DETAILED ALGORITHM REPORT          ")
        print("="*45)
        print(f"Nodes Explored: {self.nodes_explored}")
        print(f"Nodes Pruned:   {self.nodes_pruned}")
        print(f"Minimum Cost:   {self.best_cost}")
        print("-" * 45)
        print(f"Found {len(self.optimal_paths)} Optimal Path(s):")
        for i, path in enumerate(self.optimal_paths, 1):
            print(f"  {i}. {' -> '.join(map(str, path))}")
        print("="*45)

def get_dynamic_sample(n=4):
    """Generates a random sample matrix to show the user."""
    sample = [[0 if i == j else random.randint(5, 50) for j in range(n)] for i in range(n)]
    return sample

def main():
    while True:
        print("\n--- TRAVELING SALESMAN PROBLEM (BRANCH & BOUND) ---")
        print("1. Solve TSP with Custom Matrix")
        print("2. View Dynamic Sample Input Format")
        print("3. Exit")
        
        choice = input("\nEnter your choice: ")

        if choice == '1':
            try:
                n = int(input("Enter number of cities: "))
                print(f"Enter the adjacency matrix row by row (space-separated values):")
                matrix = []
                for i in range(n):
                    row = list(map(int, input(f"Row {i}: ").split()))
                    if len(row) != n:
                        raise ValueError("Row length must match number of cities.")
                    matrix.append(row)
                
                solver = TSPSolver(matrix)
                solver.solve()
                solver.display_report()
            except Exception as e:
                print(f"\n[ERROR] Invalid input: {e}")

        elif choice == '2':
            size = random.randint(3, 4)
            sample = get_dynamic_sample(size)
            print(f"\n--- DYNAMIC SAMPLE INPUT ({size} Cities) ---")
            print("To get the highest marks, provide your input like this:")
            for row in sample:
                print(" ".join(map(str, row)))
            print("\nNote: Use '0' for the distance from a city to itself.")

        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()