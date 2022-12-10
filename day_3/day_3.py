"""
Day Three
"""
import string

INPUT = 'input.txt'
LOWEST_PRIORITY = 1
HIGHEST_PRIORITY = 52
ITEM_PRIORITIES = dict(zip(string.ascii_lowercase + string.ascii_uppercase,
                           range(LOWEST_PRIORITY, HIGHEST_PRIORITY + 1)))


def get_compartments(rucksack):
    """
    Sorts the letters in rucksack evenly into compartments
    :param rucksack: string of random letters from input file
    :return: tuple of lists, each taking half of the letters in rucksack
    """
    rucksack = rucksack.replace('\n', '')
    halfway = int(len(rucksack) / 2)
    left_compartment = rucksack[:halfway]
    right_compartment = rucksack[halfway:]
    return (left_compartment, right_compartment)


def find_duplicate_item(rucksack):
    """
    Returns the single item in each rucksack that is erroneously in both
    compartments
    :param rucksack: tuple of lists
    :return: string of the letter that is in both lists in tuple rucksack
    """
    return [item for item in rucksack[0] if item in rucksack[1]][0]


def main():
    """
    runs through input.txt and prints answers
    """
    total_score = 0
    with open(INPUT, 'r', encoding="utf-8") as rucksacks:
        for rucksack in rucksacks.readlines():
            sorted_rucksack = get_compartments(rucksack)
            duplicate_item = find_duplicate_item(sorted_rucksack)
            priority_score = ITEM_PRIORITIES[duplicate_item]
            total_score += priority_score
    print(f'Total priority score is: {total_score}')


if __name__ == '__main__':
    main()
