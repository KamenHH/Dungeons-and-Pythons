class Attack:
    def __init__(self, name, damage, mana_cost):
        self._name = name
        self._damage = damage
        self._mana_cost = mana_cost

    def __str__(self):
        return f'{self._name}'

    def get_damage(self):
        return self._damage

    def use(self):
        return self._damage, self._mana_cost


class Weapon(Attack):
    def __init__(self, name, damage, mana_cost=0):
        super().__init__(name, damage, mana_cost)


class Spell(Attack):
    def __init__(self, name, damage, mana_cost):
        super().__init__(name, damage, mana_cost)


class Potion:
    def __init__(self, name, health=0, mana=0):
        self._name = name
        self._health_amount = health
        self._mana_amount = mana

    def get_type(self):
        return self._name

    def use(self):
        return self._health_amount, self._mana_amount


class Treasure:
    pass

