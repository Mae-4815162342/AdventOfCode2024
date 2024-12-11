def parse_input(input_map):
    grid = [list(line) for line in input_map.strip().split("\n")]
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell in "^>v<":
                start_pos = (r, c)
                facing = "^>v<".index(cell)
                grid[r][c] = "."
    return grid, start_pos, facing

def move(position, direction):
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
    return position[0] + moves[direction][0], position[1] + moves[direction][1]

def simulate(grid, start_pos, start_dir):
    visited_states = set()  # Tracks (position, direction) pairs
    path = set()  # Tracks all positions visited
    pos, direction = start_pos, start_dir

    while 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]):
        state = (pos, direction)
        if state in visited_states:
            return False, path  # Detected a loop
        visited_states.add(state)
        path.add(pos)

        next_pos = move(pos, direction)
        if (0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0]) 
            and grid[next_pos[0]][next_pos[1]] == "#"):
            direction = (direction + 1) % 4  # Turn right
        else:
            pos = next_pos

    return True, path  # Guard left the map

def find_valid_obstructions(grid, start_pos, start_dir):
    valid_positions = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "." and (r, c) != start_pos:
                grid[r][c] = "#"  # Place a temporary obstruction
                loops, path = simulate(grid, start_pos, start_dir)
                if not loops:
                    valid_positions.add((r, c))  # Add the obstruction position
                grid[r][c] = "."  # Remove the obstruction
    return valid_positions

# Example usage
input_map = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

grid, start_pos, start_dir = parse_input(input_map)
valid_positions = find_valid_obstructions(grid, start_pos, start_dir)
print(f"Number of valid obstruction positions: {len(valid_positions)}")
