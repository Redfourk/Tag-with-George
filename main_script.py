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
#       ~~~Code Starts Here~~~

# Import necessary resources

import tkinter as tk
import threading
from pyglet import event
from pyglet.media import player

# Create application window. App Name: "window"
# Line below MUST be first tkinter related code to execute!
window = tk.Tk()

window.title("Tkinter window")
window.geometry("2000x1200")
label = tk.Label(window, text="Tag with George v0.1.0")

# Create app backdrop (technically a rectangle). Shape creation format: shape_name = tk.Canvas(app_name, width=__, height=__, bg= "lowercase")

background = tk.Canvas(window, width=2000, height=1200, bg="#8CC63E")

# Create arrow-key player, referenced as "player1"

player1_x0 = 1740
player1_y0 = 590
player1_x1 = 1760
player1_y1 = 610
player1 = tk.Canvas.create_oval(background, player1_x0, player1_y0, player1_x1, player1_y1, outline="#FFFFFF", fill="#FFFFFF", width=15)

# Add movement script with keybinds for player1 (Up Arrow, Down Arrow, Left Arrow, Right Arrow)
# NOTE: Move left process must refresh screen, otherwise ghosting will occur

STEP = 10

def move_player1(event):
    if event.keysym == "Up":
        background.move(player1, 0, -STEP)
    elif event.keysym == "Down":
        background.move(player1, 0, STEP)
    elif event.keysym == "Left":
        background.move(player1, -STEP, 0)
        background.update_idletasks()
    elif event.keysym == "Right":
        background.move(player1, STEP, 0)

window.bind('<Up>', move_player1)
window.bind('<Down>', move_player1)
window.bind('<Left>', move_player1)
window.bind('<Right>', move_player1)

# Create WASD player, referenced as "player2"

player2_x0 = 240
player2_y0 = 590
player2_x1 = 260
player2_y1 = 610
player2 = tk.Canvas.create_oval(background, player2_x0, player2_y0, player2_x1, player2_y1, outline="#DE5844", fill="#DE5844", width=15)

def move_player2(event):
    if event.keysym == "W" or event.keysym == "w":
        background.move(player2, 0, -STEP)
    elif event.keysym == "S" or event.keysym == "s":
        background.move(player2, 0, STEP)
    elif event.keysym == "A" or event.keysym == "a":
        background.move(player2, -STEP, 0)
        background.update_idletasks()
    elif event.keysym == "D" or event.keysym == "d":
        background.move(player2, STEP, 0)

window.bind('<W>', move_player2)
window.bind('<S>', move_player2)
window.bind('<A>', move_player2)
window.bind('<D>', move_player2)

window.bind('<w>', move_player2)
window.bind('<s>', move_player2)
window.bind('<a>', move_player2)
window.bind('<d>', move_player2)

# Barrier

south_barrier = tk.Canvas.create_rectangle(background, 0, 1045, 2000, 1050, outline="#573c21", fill="#573c21", width=10)
north_barrier = tk.Canvas.create_rectangle(background, 0, 0, 2000, 10, outline="#573c21", fill="#573c21", width=10)
east_barrier = tk.Canvas.create_rectangle(background, 1902.5, 0, 1902.5, 1902.5, outline="#573c21", fill="#573c21", width=10)
west_barrier = tk.Canvas.create_rectangle(background, 0, 0, 10, 1045, outline="#573c21", fill="#573c21", width=10)

# Old barrier code
#
# rect = Rectangle(500, 10)
# rect.set_position(0, 470)
# rect.set_color("#573c21")
# add(rect)
# rec = Rectangle(10, 500)
# rec.set_position(390, 0)
# rec.set_color("#573c21")
# add(rec)
# rectd = Rectangle(10, 500)
# rectd.set_position(0, 0)
# rectd.set_color("#573c21")
# add(rectd)
# recte = Rectangle(500, 10)
# recte.set_position(0, 0)
# recte.set_color("#573c21")
# add(recte)


window.focus_set()
label.pack()
background.pack()
window.mainloop()


# 350, 200 out of 400x400
# 1750, 600
# 1740, 590
# 1760, 610





