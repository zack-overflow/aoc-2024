def read_input(filepath):
    with open(filepath, 'r') as file:
        instructions = file.readlines()
    return instructions

def check_potential_mult(potential_mult):
    # get until the closing paren
    close_paren_idx = -1
    for j in range(len(potential_mult)):
        if potential_mult[j] == ')':
            close_paren_idx = j
            break
    if close_paren_idx < 0:
        return False
    
    refined = potential_mult[:close_paren_idx]

    refined_split = refined.split(',')
    if len(refined_split) != 2:
        return False
    
    # get out the numbers to multiply
    operands = []
    for spl in refined_split:
        if len(spl) > 3:
            return False
        
        for chr in spl:
            if not chr.isdigit():
                return False
        operands.append(int(spl))

    mult = 1
    for op in operands:
        mult *= op
    return mult
    

def check_potential_conditional(potential_conditional):
    if potential_conditional[:2] == '()':
        return 1
    elif potential_conditional == "n't()":
        return 0
    
    return -1
    
enabled = True # global var so it persists between lines
def parse_instruction(instruction, part):
    global enabled
    # idea: if you see an m, keep going until it breaks; if not, add to total
    total = 0
    for i in range(len(instruction)-5):
        # check for conditional instructions
        if part == 2:
            if instruction[i:i+2] == 'do':
                res = check_potential_conditional(instruction[i+2:i+7])
                enabled = res if res >= 0 else enabled # only change if the instruction was valid

        # check for multiplication instructions
        if instruction[i:i+4] == 'mul(':
            res = check_potential_mult(instruction[i+4:i+12])
            total += (res if enabled else 0)

    return total

def main(filepath, part):
    data = read_input(filepath)
    grand_total = 0
    for instruction in data:
        grand_total += parse_instruction(instruction, part)
    print(f'\nGRAND TOTAL: {grand_total}')

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 2:
        main(sys.argv[1], int(sys.argv[2]))
    else:
        main(part=int(sys.argv[1]))