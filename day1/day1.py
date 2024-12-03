import numpy as np
# import sys
# sys.path.append('../')
# from read_input import read_input

def read_input(filepath, sample=False):
    with open(filepath, 'r') as file:
        if sample:
            first_line = file.readline().strip()
            return first_line, np.loadtxt(filepath, skiprows=1)
        else:
            return None, np.loadtxt(filepath, skiprows=0)

   
def compare_lists(lists, part=1):
    if part == 1:
        # sort the lists
        sorted_lists = np.sort(lists, axis=0)

        # get the differences between the lists
        diff = sorted_lists[:,1]- sorted_lists[:,0]
        
        return np.abs(diff).sum()
    else:
        from collections import Counter
        # count up items in right list
        counts = Counter(lists[:,1])

        # go through the left list and add up the scores
        sum = 0
        for i in range(lists.shape[0]):
            if lists[i,0] in counts:
                sum += lists[i, 0] * counts[lists[i,0]]

        return sum



def main(filepath='sample', part=1):
    if filepath == 'sample':
        first_line, lists = read_input('sample', sample=True)
        res = compare_lists(lists, part)
        first_line = first_line.split(',')[part-1]
        if res != int(first_line):
            print(f'Error: {res} != {first_line}')
        else:
            print('Test passed')

    else:
        first_line, lists = read_input(filepath)
        res = compare_lists(lists, part)
        print(int(res))

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 2:
        main(sys.argv[1], int(sys.argv[2]))
    else:
        main(part=int(sys.argv[1]))