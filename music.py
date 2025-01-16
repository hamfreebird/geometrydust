"""music logic"""
# TODO: 判定算法有问腿


import pygame
import pygame.draw
from pygame.colordict import THECOLORS

# line = [600, 960], [1800, 960]

def read_spectroscopy(film):
    spectroscopy_film = open(film, "r")
    spectroscopy = [[], [], [], [], []]
    spectroscopy_name = ""
    for index, line in enumerate(spectroscopy_film):
        if index == 1:
            spectroscopy_name = line
        if index <= 2 or index >= 10803:
            continue
        spectroscopy[0].append(line[0:5])
        spectroscopy[1].append(int(line[11]))
        spectroscopy[2].append(int(line[22]))
        spectroscopy[3].append(int(line[33]))
        spectroscopy[4].append(int(line[44]))
    return spectroscopy_name, spectroscopy

def get_decision_frame(begin_time, now_time, frame_time=2000):
    return int((now_time - begin_time) / (10000000000 / frame_time))

class Spectroscopy():
    def __init__(self, screen, spectroscopy_name, spectroscopy):
        self.screen = screen
        self.spectroscopy_name = spectroscopy_name
        self.spectroscopy = spectroscopy
        self.note_list = []

    def check_one(self, key_s, key_f, key_h, key_k, move_speed=10):
        start = 960 - (10 * move_speed)
        end = 960 + (5 * move_speed)
        return_note = []
        for index, note in enumerate(self.note_list):
            if (note[1] > end) and (note[2] is not THECOLORS.get("green")) and note[3] != -1 and note[3] != 1:
                note[3] = -1
                return_note.append(note)
            if (start <= note[1] <= end) and note[3] != -1 and note[3] != 1:
                if note[0] == 760 and key_s is True:
                    note[2] = THECOLORS.get("green")
                if note[0] == 1010 and key_f is True:
                    note[2] = THECOLORS.get("green")
                if note[0] == 1260 and key_h is True:
                    note[2] = THECOLORS.get("green")
                if note[0] == 1510 and key_k is True:
                    note[2] = THECOLORS.get("green")
                note[3] = 1
                return_note.append(note)
        return return_note

    def draw(self, decision_time, last_frame, move_speed=10, is_play=True):
        if last_frame != decision_time and is_play is True:
            self.put_note_into_list(decision_time)
        if len(self.note_list) >= 80:
            self.note_list.pop(0)
        for index, note in enumerate(self.note_list):
            if index >= 100:
                break
            if note[1] <= (965 + 5 * move_speed):
                pygame.draw.rect(self.screen, note[2], [note[0], note[1], 100, 5], 1)
            if is_play is True:
                note[1] += move_speed

    def put_note_into_list(self, decision_time):
        if self.spectroscopy[1][decision_time] == 1:
            self.note_list.append([760, 280, THECOLORS.get("grey75"), 0])
        if self.spectroscopy[2][decision_time] == 1:
            self.note_list.append([1010, 280, THECOLORS.get("grey75"), 0])
        if self.spectroscopy[3][decision_time] == 1:
            self.note_list.append([1260, 280, THECOLORS.get("grey75"), 0])
        if self.spectroscopy[4][decision_time] == 1:
            self.note_list.append([1510, 280, THECOLORS.get("grey75"), 0])

    def get_spectroscopy_name(self):
        return self.spectroscopy_name

    def get_spectroscopy(self):
        return self.spectroscopy

    def get_note_list(self):
        return self.note_list


class Time():
    def __init__(self, fps=100):
        self.fps = fps

    def get_fps(self):
        return self.fps

