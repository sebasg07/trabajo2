import random

def generate_maze(rows, cols):
    maze = [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

    
    maze[0][0] = maze[rows - 1][cols - 1] = 1

    return maze

def print_maze(maze):
    for row in maze:
        print(" ".join("X" if cell == 0 else " " for cell in row))

def navigate_maze(maze, start, end):
    current_position = start

    while current_position != end:
        x, y = current_position

        
        available_moves = [(dx, dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]
                           if 0 <= x + dx < len(maze[0]) and 0 <= y + dy < len(maze) and maze[y + dy][x + dx] == 1]

        if available_moves:
            
            next_move = random.choice(available_moves)
            dx, dy = next_move
            maze[y][x] = 2  
            current_position = (x + dx, y + dy)
        else:
            
            maze[y][x] = 0  
            current_position = start

    return maze

def main():
    rows, cols = 5, 5
    start = (0, 0)
    end = (rows - 1, cols - 1)

    maze = generate_maze(rows, cols)
    print("Laberinto generado:")
    print_maze(maze)

    maze = navigate_maze(maze, start, end)

    print("\nLaberinto después de la navegación:")
    print_maze(maze)

    if maze[end[1]][end[0]] == 2:
        print("\n¡Has llegado a la salida!")
    else:
        print("\nNo se puede llegar a la salida.")

if __name__ == "__main__":
    main()
