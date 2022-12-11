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


def get_part_one_answer(rucksacks):
    """
    iterates over list of rucksacks and returns the answer for part one
    :param rucksacks: list[str]
    :return: int
    """
    total_score = 0
    for rucksack in rucksacks:
        sorted_rucksack = get_compartments(rucksack)
        duplicate_item = find_duplicate_item(sorted_rucksack)
        priority_score = ITEM_PRIORITIES[duplicate_item]
        total_score += priority_score
    return total_score


def get_badge_letter_from_rucksack_group(rucksack_group):
    """
    Finds the letter that is repeated in a list of three strings
    :param rucksack_group: list[str]
    :return: str
    """
    for letter in rucksack_group[0]:
        if all(letter in rucksack for rucksack in rucksack_group):
            return letter
    return None


def process_rucksack_groups(rucksacks):
    """
    Finds which letter appears in each of the rucksack strings in a rucksack
    group, returning that letter
    :param rucksack_group: list[str]
    :return: str
    """
    rucksack_group = []
    full_list = []
    for idx, rucksack in enumerate(rucksacks):
        rucksack_group.append(rucksack)
        if (idx + 1) % 3 == 0:
            full_list.append(rucksack_group)
            rucksack_group = []
    return full_list


def get_part_two_answer(rucksacks):
    """
    Processes the input file for part two challenge of day 3
    :param rucksacks: list[str]
    :return: int
    """
    rucksack_groups = process_rucksack_groups(rucksacks)
    priority_points = 0
    for rucksack_group in rucksack_groups:
        badge = get_badge_letter_from_rucksack_group(rucksack_group)
        priority_points += ITEM_PRIORITIES[badge]
    return priority_points


def main():
    """
    runs through input.txt and prints answers
    """
    with open(INPUT, 'r', encoding="utf-8") as rucksacks_file:
        rucksacks = rucksacks_file.readlines()
    part_one_answer = get_part_one_answer(rucksacks)
    part_two_answer = get_part_two_answer(rucksacks)
    print(f'Total priority score is: {part_one_answer}')
    print(f'Total sum of badge priorities: {part_two_answer}')


if __name__ == '__main__':
    main()
