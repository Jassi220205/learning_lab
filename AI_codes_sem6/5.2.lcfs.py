import heapq

def lowest_cost_first_search(graph, start, goal):
    priority_queue = [(0, start, [start])]  # (cost, node, path)
    visited = set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node == goal:
            return cost, path

        if node not in visited:
            visited.add(node)

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(
                        priority_queue,
                        (cost + weight, neighbor, path + [neighbor])
                    )

    return float("inf"), None


# Example usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

cost, path = lowest_cost_first_search(graph, 'A', 'F')
print("Cost:", cost)
print("Path:", path)