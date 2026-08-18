import heapq

# Graph representation using adjacency list
graph = {
    'A': [('B', 4), ('C', 3)],
    'B': [('A', 4), ('C', 2), ('D', 5)],
    'C': [('A', 3), ('B', 2), ('D', 6)],
    'D': [('B', 5), ('C', 6)]
}

def prim(graph, start):
    visited = set()
    min_heap = [(0, start)]
    total_cost = 0
    mst_edges = []

    while min_heap:
        cost, node = heapq.heappop(min_heap)

        if node not in visited:
            visited.add(node)
            total_cost += cost

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, neighbor))
                    mst_edges.append((node, neighbor, weight))

    return total_cost

minimum_cost = prim(graph, 'A')
print("Minimum Total Connection Cost:", minimum_cost)