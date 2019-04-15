from collectables import Weapon, TreasureChest
from sprites import Hero
from map import Map
import ui


def main():
    m = Map()
    m.spawn(Hero('Billy', 'Wizard', health=250, mana=100, mana_regeneration_rate=2))
    w = Weapon(name='Keyboard', damage=15, scope=1)
    m.hero.equip(w)
    m.spawn_enemies()
    TreasureChest.parse_json()
    print(ui.intro(m.hero.known_as()))
    print(ui.get_menu())

    while True:
        user_input = ui.parse_user_input()
        if user_input == 'status':
            print(m.hero.get_status())
        elif user_input == 'attack':
            m.hero_attack()
            m.clear_enemy()
        elif user_input == 'map':
            print(m)
        elif user_input in ['right', 'left', 'down', 'up']:
            m.move_hero(user_input)
        elif user_input == '':
            print(ui.get_menu())


if __name__ == '__main__':
    main()