from random import randint, choice

class OutOfBoardException(Exception):
    pass

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'Dot({self.x}, {self.y})'


class Ship:
    def __init__(self, bow, lenth, pos):
        self.bow = bow
        self.lenth = lenth
        self.pos = pos
        self.lives = lenth

    def get_dots(self):
        dots = [self.bow]
        x = self.bow.x
        y = self.bow.y
        for i in range(self.lenth - 1):
            if self.pos == 0:
                x += 1
            elif self.pos == 1:
                y += 1
            dots.append(Dot(x, y))
        return dots

a = Ship(Dot(1, 12), 4, 1)
print(a.get_dots())





