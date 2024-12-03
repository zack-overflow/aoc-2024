import numpy as np

def read_input(filepath, sample=False):
    with open(filepath, 'r') as file:
        if sample:
            first_line = file.readline().strip()
            return first_line, line_generator(filepath)
        else:
            return None, line_generator(filepath)
