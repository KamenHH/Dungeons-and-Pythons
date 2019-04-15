import pdb
import json
import math
class Sprite:
    def __init__(self, health, mana):
        self._curr_health = health
        self._max_health = health
        self._curr_mana = mana
        self._max_mana = mana
        # self._curr_position = curr_position

    # def __repr__(self):
    #     """For debugging.."""
    #     return ', '.join([str((k, v)) for k, v in self.__dict__.items()])

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

    def is_alive(self):
        """Returns true if current health is greater than 0."""
        return self._curr_health > 0

    def can_cast(self):
        """Returns true if current mana is greater than 0 and enougf to cast spell."""
        spell = self.__dict__.get('spell', 0)
        return spell != 0 and self.get_mana() >= spell.mana_cost

    def take_damage(self, damage):
        """Decreases sprite's health based on the given damage factor."""
        remaining_health = self._curr_health - damage
        if remaining_health <= 0:
            self._curr_health = 0
        else:
            self._curr_health = remaining_health

    def distance_from(self, other):
        return math.fabs(self.y_coord - other.y_coord) \
             + math.fabs(self.x_coord - other.x_coord)

    # use lose_health instead of take_damage to make it clearer what method does
    def lose_health(self, damage):
        self.take_damage(damage)

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
            
    def take_mana(self, restore_amount):
        """Restores sprite's mana, if new value doesn't exceed max_mana"""
        new_mana = self._curr_mana + restore_amount
        if new_mana >= self.max_mana:
            self._curr_mana = self.max_mana
        else:
            self._curr_mana = new_mana

    # use increase_mana instead of take_mana to make it clearer what method does
    def increase_mana(self, restore_amount):
        self.take_mana(restore_amount)

    def attack(self, by=None):
        if by == 'weapon':
            return self.attack_by_weapon()
        elif by == 'magic' or by == 'spell':
            return self.attack_by_spell()
        else:
            raise ValueError("No weapon provided")

    def attack_points(self, by='None'):
        return self.attack(by)

    def attack_by_weapon(self):
        weapon = self.__dict__.get('weapon', 0)
        if weapon == 0:
            return 0
        else:
           return weapon.damage

    def attack_by_spell(self):
        if self.can_cast():
            spell = self.__dict__.get('spell', 0)
            return spell.damage
        return 0
    # I didn't understand that logic so I wrote another method above 
    # def attack(self, by=None):
    #     # pdb.set_trace()
    #     if self._curr_mana == 0:
    #         damage, mana_cost = self.__dict__.get('weapon', 0).use()
    #     else:
    #         damage, mana_cost = self.__dict__.get(by, 0).use()
    #         if mana_cost != 0:
    #             self.spend_mana(mana_cost)
    #     return damage

    def update_cords(self, new_y, new_x):
        self.y_coord = new_y
        self.x_coord = new_x

    # def move(self, direction):
    #     """Move sprite in one of 4 possible directions.
    #         Adds, the coordinates of the new position to those of the current one."""
    #     # direction tuple = (down & up <y-axis>, right & left <x-axis>)
    #     directions = {'up': (-1, 0),
    #                   'down': (1, 0),
    #                   'right': (0, 1),
    #                   'left': (0, -1)
    #                   }
    #     new_direction = directions.get(direction, (0, 0))
    #     self.y_coord += new_direction[0]
    #     self.x_coord += new_direction[1]



class Hero(Sprite):
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        super().__init__(health, mana)
        self._name = name
        self._title = title
        self._mana_regeneration_rate = mana_regeneration_rate

    def __str__(self):
        return 'H'

    def __repr__(self):
        return str(self)

    def known_as(self):
        pass
        """Returns hero's name and title."""
        # return f'{self._name} the {self._tile}'

    def equip(self, w):
        """Equips a new weapon."""
        self.weapon = w

    def learn(self, spell):
        """Equips a new spell."""
        self.spell = spell


class Enemy(Sprite):
    # TODO Parse enemy object while parsing map
    # Enemy should also have coordinates, same as Hero
    def __init__(self, health, mana, damage):
        super().__init__(health, mana)
        self._damage = damage
    
    # def __str__(self):
    #     return 'E'

    def __str__(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return str(self)

    @property
    def damage(self):
        return self._damage


if __name__ == '__main__':
    h = Hero('Billy', 'Wizard', health=250, mana=100, mana_regeneration_rate=2)
    print(h.__dict__)
    # print(h.is_alive())
    # print(h.known_as())
    # import time
    # while True:
    #     h.take_healing(21)
    #     print(h.get_health())
    #     time.sleep(0.5)
    #     print(h.is_alive())
    h.x_coord = 10
    print(h.x_coord)    




