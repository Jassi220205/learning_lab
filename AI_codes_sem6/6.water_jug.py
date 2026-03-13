from collections import deque

def water_jug_bfs(cap1, cap2, target):
    visited = set()
    queue = deque()
    
    # Each element: (jug1, jug2, path)
    queue.append((0, 0, []))
    
    while queue:
        x, y, path = queue.popleft()
        
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        path = path + [(x, y)]
        
        # Goal check
        if x == target or y == target:
            return path
        
        # Possible operations
        next_states = [
            (cap1, y),              # Fill Jug1
            (x, cap2),              # Fill Jug2
            (0, y),                 # Empty Jug1
            (x, 0),                 # Empty Jug2
            (x - min(x, cap2 - y),  # Pour Jug1 -> Jug2
             y + min(x, cap2 - y)),
            (x + min(y, cap1 - x),  # Pour Jug2 -> Jug1
             y - min(y, cap1 - x))
        ]
        
        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))
    
    return None


# ----------- USER INPUT -------------
cap1 = int(input("Enter capacity of Jug1: "))
cap2 = int(input("Enter capacity of Jug2: "))
target = int(input("Enter target amount: "))

solution = water_jug_bfs(cap1, cap2, target)

if solution:
    print("\nSolution Steps:")
    for step in solution:
        print(step)
else:
    print("\nNo solution possible.")