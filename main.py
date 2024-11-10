"""Geometry Dust"""

import pygame
import pygame.draw
from pygame.colordict import THECOLORS
from freepygame import freetext, freebutton
import time
import sys

pygame.init()
frame_number = 60
display_size = (1920, 1080)
pygame.display.set_caption("freebird application")
pygame.display.set_icon(pygame.image.load("assets\\freebird_music.ico"))
screen = pygame.display.set_mode(display_size, pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.FULLSCREEN)
screen.fill(THECOLORS.get("grey0"))
buffer = pygame.Surface(display_size)
clock = pygame.time.Clock()

event_text = freetext.SuperText(screen, [3, 5], "", "assets\\simhei.ttf", size=10,
                                color=THECOLORS.get("grey70"))
button_exit = freebutton.FreeButton(screen, [display_size[0] - 80, 0], [80, 40],
                                    "EXIT", "assets\\simhei.ttf",
                                    border_color=THECOLORS.get("grey50"), draw_border=True, msg_tran=True)
button = [button_exit]

while True:
    event_text.set_msg("现在时间：" + str(time.localtime().tm_year) + "年 " + str(time.localtime().tm_mon) + "月 " +
                       str(time.localtime().tm_mday) + "日 " + str(time.localtime().tm_hour) + "时 " +
                       str(time.localtime().tm_min) + "分 " + str(time.localtime().tm_sec) + "秒   " +
                       "当前帧速率 " + str(int(clock.get_fps())) + "     Copyright (c) 2024 freebird")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif freebutton.position_button_class(button_exit, pygame.mouse.get_pos()) is True:
            button_exit.set_msg_color(THECOLORS.get("grey95"))
            button_exit.check_button = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()
        else:
            for unit in button:
                unit.check_button = False  # 这里的check_button是用于控制按钮是否被按下的，上面的代码中也有
        if event.type == pygame.WINDOWLEAVE:  # 当光标离开窗口后，坐标依然停留在离开前的位置，可能造成按钮一直被按下的假象
            for unit in button:  # 所以这里在设置一次
                unit.check_button = False

    for unit in button:
        if unit.check_button is False:
            unit.set_msg_color(THECOLORS.get("grey75"))
        unit.draw()

    event_text.draw()
    pygame.display.flip()
    screen.fill(THECOLORS.get("grey0"))
    clock.tick(frame_number)
