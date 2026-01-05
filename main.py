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




def move_player1(event):
    dx, dy = 0, 0
    if event.keysym == "Up":
        dy += -player1_step
    if event.keysym == "Down":
        dy += player1_step
    if event.keysym == "Left":
        dx += -player1_step
    if event.keysym == "Right":
        dx += player1_step

    background.move(player1, dx, dy)
    if is_collision(player1):
        background.move(player1, -dx, -dy)

    background.update_idletasks()

window.bind('<Up>', move_player1)
window.bind('<Down>', move_player1)
window.bind('<Left>', move_player1)
window.bind('<Right>', move_player1)

# Player 2:

from player2_properties import player2_x0, player2_y0, player2_x1, player2_y1, player2_step
player2 = tk.Canvas.create_oval(background, player2_x0, player2_y0, player2_x1, player2_y1, outline="#DE5844", fill="#DE5844", width=15)

def move_player2(event):
    dx, dy = 0, 0
    if event.keysym == "W" or event.keysym == "w":
        dx, dy = 0, -player2_step
    elif event.keysym == "S" or event.keysym == "s":
        dx, dy = 0, player2_step
    elif event.keysym == "A" or event.keysym == "a":
        dx, dy = -player2_step, 0
        background.update_idletasks()
    elif event.keysym == "D" or event.keysym == "d":
        dx, dy = player2_step, 0

    background.move(player2, dx, dy)
    if is_collision(player2):
        background.move(player2, -dx, -dy)

    background.update_idletasks()

window.bind('<W>', move_player2)
window.bind('<S>', move_player2)
window.bind('<A>', move_player2)
window.bind('<D>', move_player2)

window.bind('<w>', move_player2)
window.bind('<s>', move_player2)
window.bind('<a>', move_player2)
window.bind('<d>', move_player2)

# Barriers:

south_barrier = tk.Canvas.create_rectangle(background, 0, 1045, 2000, 1055, outline="#573c21", fill="#573c21", width=10)
north_barrier = tk.Canvas.create_rectangle(background, 0, 0, 1900, 10, outline="#573c21", fill="#573c21", width=10)
east_barrier = tk.Canvas.create_rectangle(background, 1900, 0, 1905, 1045, outline="#573c21", fill="#573c21", width=10)
west_barrier = tk.Canvas.create_rectangle(background, 0, 0, 10, 1045, outline="#573c21", fill="#573c21", width=10)

barriers = [south_barrier, north_barrier, east_barrier, west_barrier]


def is_collision(player_id):
    coords = background.coords(player_id)
    overlapping_items = background.find_overlapping(coords[0], coords[1], coords[2], coords[3])
    for item in overlapping_items:
        if item in barriers:
            return True
    return False



window.focus_set()
label.pack()
background.pack()
window.mainloop()
