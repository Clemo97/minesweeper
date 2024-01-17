def count_adjacent_bombs(grid):
    rows, cols = len(grid), len(grid[0])
    adjacent_bombs_count = [[0 for _ in range(cols)] for _ in range(rows)]

    # Define the eight possible directions for adjacent cells
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1), (1, 0),  (1, 1)
    ]

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '*':
                # If the cell contains a bomb, update adjacent cells
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc

                    # Check if the new coordinates are within the grid boundaries
                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        adjacent_bombs_count[new_row][new_col] += 1

    return adjacent_bombs_count

# Example usage:
grid = [
    ['.', '.', '*', '.'],
    ['*', '.', '.', '*'],
    ['.', '*', '.', '.'],
    ['*', '.', '.', '*']
]

adjacent_bombs = count_adjacent_bombs(grid)

# Print the resulting 2D array
for row in adjacent_bombs:
    print(row)
