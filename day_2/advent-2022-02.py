INPUT = 'input.txt'
WEAPONS = {
    'opponent':{
        'A':{
            'weapon_name': 'rock',
            'beats': 'Z',
            'choice_points': 1
        },
        'B':{
            'weapon_name': 'paper',
            'beats': 'X',
            'choice_points': 2
        },
        'C':{
            'weapon_name': 'scissors',
            'beats': 'Y',
            'choice_points': 3
        },
    },
    'self':{
        'X':{
            'weapon_name': 'rock',
            'beats': 'C',
            'choice_points': 1
        },
        'Y':{
            'weapon_name': 'paper',
            'beats': 'A',
            'choice_points': 2
        },
        'Z':{
            'weapon_name': 'scissors',
            'beats': 'B',
            'choice_points': 3
        },
    },
}

POINTS = {
    'outcome': {
        'win': 6,
        'loss': 0,
        'draw': 3,
    },
}

def eval_battle(opponent_choice, my_choice):
    op_weapon = WEAPONS['opponent'][opponent_choice]
    my_weapon = WEAPONS['self'][my_choice]
    my_points = my_weapon['choice_points']
    if op_weapon['weapon_name'] == my_weapon['weapon_name']:
        my_points += 3
    elif op_weapon['beats'] == my_choice:
        my_points += 0
    elif my_weapon['beats'] == opponent_choice:
        my_points += 6
    return my_points

if __name__ == '__main__':
    with open(INPUT, 'r') as f:
        game_points = 0
        for line in f.readlines():
            game = tuple(line.replace('\n','').split(' '))
            game_points += eval_battle(*game)
    print(game_points)
