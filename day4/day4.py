import sys
import numpy as np

def read_input(filepath, sample=False):
    with open(filepath, 'r') as file:
        if sample:
            first_line = file.readline().strip()
            return first_line, np.genfromtxt(filepath, skip_header=1, dtype=str, delimiter=1)
        else:
            return None, np.genfromtxt(filepath, skip_header=0, dtype=str, delimiter=1)

# Dictionary to define the next expected character in the word
next_dict = {
    'X': 'M',
    'M': 'A',
    'A': 'S'
}

def check_inbounds(grid, i, j):
    return 0 <= i < grid.shape[0] and 0 <= j < grid.shape[1]

def dfs(grid, i, j, next, delta_i, delta_j, visited):
    # Base case: if we reach the end of the word
    if next is None:
        return 1  # Found one instance of "XMAS"
    
    # Move to the next cell in the given direction
    new_i, new_j = i + delta_i, j + delta_j
    if (new_i, new_j) in visited:
        return 0  # Avoid revisiting cells in this path
    if not check_inbounds(grid, new_i, new_j) or grid[new_i][new_j] != next:
        return 0  # Stop if out of bounds or character mismatch
    
    # Add current cell to visited and continue searching
    visited.add((new_i, new_j))
    count = dfs(grid, new_i, new_j, next_dict.get(next), delta_i, delta_j, visited)
    visited.remove((new_i, new_j))  # Backtrack
    
    return count

def iterate_and_search(grid):
    total = 0
    
    # Look for all starting points ('X')
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i][j] == 'X':
                # Explore all 8 directions from the starting point
                for delta_i in [-1, 0, 1]:
                    for delta_j in [-1, 0, 1]:
                        if delta_i == 0 and delta_j == 0:
                            continue
                        visited = {(i, j)}  # Mark starting cell as visited
                        total += dfs(grid, i, j, 'M', delta_i, delta_j, visited)
    
    return total

def main(filename='sample', part=1):
    sample = filename == 'sample'
    first_line, data = read_input(filename, sample)
    
    num_instances = iterate_and_search(data)
    
    if sample:
        first_line = first_line.split(',')[part-1]
        if num_instances != int(first_line):
            print(f'Error: algo result {num_instances} != ground truth {first_line}')
        else:
            print('Test passed')

    print(f'GRAND TOTAL: {num_instances}')

if __name__ == '__main__':
    main()