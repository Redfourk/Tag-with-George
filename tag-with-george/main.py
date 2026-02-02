#===================================================================================
#
# Tag with George
# Copyright © 2025-2026 Redfourk and CatthonCoder
# This code uses the MIT license, for more information, see https://mit-license.org/
#
#===================================================================================
#
project_version = "0.1.0-beta.1"
#
#       ~Chore list~
# Todo: Find updated features added by CatthonCoder
# Todo: Clean up and format code
# Todo: Implement bushes
#
#
#

print("""===================================================================================
Tag with George
Copyright © 2025-2026 Redfourk and CatthonCoder
This code uses the MIT license, for more information, see https://mit-license.org/
===================================================================================
""")
print("Current project version: " + project_version)
print("Fetching dependencies...")
import html
import tkinter as tk
import threading
import random
import pygame
from pygame import mixer
import dash
from dash.html import Audio
import app_properties
from app_properties import *
import os

from PIL import Image, ImageTk

print("Opening project window...")

window = tk.Tk()

window.title(window_title)
window.geometry(str(window_length) + "x" + str(window_width))
label = tk.Label(window, text=str(window_label))
background = tk.Canvas(window, width=canvas_width, height=canvas_height, bg=canvas_color)


# Create arrow-key player, referenced as "player1"

print("Making player 1...")

from player1_properties import player1_x0, player1_y0, player1_x1, player1_y1, player1_step
player1 = tk.Canvas.create_oval(background, player1_x0, player1_y0, player1_x1, player1_y1, outline="#FFFFFF", fill="#FFFFFF", width=15, tags="shape")

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
    game_over_monitor()

window.bind('<Up>', move_player1)
window.bind('<Down>', move_player1)
window.bind('<Left>', move_player1)
window.bind('<Right>', move_player1)

# Player 2:

print("Making player 2...")

from player2_properties import player2_x0, player2_y0, player2_x1, player2_y1, player2_step
player2 = tk.Canvas.create_oval(background, player2_x0, player2_y0, player2_x1, player2_y1, outline="#DE5844", fill="#DE5844", width=15, tags="shape")

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
    game_over_monitor()

window.bind('<W>', move_player2)
window.bind('<S>', move_player2)
window.bind('<A>', move_player2)
window.bind('<D>', move_player2)

window.bind('<w>', move_player2)
window.bind('<s>', move_player2)
window.bind('<a>', move_player2)
window.bind('<d>', move_player2)

# Barriers:

print("Setting barriers...")

south_barrier = tk.Canvas.create_rectangle(background, 0, 695, 2000, 700, outline="#573c21", fill="#573c21", width=10, tags="shape")
north_barrier = tk.Canvas.create_rectangle(background, 0, 0, 1900, 10, outline="#573c21", fill="#573c21", width=10, tags="shape")
east_barrier = tk.Canvas.create_rectangle(background, 1265, 0, 1905, 1045, outline="#573c21", fill="#573c21", width=10, tags="shape")
west_barrier = tk.Canvas.create_rectangle(background, 0, 0, 10, 1045, outline="#573c21", fill="#573c21", width=10, tags="shape")

barriers = [south_barrier, north_barrier, east_barrier, west_barrier]
players = [player1, player2]

print("Defining events...")

def game_over_monitor():
    if background.coords(player1) == background.coords(player2):
        ending_bg = tk.Canvas.create_rectangle(background, 0, 0, 5000, 5000, outline="black", fill="black", )
        ending_text = tk.Canvas.create_text(background, 600, 300, text="The tagger won!", fill="white", font=("Cursive", 20))
        ending_face = tk.Canvas.create_text(background, 600, 200, text="☺", fill="white", font=("Arial", 150))
    else:
        return

def is_collision(player_id):
    coords = background.coords(player_id)
    overlapping_items = background.find_overlapping(coords[0], coords[1], coords[2], coords[3])
    for item in overlapping_items:
        if item in barriers:
            return True
    return False


# Bushes:

#|************************
#|Currently in development
#|************************

"""
def bush(x, y):
    r = x - 5
    R = x - 15
    F = x - 30
    t = y - 5
    bush_circ1 = tk.Canvas.create_oval(background, R - 15, t - 15, R + 15, t + 15, outline="#0e6101", fill="#0e6101", width=15, tags="shape")
    bush_circ2 = tk.Canvas.create_oval(background, x - 10, y - 10, x + 10, y + 10, outline="#0e6101", fill= "#0e6101", width=10, tags="shape")
    bush_rect = tk.Canvas.create_rectangle(background, F + 20, y + 20, F + 20, y + 20, outline="#0e6101", fill="#0e6101", width=40, tags="shape")

for i in range (10):
    random_gen_x = random.randint(50, 350)
    random_gen_y = random.randint(50, 500)
    bush(random_gen_x, random_gen_y)
"""

# Music:

print("Playing music...")

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

try:
    pygame.mixer.music.load("tag.mp3")
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(-1)
except pygame.error as e:
    print(f"Could not load music file: {e}")


print("Finalizing...")

window.focus_set()
label.pack()
background.pack()
window.mainloop()