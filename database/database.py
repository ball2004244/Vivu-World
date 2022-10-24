import json
import sys 
sys.path.append('../Vivu-World')

score = 0
highest_score = 0
current_round = 0
mouse_speed = 10
resolution = (1080, 720)

ingame_data = {
    'highest-score': highest_score,
    'slot1': {
        'score': score,
        'current-round': current_round,
        'status': 'SAVED',
    },
    'slot2': {
        'score': None,
        'current-round': None,
        'status': 'EMPTY',
    },
    'slot3': {
        'score': None,
        'current-round': None,
        'status': 'EMPTY',
    },
}

setting_data = {
    'mouse-speed': mouse_speed,
    'resolution': resolution,
    'volume': None
}

# JSON processing
def export_data(data: dict, database: str) -> None:
    # Export ingame data to JSON files
    with open(r'database/' + database, 'w') as storage:
        json.dump(data, storage, indent=4)

def import_data(database: str) -> dict:
    # Import ingame data from JSON files
    with open(r'database/' + database, 'r') as storage:
        ingame_data = json.load(storage)
        # print(ingame_data)
    return ingame_data

def process_data():
    # Process data
    # score = ingame_data['score']
    # highest_score = ingame_data['highest-score']
    # current_round = ingame_data['current-round']
    # Calculation when game gets harder
    game_speed = current_round // 100 + 1

    # for zombie_slap
    zombie_health = current_round // 20 + 1

    # flappy bird
    flappy_speed = game_speed

    # mole in hole
    mole_speed = game_speed

    # horse shooting
    horse_speed = game_speed
    bullet_speed = game_speed // 1000
    pass


if __name__ == '__main__':
    # export_data()
    # ingame_data = import_data('database.json')
    # print(ingame_data)
    print(type(ingame_data))
    export_data(ingame_data, 'database.json')
    pass
