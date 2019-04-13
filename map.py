import os
import pdb
from collectables import TreasureChest, Potion, Weapon, Spell
class Map:
    LEVELS_PATH = 'Levels'
    DIRECTIONS = {
        'up': (-1, 0),
        'down': (1, 0),
        'right': (0, 1),
        'left': (-1, 0)
    }
    OBSTACLE = '#'
    TREASURE = 'T'
    ENEMY = 'E'
    FREE_SPACE = '.'
    GATEWAY = 'G'

    def __init__(self, matrix):
        self.map = matrix

    def __str__(self):
        # equivalent to print_map()
        result = ''
        for row in self.map:
            for cell in row:
                result += str(cell)
            result += '\n'
        return result
        # return '\n'.join([''.join(row) for row in self.map])

    def spawn(self, hero):
        for row in self.map:
            for cell in row:
                if cell == 'S':
                    setattr(self, 'hero', hero)
                    y = self.map.index(row)
                    x = row.index(cell)
                    self.hero.update_cords(y, x)
                    self.map[y][x] = hero
                return


    def move_hero(self, direction):
        prev_y_hero, prev_x_hero  = self.hero.y_coord, self.hero.x_coord
        new_direction = Map.DIRECTIONS.get(direction, (0 ,0))
        new_y, new_x = new_direction[0] + prev_y_hero, new_direction[1] + prev_x_hero
        if new_x < 0 or new_y < 0:
            return False
        try:
            if self.map[new_y][new_x] == Map.FREE_SPACE:
                pdb.set_trace()
                self.map[prev_y_hero][prev_x_hero] = Map.FREE_SPACE
                self.map[new_y][new_x] = self.hero
                self.hero.update_cords(new_y, new_x)
                return True
            elif self.map[new_y][new_x] == Map.OBSTACLE:
                print('Obstacle in the way!')
                return False
            elif self.map[new_y][new_x] == Map.TREASURE:
                print('Found treasure!')
                treasure = TreasureChest().treasure
                print('Found %s!' % treasure.__class__.__name__)
                self.hero.take_damage(50)
                if isinstance(treasure, Potion):
                    health_amount, mana_amount = treasure.use()
                    self.hero.take_healing(health_amount)
                    self.hero.take_mana(mana_amount)
                if isinstance(treasure, Weapon):
                    self.hero.equip(treasure)
                if isinstance(treasure, Spell):
                    self.hero.learn(treasure)
                print(self.hero.__dict__)
                return False
            elif self.map[new_y][new_x] == Map.ENEMY:
                # TODO: implement enemy event
                return False
            elif self.map[new_y][new_x] == Map.GATEWAY:
                # TODO: implement gateway event
                return False
        except IndexError:
            # print('Edge of the maze reached!')
            return False

    def attack(by=None):
        print(by)
        attack_by_weapon()

    def attack_by_weapon():
        print(self.hero__dict__)

    @classmethod
    def from_file(cls):
        with open(os.path.join(Map.LEVELS_PATH, 'level1.txt')) as f:
            return cls([[cell for cell in row.strip()]
                        for row in f.readlines()])


if __name__ == '__main__':
    from sprites import Hero
    m = Map.from_file()
    print(m)
    h = Hero(name='Jon', title='Assasin', health=100, mana=125, mana_regeneration_rate=2)
    m.spawn(h)
    print(m)
    print(m.move_hero('right'))
    print(m.move_hero('down'))
    print(m.hero.attack(by="weapon"))

