class Fight:
    def __init__(self, hero, enemy):
        self._hero = hero
        self._enemy = enemy

    @property
    def hero(self):
        return self._hero

    @property
    def enemy(self):
        return self._enemy

    def process(self):
        print('A fight is started between our Hero(health={}, mana={}) and Enemey(health={}, mana={}, damage={})'
            .format(self.hero.get_health(), self.hero.get_mana(), self.enemy.get_health(), self.enemy.get_mana(), self.enemy.damage))

        while self.hero.is_alive() and self.enemy.is_alive():
            self.hero_attacks_enemy()
            self.enemy_attacks_hero()

    def hero_attacks_enemy(self):
        if self.hero.is_alive() is False:
            return
        distance = self.distance()
        if distance == 1:
            damage_by_weapon = self.hero.attack_points(by='weapon')
            damage_by_spell = self.hero.attack_points(by='spell')
            if damage_by_weapon > damage_by_spell:
                print(f'{self.hero.known_as()} deals {damage_by_weapon} to Enemy, using {self.hero.weapon}.')
                self.enemy.lose_health(damage_by_weapon)
            else:
                print(f'{self.hero.known_as()} deals {damage_by_weapon} to Enemy, using {self.hero.spell}.')
                self.enemy.lose_health(damage_by_spell)
                mana_for_spell = self.hero.__dict__.get('spell', 0).mana_cost
                self.hero.spend_mana(mana_for_spell)
            print(f'Enemy left with {self.enemy.get_health()} health points.')

    def enemy_attacks_hero(self):
        if self.enemy.is_alive() is False:
            return
        damage_by_weapon = self.enemy.attack_points(by='weapon')
        damage_by_spell = self.enemy.attack_points(by='spell')
        enemy_damage = self.enemy.damage
        max_damage = max(damage_by_weapon, damage_by_spell, enemy_damage)
        print(f'Enemy deals {max_damage} to {self.hero.known_as()}.')
        self.hero.lose_health(max_damage)
        print(f'{self.hero.known_as()} left with {self.hero.get_health()} health points.')
        if max_damage == damage_by_spell:
            mana_for_spell = self.enemy.__dict__.get('spell', 0).mana_cost
            self.enemy.spend_mana(mana_for_spell)

    def distance(self):
        return abs(self.hero.y_coord - self.enemy.y_coord) \
             + abs(self.hero.x_coord - self.enemy.x_coord)

#
# if __name__ == '__main__':
#     from sprites import Hero, Enemy
#     from collectables import Weapon
#     h = Hero('Bron', 'Dragonslayer', 250, 100, 2)
#     e = Enemy('Some', 'Creature', 100, 10, 10)
#     w = Weapon('Axe', 20, 1)
#     f = Fight(h, e)
#     f.process()