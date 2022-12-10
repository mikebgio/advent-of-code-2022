INPUT = 'input.txt'
BLANK = '\n'

def setup_hauls():
    elf_hauls = []
    with open(INPUT, 'r') as f:
        batch = []
        for line in f.readlines():
            if line == BLANK:
                elf_hauls.append(batch)
                batch=[]
            else:
                batch.append(int(line))
    elf_hauls = sum_up_hauls(elf_hauls)
    return elf_hauls

def sum_up_hauls(hauls):
    summed_hauls = []
    for h in hauls:
        summed_hauls.append(sum(h))
    return summed_hauls

def find_hefty_haul(hauls):
    hauls.sort()
    return hauls[-1]

def find_top_three_haulers(hauls):
    hauls.sort()
    return sum(hauls[-3:])

if __name__ == '__main__':
    elf_hauls = setup_hauls()
    biggest_elf_haul = find_hefty_haul(elf_hauls)
    print(f'Most calories by a single elf: {biggest_elf_haul}')
    top_three = find_top_three_haulers(elf_hauls)
    print(f'Total calories by top three elves: {top_three}')

