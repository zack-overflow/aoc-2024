from functools import cmp_to_key

def read_input(filepath, sample=True):
    with open(filepath, 'r') as file:
        if sample:
            first_line = file.readline().strip()
            # read the lines until the empty line
            rule_book = {}
            while line := file.readline().strip():
                line_split = line.split('|')
                rule_book.setdefault(line_split[1], set()).add(line_split[0])

            updates = []
            while line := file.readline().strip():
                updates.append(line.split(','))
            return first_line, rule_book, updates
        else:
            rule_book = {}
            while line := file.readline().strip():
                line_split = line.split('|')
                rule_book.setdefault(line_split[1], set()).add(line_split[0])

            updates = []
            while line := file.readline().strip():
                updates.append(line.split(','))
            return rule_book, updates

def check_update_validity(update, rule_book):
    valid = True

    for i in range(len(update)):
        for j in range(i, len(update)):
            earlier = update[i]
            later = update[j]
            if earlier in rule_book:
                if later in rule_book[earlier]:
                    valid = False

    return valid

def compare_pages_outer(rule_book):
    def compare_pages(p1, p2):
        if p2 in rule_book:
            if p1 in rule_book[p2]:
                return 1

        if p1 in rule_book:
            if p2 in rule_book[p1]:
                return -1

    return compare_pages

def fix_update(update, rule_book):

    update.sort(key=cmp_to_key(compare_pages_outer(rule_book)))
    return int(update[len(update) // 2])

def count_updates(rule_book, updates, part):
    if part == 1:
        total = 0
        for update in updates:
            valid = check_update_validity(update, rule_book)

            if valid:
                update_len = len(update)
                total += int(update[update_len // 2])

    else:
        total = 0
        for update in updates:
            valid = check_update_validity(update, rule_book)

            if not valid:
                total += fix_update(update, rule_book)

    return total

def main(filename, part):
    if filename == 'sample':
        first_line, rule_book, updates = read_input(filename)
        res = count_updates(rule_book, updates, 2)

        if part == 1:
            expected = int(first_line.split(',')[0])
        else:
            expected = int(first_line.split(',')[1])

        if res != expected:
            print(f'Error: expected: {expected} \n output: {res}')
        else:
            print('Test Passed')
    else:
        rule_book, updates = read_input(filename, sample=False)
        res = count_updates(rule_book, updates, 2)
        print(res)


main('input', 2)
