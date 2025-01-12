"""Geometry Dust"""

import pygame
import pygame.draw
from pygame.colordict import THECOLORS
from freepygame import freetext, freebutton, freeicon
import music
import time
import sys

pygame.init()
frame_number = 120
display_size = (1920, 1080)
pygame.display.set_caption("freebird application")
pygame.display.set_icon(pygame.image.load("assets\\geometrydust.ico"))
screen = pygame.display.set_mode(display_size, pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.FULLSCREEN)
screen.fill(THECOLORS.get("grey0"))
buffer = pygame.Surface(display_size)
clock = pygame.time.Clock()

event_text = freetext.SuperText(screen, [3, 5], "", "assets\\simhei.ttf", size=10,
                                color=THECOLORS.get("grey70"))

icon_main_title = freeicon.FreeIcon(screen, (100, 100), pygame.image.load("assets\\icon\\icon_main_title.PNG"),
                                pygame.image.load("assets\\icon\\icon_play_title.PNG"))
icon = [icon_main_title]

text_main_title = freetext.SuperText(screen, [600, 120], "Geometry Dust", "assets\\simhei.ttf",
                                size=30, color=THECOLORS.get("grey90"))
text_play_title = freetext.SuperText(screen, [600, 160], "stop", "assets\\simhei.ttf", size=15,
                                color=THECOLORS.get("grey80"))
text_s = freetext.SuperText(screen, [800, 990], "<s>", "assets\\simhei.ttf", size=15,
                                color=THECOLORS.get("grey60"))
text_f = freetext.SuperText(screen, [1050, 990], "<f>", "assets\\simhei.ttf", size=15,
                                color=THECOLORS.get("grey60"))
text_h = freetext.SuperText(screen, [1300, 990], "<h>", "assets\\simhei.ttf", size=15,
                                color=THECOLORS.get("grey60"))
text_k = freetext.SuperText(screen, [1550, 990], "<k>", "assets\\simhei.ttf", size=15,
                                color=THECOLORS.get("grey60"))
text = [text_main_title, text_play_title, text_s, text_f, text_h, text_k]

button_exit = freebutton.FreeButton(screen, [display_size[0] - 40, 0], [40, 20],
                                "EXIT", "assets\\simhei.ttf", size=10, border_color=THECOLORS.get("grey50"),
                                draw_border=True, msg_tran=True)
button = [button_exit]

play = False

while True:
    event_text.set_msg("现在时间：" + str(time.localtime().tm_year) + "年 " + str(time.localtime().tm_mon) + "月 " +
                       str(time.localtime().tm_mday) + "日 " + str(time.localtime().tm_hour) + "时 " +
                       str(time.localtime().tm_min) + "分 " + str(time.localtime().tm_sec) + "秒   " +
                       "当前帧速率 " + str(int(clock.get_fps())) + "     Copyright (c) 2024 freebird")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                text_s.set_msg("---")
            elif event.key == pygame.K_f:
                text_f.set_msg("---")
            elif event.key == pygame.K_h:
                text_h.set_msg("---")
            elif event.key == pygame.K_k:
                text_k.set_msg("---")
            elif event.key == pygame.K_SPACE:
                icon_main_title.set_index(1)
                if play is False:
                    play = True
                    text_play_title.set_msg("play")
                    icon_main_title.check_button = True
                else:
                    play = False
                    text_play_title.set_msg("stop")
                    icon_main_title.check_button = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                text_s.set_msg("<s>")
            elif event.key == pygame.K_f:
                text_f.set_msg("<f>")
            elif event.key == pygame.K_h:
                text_h.set_msg("<h>")
            elif event.key == pygame.K_k:
                text_k.set_msg("<k>")
        elif freebutton.position_button_class(button_exit, pygame.mouse.get_pos()) is True:
            button_exit.set_msg_color(THECOLORS.get("grey95"))
            button_exit.check_button = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()
        elif freebutton.position_button([100, 500, 100, 500], pygame.mouse.get_pos()) is True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                icon_main_title.set_index(1)
                if play is False:
                    play = True
                    text_play_title.set_msg("play")
                    icon_main_title.check_button = True
                else:
                    play = False
                    text_play_title.set_msg("stop")
                    icon_main_title.check_button = False
        else:
            for unit in button:
                unit.check_button = False  # 这里的check_button是用于控制按钮是否被按下的，上面的代码中也有
        if event.type == pygame.WINDOWLEAVE:  # 当光标离开窗口后，坐标依然停留在离开前的位置，可能造成按钮一直被按下的假象
            for unit in button:  # 所以这里在设置一次
                unit.check_button = False

    if play is True:
        icon_main_title.set_index(1)
    else:
        icon_main_title.set_index(0)

    for unit in icon:
        if unit.display_button is False:
            continue
        if unit.check_button is False:
            unit.set_index(0)
        unit.draw()
    for unit in button:
        if unit.check_button is False:
            unit.set_msg_color(THECOLORS.get("grey75"))
        unit.draw()
    for unit in text:
        unit.draw()

    pygame.draw.aaline(screen, THECOLORS.get("grey50"), [0, 20], [1920, 20], 1)
    pygame.draw.aaline(screen, THECOLORS.get("grey70"), [548, 50], [548, 1030], 1)
    pygame.draw.aaline(screen, THECOLORS.get("grey70"), [552, 50], [552, 1030], 1)
    pygame.draw.aaline(screen, THECOLORS.get("grey70"), [600, 960], [1800, 960], 1)

    event_text.draw()
    pygame.display.flip()
    screen.fill(THECOLORS.get("grey0"))
    clock.tick(frame_number)
