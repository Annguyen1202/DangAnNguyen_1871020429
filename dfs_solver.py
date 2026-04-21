from src.core_logic import get_start_goal, get_neighbors, print_maze_with_path # pyright: ignore[reportMissingImports]

def dfs(maze):
    start, goal = get_start_goal(maze)
    stack = [(start, [start])]
    visited = set([start])
    
    while stack:
        current, path = stack.pop()

        # Nếu tới đích
        if current == goal:
            print("DFS - Found path!")
            print("Visited Nodes:", len(visited))
            print_maze_with_path(maze, path, len(visited))
            return path

        # Duyệt hàng xóm
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [neighbor]))

    print("DFS - No path found")
    return None