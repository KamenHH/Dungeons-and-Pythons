import os
from sprites import Enemy
from collectables import Weapon, Spell, Potion, TreasureChest
from fights import Fight


class Map:
    LEVELS_PATH = 'Levels'
    LEVELS = sorted(os.listdir(LEVELS_PATH))
    DIRECTIONS = {
        'up': (-1, 0),
        'down': (1, 0),
        'right': (0, 1),
        'left': (0, -1)
    }
    OBSTACLE = '#'
    TREASURE = 'T'
    ENEMY = 'E'
    FREE_SPACE = '.'
    GATEWAY = 'G'

    def __init__(self):
        self.map = Map.from_file(Map.LEVELS.pop(0))

    def __str__(self):
        # equivalent to print_map()
        result = ''
        for row in self.map:
            for cell in row:
                result += str(cell)
            result += '\n'
        return result

    def spawn(self, hero):
        for row in self.map:
            for cell in row:
                if cell == 'S':
                    setattr(self, 'hero', hero)
                    y = self.map.index(row)
                    x = row.index(cell)
                    self.hero.update_cords(y, x)
                    self.map[y][x] = self.hero
                    return

    def move_hero(self, direction):
        prev_y_hero, prev_x_hero = self.hero.y_coord, self.hero.x_coord
        new_direction = Map.DIRECTIONS.get(direction, (0, 0))
        new_y, new_x = new_direction[0] + prev_y_hero, new_direction[1] + prev_x_hero
        if new_x < 0 or new_y < 0:
            print('Can\'t move in that direction!')
            return False
        try:
            if self.map[new_y][new_x] == Map.FREE_SPACE:
                self.update_hero(prev_y_hero, prev_x_hero, new_y, new_x)
                return True
            elif self.map[new_y][new_x] == Map.OBSTACLE:
                print('Obstacle in the way!')
                return False
            elif self.map[new_y][new_x] == Map.TREASURE:
                treasure = TreasureChest().treasure
                print(f'Found {treasure._name}')
                self.determine_treasure(treasure)
                self.update_hero(prev_y_hero, prev_x_hero, new_y, new_x)
                # TODO: implement treasure event
                return True
            elif isinstance(self.map[new_y][new_x], Enemy):
                self.hero_attack()
                self.update_hero(prev_y_hero, prev_x_hero, new_y, new_x)
                # e = Enemy.from_json('enemies.json')
                # b = battles.Battle(self.hero, e).start_battle()
                return False
            elif self.map[new_y][new_x] == Map.GATEWAY:
                self.found_gateway()
                return False
        except IndexError:
            print('Can\'t move in that direction!')
            return False

    def update_hero(self, prev_y, prev_x, new_y, new_x):
        self.map[prev_y][prev_x] = Map.FREE_SPACE
        self.map[new_y][new_x] = self.hero
        self.hero.update_cords(new_y, new_x)
        self.hero.increase_mana(self.hero.mana_regeneration_rate)

    def clear_enemy(self):
        for row in self.map:
            for cell in row:
                if isinstance(cell, Enemy) and not cell.is_alive():
                    self.map[self.map.index(row)][row.index(cell)] = Map.FREE_SPACE

    def found_gateway(self):
        try:
            self.map = Map.from_file(Map.LEVELS.pop(0))
            self.hero.take_healing(self.hero.max_health)
            self.hero.increase_mana(self.hero.max_mana)
            self.spawn(self.hero)
            print("You have reached the end of the level!\nBrace yourself for the upcoming one..")
            print(self)
        except IndexError:
            print('Congratulations, you have reached the end ot the dungeon and vanquished all the pythons!\n'
                  f'{self.hero.known_as()}, you are a TRUE hero!')
            exit(0)

    def determine_treasure(self, treasure):
        if isinstance(treasure, Potion):
            health_amount, mana_amount = treasure.use()
            self.hero.take_healing(health_amount)
            self.hero.increase_mana(mana_amount)
        if isinstance(treasure, Weapon):
            self.hero.equip(treasure)
        if isinstance(treasure, Spell):
            self.hero.learn(treasure)

    def spawn_enemies(self):
        self.enemies = [Enemy(100, 50, 10) for _ in range(self.get_enemy_count())]
        index_of_enemy = 0
        for index_row, row in enumerate(self.map):
            for index_cell, cell in enumerate(row):
                if cell == 'E':
                    enemy = self.enemies[index_of_enemy]
                    enemy.x_coord = index_cell
                    enemy.y_coord = index_row
                    self.map[index_row][index_cell] = enemy
                    index_of_enemy += 1

    def get_enemy_count(self):
        enemy_count = 0
        for row in self.map:
            for cell in row:
                if cell == 'E':
                    enemy_count += 1
        return enemy_count

    def hero_attack(self):
        closest_enemy = min(self.enemies, key=lambda enemy: self.hero.distance_from(enemy))
        fight = Fight(self.hero, closest_enemy)
        fight.process()

    @staticmethod
    def from_file(file):
        with open(os.path.join(Map.LEVELS_PATH, file)) as f:
            return [[cell for cell in row.strip()]
                    for row in f.readlines()]


# if __name__ == '__main__':
#     from sprites import Hero
#     TreasureChest.parse_json()
#     print(Map.LEVELS)
#     m = Map()
#     print(m)
#     h = Hero(name='Jon', title='Assassin', health=100, mana=125, mana_regeneration_rate=2)
#     h.equip(Weapon('Axe', 20, 1))
#     m.spawn(h)
#     m.spawn_enemies()
#     while True:
#         print(m)
#         pos = input('>')
#         m.move_hero(pos)

