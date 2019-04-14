import os


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
            print('Can\t move in that direction!')
            return False
        try:
            if self.map[new_y][new_x] == Map.FREE_SPACE:
                self.update_hero(prev_y_hero, prev_x_hero, new_y, new_x)
                return True
            elif self.map[new_y][new_x] == Map.OBSTACLE:
                print('Obstacle in the way!')
                return False
            elif self.map[new_y][new_x] == Map.TREASURE:
                print('Treasure found!')
                self.update_hero(prev_y_hero, prev_x_hero, new_y, new_x)
                # TODO: implement treasure event
                return True
            elif self.map[new_y][new_x] == Map.ENEMY:
                # TODO: implement battle event
                return False
            elif self.map[new_y][new_x] == Map.GATEWAY:
                self.found_gateway()
                return False
        except IndexError:
            print('Can\t move in that direction!')
            return False

    def update_hero(self, prev_y, prev_x, new_y, new_x):
        self.map[prev_y][prev_x] = Map.FREE_SPACE
        self.map[new_y][new_x] = self.hero
        self.hero.update_cords(new_y, new_x)

    def found_gateway(self):
        try:
            self.map = Map.from_file(Map.LEVELS.pop(0))
            self.hero.take_healing(self.hero.max_health)
            self.hero.take_mana(self.hero.max_mana)
            self.spawn(self.hero)
            print("You have reached the end of the level!\nBrace yourself for the upcoming one..")
        except IndexError:
            print('Congratulations, you have reached the end ot the dungeon and vanquished all the pythons!\n'
                  f'{self.hero.known_as()}, you are a TRUE hero!')
            exit(0)

    @staticmethod
    def from_file(file):
        with open(os.path.join(Map.LEVELS_PATH, file)) as f:
            return [[cell for cell in row.strip()]
                    for row in f.readlines()]


if __name__ == '__main__':
    from sprites import Hero
    print(Map.LEVELS)
    m = Map()
    print(m)
    h = Hero(name='Jon', title='Assassin', health=100, mana=125, mana_regeneration_rate=2)
    m.spawn(h)
    while True:
        print(m)
        pos = input('>')
        m.move_hero(pos)

