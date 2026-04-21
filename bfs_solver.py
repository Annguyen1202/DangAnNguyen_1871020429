from collections import deque
from src.core_logic import get_start_goal, get_neighbors, print_maze_with_path # pyright: ignore[reportMissingImports]

def bfs(maze):
    start, goal = get_start_goal(maze)
    queue = deque([(start, [start])])
    visited = set([start])
    
    while queue:
        current, path = queue.popleft()

        # Nếu tới đích
        if current == goal:
            print("BFS - Found path!")
            print("Visited Nodes:", len(visited))
            print_maze_with_path(maze, path, len(visited))
            return path

        # Duyệt hàng xóm
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    print("BFS - No path found")
    return None