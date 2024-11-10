"""game logic"""

import pygame
import pygame.draw
import random

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
