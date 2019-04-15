class Sprite:
    def __init__(self, health, mana):
        self._curr_health = health
        self._max_health = health
        self._curr_mana = mana
        self._max_mana = mana

    @property
    def x_coord(self):
        return self._x

    @x_coord.setter
    def x_coord(self, coord):
        self._x = coord

    @property
    def y_coord(self):
        return self._y

    @y_coord.setter
    def y_coord(self, coord):
        self._y = coord

    @property
    def max_health(self):
        """Cannot be changed, used as reference for initial health points."""
        return self._max_health

    @property
    def max_mana(self):
        """Cannot be changed, used as reference for initial mana points."""
        return self._max_mana

    def get_health(self):
        return self._curr_health

    def get_mana(self):
        return self._curr_mana

    def get_status(self):
        return f'Health: {self._curr_health}/{self.max_health}; Mana: {self._curr_mana}/{self.max_mana}\n' \
               f'{self.has_weapon()} - damage: {self.weapon.damage if self.has_weapon() else 0}\n' \
               f'{self.has_spell()} - damage: {self.spell.damage if self.has_spell() else 0}'

    def is_alive(self):
        """Returns true if current health is greater than 0."""
        return self._curr_health > 0

    def can_cast(self):
        """Returns true if current mana is greater than 0 and enough to cast the spell."""
        spell = self.__dict__.get('spell', 0)
        return spell != 0 and self.get_mana() >= spell.mana_cost

    def lose_health(self, damage):
        """Decreases sprite's health based on the given damage factor."""
        remaining_health = self._curr_health - damage
        if remaining_health <= 0:
            self._curr_health = 0
        else:
            self._curr_health = remaining_health

    def take_healing(self, heal_amount):
        """Restores sprite's health, if new value doesn't exceed max_health"""
        new_health = self._curr_health + heal_amount
        if new_health >= self.max_health:
            self._curr_health = self.max_health
        else:
            self._curr_health = new_health

    def spend_mana(self, amount):
        remaining_mana = self._curr_mana - amount
        if remaining_mana <= 0:
            self._curr_mana = 0
        else:
            self._curr_mana = remaining_mana

    def increase_mana(self, restore_amount):
        """Restores sprite's mana, if new value doesn't exceed max_mana"""
        new_mana = self._curr_mana + restore_amount
        if new_mana >= self.max_mana:
            self._curr_mana = self.max_mana
        else:
            self._curr_mana = new_mana

    def attack(self, by=None):
        if by == 'weapon':
            return self.attack_by_weapon()
        elif by == 'magic' or by == 'spell':
            return self.attack_by_spell()
        else:
            raise ValueError("No weapon provided")

    def attack_points(self, by=None):
        return self.attack(by)

    def attack_by_weapon(self):
        weapon = self.__dict__.get('weapon', 0)
        if weapon == 0:
            return 0
        return weapon.damage

    def attack_by_spell(self):
        if self.can_cast():
            return self.spell.damage
        return 0

    def update_cords(self, new_y, new_x):
        self.y_coord = new_y
        self.x_coord = new_x

    def distance_from(self, other):
        return abs(self.y_coord - other.y_coord) \
               + abs(self.x_coord - other.x_coord)

    def has_weapon(self):
        return getattr(self, 'weapon', None)

    def has_spell(self):
        return getattr(self, 'spell', None)


class Hero(Sprite):
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        super().__init__(health, mana)
        self._name = name
        self._tile = title
        self._mana_regeneration_rate = mana_regeneration_rate

    def __str__(self):
        return 'H'

    def __repr__(self):
        return str(self)

    @property
    def mana_regeneration_rate(self):
        return self._mana_regeneration_rate

    def known_as(self):
        """Returns hero's name and title."""
        return f'{self._name} the {self._tile}'

    def equip(self, w):
        """Equips a new weapon."""
        self.weapon = w

    def learn(self, spell):
        """Equips a new spell."""
        self.spell = spell


class Enemy(Sprite):
    def __init__(self, health, mana, damage):
        super().__init__(health, mana)
        self._damage = damage

    def __str__(self):
        return 'E'

    def __repr__(self):
        return str(self)

    @property
    def damage(self):
        return self._damage

    @classmethod
    def from_json(cls, json_file):
        import json
        with open(json_file) as f:
            enemy_data = Enemy.pick_random_enemy(json.load(f))
        return cls(**enemy_data)

    @staticmethod
    def pick_random_enemy(enemies_data):
        from random import choice
        return choice(enemies_data)

# if __name__ == '__main__':
#     h = Hero('Billy', 'Wizard', health=250, mana=100, mana_regeneration_rate=2)
#     e = Enemy.from_json('enemies.json')
#     print(e.__dict__)
#


