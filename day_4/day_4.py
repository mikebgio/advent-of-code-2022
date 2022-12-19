"""
Day Four
"""
INPUT = 'input.txt'
# INPUT = 'sample.txt'


def get_elf_section_range(elf_assignment):
    """
    Accepts a single line of input.txt and returns a list of lists of ints
    :param elf_assignment: str
    :return: list[list[int]]
    """
    section_range = elf_assignment.split('-')
    section_range = [int(i) for i in section_range]
    if section_range[0] == section_range[1]:
        return [section_range[0]]
    return list(range(section_range[0], section_range[1] + 1))


def parse_pairs(line):
    """
    parses pairs
    """
    pair = []
    for elf in line.split(','):
        pair.append(get_elf_section_range(elf))
    return pair


def pairs_fully_overlapped(pair: list):
    """
    Figures out which set in the pair is the subset
    :param pair: list
    :return: bool
    """
    if pair[0] == pair[1]:
        return True
    if len(pair[0]) <= len(pair[1]):
        result = compare_pair_assignments(pair[0], pair[1])
    else:
        result = compare_pair_assignments(pair[1], pair[0])
    return result


def compare_pair_assignments(smaller_set, larger_set, ):
    if (all(x in larger_set for x in smaller_set)):
        return True
    else:
        return False


def main():
    part_one_answer = 0
    with open(INPUT, 'r') as input:
        assignments = input.readlines()
    for assignment in assignments:
        pair = parse_pairs(assignment)
        if pairs_fully_overlapped(pair):
            print(assignment)
            part_one_answer += 1
    print(part_one_answer)


if __name__ == '__main__':
    main()
