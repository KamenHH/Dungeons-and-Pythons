import json
import random
import sys


class TreasureChest:
    """Used to load and parse the collectables.json,
    pick a random item and create an object instance from the parsed data."""

    # treasures = parse_json()
    def __init__(self):
        self.treasure = __class__.parse_object()

    def __str__(self):
        return

    @classmethod
    def parse_object(cls):
        class_info = cls._pick_item()
        class_name = class_info.pop('type')
        return getattr(sys.modules[__name__], class_name)(**class_info)

    @classmethod
    def parse_json(cls):
        """Gets the json data."""
        with open('treasures.json') as jf:
            cls.treasures = json.load(jf)

    @classmethod
    def _pick_item(cls):
        return random.choice(cls.treasures)


class MeansOfAttack:
    """Base class for Weapon and Spell.
    name: name of the type of attack: Axe, Fireball, Bow, Blizzad, etc.
    damage: the damage that the type of attack deals on a single use,
    mele attack: scope = 1, ranged attack: scope > 1
    """

    def __init__(self, name, damage, scope):
        self._name = name
        self._damage = damage
        self._scope = scope

    def __str__(self):
        return f'{self._name}'

    @property
    def damage(self):
        return self._damage

    def use(self):
        return self._damage, self._scope


class Weapon(MeansOfAttack):
    """Weapon class, can be ranged or mele."""

    def __init__(self, name, damage, scope):
        super().__init__(name, damage, scope)


class Spell(MeansOfAttack):
    """Spell class, mostly ranged, but can be mele
    mana cost: the amount of points that will be taken from the
    hero's mana for a single use of the spell."""

    def __init__(self, name, damage, scope, mana_cost):
        super().__init__(name, damage, scope)
        self._mana_cost = mana_cost

    @property
    def mana_cost(self):
        return self._mana_cost

    def use(self):
        return self._damage, self._scope, self._mana_cost


class Potion:
    """Restores some amount of health, mana, or both, to the hero in play."""

    def __init__(self, name, health_amount, mana_amount):
        self._name = name
        self._health_amount = health_amount
        self._mana_amount = mana_amount

    def __str__(self):
        return self._name

    def use(self):
        return self._health_amount, self._mana_amount

# if __name__ == "__main__":
#     TreasureChest.parse_json()
#     tc = TreasureChest()
#     # t.parse_object()
#     # print(Treasure.treasures)
#     # print(t.treasure)
#     print(tc.treasure.__dict__)