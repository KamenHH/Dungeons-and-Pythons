import json
import random

class Treasure:
    # treasures = parse_json()
    def __init__(self):
        # self.treasure = __class__.pick_item()
        pass

    @classmethod
    def parse_json(cls):  
        with open('treasures.json') as jf:
            cls.treasures = json.load(jf)
    
    @classmethod
    def _pick_item(cls):
        return random.choice(cls.treasures)

    @staticmethod
    def parse_object():
        obj = __class__._pick_item()         
        for attr in obj.items():
            print(attr)


class MeansOfAttack:
    def __init__(self, name, damage, scope):
        self._name = name
        self._damage = damage
        self._range = scope

    def __str__(self):
        return f'{self._name}'

    def get_damage(self):
        return self._damage

    def use(self):
        return self._damage, self._mana_cost


class Weapon(MeansOfAttack):
    def __init__(self, name, damage, scope):
        super().__init__(name, damage, scope)


class Spell(MeansOfAttack):
    def __init__(self, name, damage, scope, mana_cost):
        super().__init__(name, damage, scope)
        self._mana_cost = mana_cost



class Potion:
    def __init__(self, name, health=0, mana=0):
        self._name = name
        self._health_amount = health
        self._mana_amount = mana

    def get_type(self):
        return self._name

    def use(self):
        return self._health_amount, self._mana_amount

if __name__ == "__main__":
    Treasure.parse_json()
    t = Treasure()
    # print(Treasure.treasures)
    # print(t.treasure)
    print(t.parse_object())