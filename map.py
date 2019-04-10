import os


class Map:
    LEVELS_PATH = 'Levels'

    def __init__(self, matrix):
        self.map = matrix

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.map])

    @classmethod
    def from_file(cls):
        with open(os.path.join(Map.LEVELS_PATH, 'level1.txt')) as f:
            return cls([[cell for cell in row.strip()]
                        for row in f.readlines()])


if __name__ == '__main__':
    m = Map.from_file()
    print(m)



