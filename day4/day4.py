import sys
import numpy as np

def read_input(filepath, sample=False):
    with open(filepath, 'r') as file:
        if sample:
            first_line = file.readline().strip()
            return first_line, np.genfromtxt(filepath, skip_header=1, dtype=str, delimiter=1)
        else:
            return None, np.genfromtxt(filepath, skip_header=0, dtype=str, delimiter=1)


def check_inbounds(grid, i, j):
    return 0 <= i < grid.shape[0] and 0 <= j < grid.shape[1]

def check_A(grid, i, j):
    # see if the A is the center of an X-mas
    deltas = [-1, 1]
    for delta_i in deltas:
        for delta_j in deltas:
            this_good = True

            # check for an S in the spot defined by the deltas, WLOG
            if check_inbounds(grid, i+delta_i, j+delta_j) and grid[i+delta_i][j+delta_j] == 'S':
                M_diagonal = check_inbounds(grid, i-delta_i, j-delta_j) and grid[i-delta_i][j-delta_j] == 'M'
                S_vertical = check_inbounds(grid, i-delta_i, j+delta_j) and grid[i-delta_i][j+delta_j] == 'S'
                S_to_side = check_inbounds(grid, i+delta_i, j-delta_j) and grid[i+delta_i][j-delta_j] == 'S'
                M_vertical = check_inbounds(grid, i-delta_i, j+delta_j) and grid[i-delta_i][j+delta_j] == 'M'
                M_to_side = check_inbounds(grid, i+delta_i, j-delta_j) and grid[i+delta_i][j-delta_j] == 'M'

                this_good = M_diagonal and ((S_to_side and M_vertical) or (S_vertical and M_to_side))

                if this_good:
                    return True
                
    return False


def iterate_and_search(grid):
    total = 0
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i][j] == 'A':
                total += check_A(grid, i, j)
    
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
    if len(sys.argv) > 2:
        main(sys.argv[1], int(sys.argv[2]))
    else:
        main(part=int(sys.argv[1]))
