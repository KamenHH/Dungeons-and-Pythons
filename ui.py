def get_menu():
    return """\n
status - shows hero data (hp, mana, weapons & spells)
map - show dungeon map
attack - targets a nearby creature and enters in battle
right - move hero once cell to the right
left = move hero one cell to the left
down - move hero one cell down
up - move hero one cell up\n"""


def intro(hero_known_as):
    return f"{hero_known_as} begins his adventure!"


def get_hero_status(hero):
    return f"{hero.known_as()}" \
           f"health - {hero.get_health()}, {hero.get_mana()}" \



def parse_user_input():
    valid_input_commands = ['status', 'attack', 'map', 'right', 'left', 'down', 'up', '']
    while True:
        user_input = input('>')
        if user_input not in valid_input_commands:
            print("Unknown command entered!")
        else:
            return user_input


