"""game logic"""

import pygame
import pygame.draw
import random
import numpy as np

def random_triangle_in_line(line, line_len, spacing, is_x = True):
    if is_x is True:
        number = int(line_len / spacing)
        size = int((spacing / 2) - 5)
        points = [[line, index * spacing] for index in range(0, number + 1)]

class Triangle():

    def __init__(self, screen, pos, width, color):
        self.screen = screen
        self.pos = pos
        self.width = width
        self.color = color

    def get_pos(self):
        return self.pos

    def set_pos(self, pos):
        self.pos = pos

    def draw(self):
        pygame.draw.lines(self.screen, self.color, True, self.pos, self.width)

class Fractal:
    def __init__(self, fractal_type: str):
        if fractal_type == "tree":
            self.fractal_type = 1
        elif fractal_type == "triangle":
            self.fractal_type = 2
        else:
            self.fractal_type = 0

    def set_tree(self):
        pass

    def iter_tree(self):
        pass

def iter_point(c, n, m):
    z = c
    for i in range(0, n):
        if abs(z) > 2:
            break
        z = pow(z, m) + c
    return i

def get_leaf_dots(p, func, init, n):
    pos = np.ones(3, dtype = np.float)
    pos[:2] = init
    result = np.zeros((n, 2), dtype = np.float)
    np.random.seed(0)
    probility = np.array(p)
    for i in range(0, n):
        index = np.random.choice([0, 1, 2, 3], p = probility.ravel())
        temp = np.dot(func[index], pos)
        pos[:2] = temp
        result[i] = temp
    return result[:, 0], result[:, 1]
