'''
The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
'''

def read_input(filepath, sample=False):
    with open(filepath, 'r') as file:
        if sample:
            first_line = file.readline().strip()
        else:
            first_line = None
        
        lines = []
        for line in file:
            line_arr = list(map(int, line.split()))
            lines.append(line_arr)
        
        return first_line, lines


def check_safe(row_raw: list, part:int) -> bool:
    '''
    Safe row should either be all increase or all decrease (by at most 3)
    '''
    if part == 1:
        row = row_raw
        for i in range(1, len(row)):
                curr = row[i]
                prev = row[i-1]

                new_change = curr > prev # True is increase, False is decrease

                no_change = curr == prev
                breaks_pattern = i > 1 and new_change != inc
                change_too_big = abs(curr-prev) > 3
                
                if no_change or breaks_pattern or change_too_big:
                    return False
                
                inc = new_change # for first iteration to set pattern of inc or dec
            
        return True
    else:
        for j in range(len(row_raw)):
            row = row_raw[:j] + row_raw[j+1:]
            fail = False
            
            for i in range(1, len(row)):
                curr = row[i]
                prev = row[i-1]

                new_change = curr > prev # True is increase, False is decrease

                no_change = curr == prev
                breaks_pattern = i > 1 and new_change != inc
                change_too_big = abs(curr-prev) > 3
                
                if no_change or breaks_pattern or change_too_big:
                    fail = True
                    break
                
                inc = new_change # for first iteration to set pattern of inc or dec
            
            if not fail:
                return True
            
        return False


def main(filepath:str='sample', part:int=1):
    sample = filepath == 'sample'
    first_line, data = read_input(filepath, sample)
    num_safe = sum(check_safe(row, part) for row in data)
    
    if sample:
        first_line = first_line.split(',')[part-1]
        if num_safe != int(first_line):
            print(f'Error: algo result {num_safe} != ground truth {first_line}')
        else:
            print('Test passed')

    print(num_safe)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 2:
        main(sys.argv[1], int(sys.argv[2]))
    else:
        main(part=int(sys.argv[1]))
