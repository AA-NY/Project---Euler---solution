def lattice_paths(grid_size):
    # Create a 2D grid with grid_size + 1 rows and columns
    grid = [[0] * (grid_size + 1) for _ in range(grid_size + 1)]

    # Initialize the base cases (rightmost column and bottommost row)
    for i in range(grid_size + 1):
        grid[i][grid_size] = 1
        grid[grid_size][i] = 1

    # Work backwards, filling in the number of paths for each grid point
    for i in range(grid_size - 1, -1, -1):
        for j in range(grid_size - 1, -1, -1):
            grid[i][j] = grid[i + 1][j] + grid[i][j + 1]

    return grid[0][0]

# Example usage for a 20x20 grid
grid_size = 20
result = lattice_paths(grid_size)
print(f"The number of routes through a {grid_size}x{grid_size} grid is: {result}")

#The number of routes through a 20x20 grid is: 137846528820