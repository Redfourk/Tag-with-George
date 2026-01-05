#===================================================================================
#
# Tag with George
# Copyright © 2025 Redfourk and CatthonCoder
# This code uses the MIT license, for more information, see https://mit-license.org/
#
#===================================================================================
#
#
#       ~Chore list~
# Todo: Translate audio mechanics:
# my_music = html.AUDIO(src="https://codehs.com/uploads/8179d3793582c02c44438d0160d6f0a5")
# my_music.loop = True
# my_music
# .play()
# Todo: Implement player 2
# Todo: Find updated features added by CatthonCoder
# Todo: Clean up and format code
# Todo: Implement bushes
#
#
#

import tkinter as tk
import threading
import time
from pyglet import event
from pyglet.media import player
from pygments.lexers import q

import app_properties
from app_properties import *
import player1_properties
from player1_properties import *


window = tk.Tk()

window.title(window_title)
window.geometry(str(window_length) + "x" + str(window_width))
label = tk.Label(window, text=str(window_label))
background = tk.Canvas(window, width=canvas_width, height=canvas_height, bg=canvas_color)


# Create arrow-key player, referenced as "player1"

from player1_properties import player1_x0, player1_y0, player1_x1, player1_y1, player1_step
player1 = tk.Canvas.create_oval(background, player1_x0, player1_y0, player1_x1, player1_y1, outline="#FFFFFF", fill="#FFFFFF", width=15)

# Add movement script with keybinds for player1 (Up Arrow, Down Arrow, Left Arrow, Right Arrow)


STEP = player1_step

def move_player1(event):
    dx, dy = 0, 0
    if event.keysym == "Up":
        dy += -STEP
    if event.keysym == "Down":
        dy += STEP
    if event.keysym == "Left":
        dx += -STEP
    if event.keysym == "Right":
        dx += STEP

    background.move(player1, dx, dy)
    if is_collision(player1):
        background.move(player1, -dx, -dy)

    background.update_idletasks()

window.bind('<Up>', move_player1)
window.bind('<Down>', move_player1)
window.bind('<Left>', move_player1)
window.bind('<Right>', move_player1)





window.focus_set()
label.pack()
background.pack()
window.mainloop()
