import string

INPUT = 'input.txt'
LOWEST_PRIORITY = 1
HIGHEST_PRIORITY = 52
ITEM_PRIORITIES = dict(zip(string.ascii_lowercase + string.ascii_uppercase,
                           range(LOWEST_PRIORITY, HIGHEST_PRIORITY + 1)))


def get_compartments(rucksack):
    rucksack = rucksack.replace('\n', '')
    halfway = int(len(rucksack) / 2)
    c1 = rucksack[:halfway]
    c2 = rucksack[halfway:]
    return (c1, c2)

def find_duplicate_item(rucksack):
    return [item for item in rucksack[0] if item in rucksack[1]][0]

def main():
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
