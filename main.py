from collectables import Weapon, Spell
from sprites import Hero
import time


def main():
    h = Hero('Billy', 'Wizard', health=250, mana=100, mana_regeneration_rate=2)
    w = Weapon(name='Axe', damage=15)
    s = Spell(name='Firball', damage=25, mana_cost=20)
    h.equip(w)
    h.learn(s)
    while True:
        print(h.attack(by='spell'))
        print(h.get_mana())
        print('------')
        time.sleep(0.5)


if __name__ == '__main__':
    main()