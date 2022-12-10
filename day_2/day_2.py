INPUT = 'input.txt'

PLAYS = {
    'A': {
        'weapon_name': 'rock',
        'beats': 'Z',
    },
    'B': {
        'weapon_name': 'paper',
        'beats': 'X',
    },
    'C': {
        'weapon_name': 'scissors',
        'beats': 'Y',
    },
    'X': {
        'weapon_name': 'rock',
        'beats': 'C',
        'true_meaning': 'loss'
    },
    'Y': {
        'weapon_name': 'paper',
        'beats': 'A',
        'true_meaning': 'draw'
    },
    'Z': {
        'weapon_name': 'scissors',
        'beats': 'B',
        'true_meaning': 'win'
    },
}

POINTS = {
    'battle': {
        'win': 6,
        'loss': 0,
        'draw': 3,
    },
    'weapon_choice': {
        'rock': 1,
        'paper': 2,
        'scissors': 3
    }

}


def rps_eval(opponent_weapon, my_weapon):
    """
    evaluates any rock paper scissors (RPS) battle and returns the second
    player's score
    :param opponent_weapon: str - name of RPS weapon for the first player
    :param my_weapon: str - name of RPS weapon for the second player
    :return: points: int
    """
    points = POINTS['weapon_choice'][my_weapon]
    if opponent_weapon == my_weapon:
        points += POINTS['battle']['draw']
    elif opponent_weapon == 'rock':
        if my_weapon == 'paper':
            points += POINTS['battle']['win']
        elif my_weapon == 'scissors':
            points += POINTS['battle']['loss']
    elif opponent_weapon == 'paper':
        if my_weapon == 'rock':
            points += POINTS['battle']['loss']
        elif my_weapon == 'scissors':
            points += POINTS['battle']['win']
    elif opponent_weapon == 'scissors':
        if my_weapon == 'rock':
            points += POINTS['battle']['win']
        elif my_weapon == 'paper':
            points += POINTS['battle']['loss']
    return points

def select_startegic_weapon(strategy, op_weapon):
    if strategy == 'draw':
        return op_weapon
    if op_weapon == 'rock':
        if strategy == 'win':
            return 'paper'
        else:
            return 'scissors'
    elif op_weapon == 'paper':
        if strategy == 'win':
            return 'scissors'
        else:
            return 'rock'
    elif op_weapon == 'scissors':
        if strategy == 'win':
            return 'rock'
        else:
            return 'paper'

def eval_battle_pt_1(opponent_choice, my_choice):
    op_weapon = PLAYS[opponent_choice]['weapon_name']
    my_weapon = PLAYS[my_choice]['weapon_name']
    return rps_eval(op_weapon, my_weapon)


def eval_battle_pt_2(opponent_choice, my_choice):
    op_weapon = PLAYS[opponent_choice]['weapon_name']
    my_strategy = PLAYS[my_choice]['true_meaning']
    my_weapon = select_startegic_weapon(my_strategy, op_weapon)
    return rps_eval(op_weapon, my_weapon)


if __name__ == '__main__':
    with open(INPUT, 'r') as f:
        part_1_points = 0
        part_2_points = 0
        for line in f.readlines():
            game = tuple(line.replace('\n', '').split(' '))
            part_1_points += eval_battle_pt_1(*game)
            part_2_points += eval_battle_pt_2(*game)
    print(f'The answer for Part One is: {part_1_points}')
    print(f'The answer for Part Two is: {part_2_points}')
