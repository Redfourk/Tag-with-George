#import pygame
#import pynput
import arcade
#from pygame import display
# from pygame.event import Event
# from pyglet import window
# from pyglet.input.linux.evdev_constants import KEY_LEFT
# from pynput import keyboard
import tkinter as tk

# print(f"Pygame imported successfully, version: {pygame.version.ver}")
# print("Pynput keyboard module imported successfully")

# Stuff to figure out later...

# my_music = html.AUDIO(src="https://codehs.com/uploads/8179d3793582c02c44438d0160d6f0a5")
# my_music.loop = True
# my_music
# .play()

window = tk.Tk()

player1_x = 350
player1_y = 200


window.title("Tkinter window")
window.geometry("2000x1200")
label = tk.Label(window, text="Tag with George v0.1.0")
#shape_name = tk.Canvas(app_name, width=__, height=__, bg= "lowercase")
background = tk.Canvas(window, width=2000, height=1200, bg="green")
x0 = 1740
y0 = 590
x1 = 1760
y1 = 610
player1 = tk.Canvas.create_oval(background, x0, y0, x1, y1, outline="red", fill="red", width=15)

STEP = 10

def move_circle(event):
    """Moves the circle based on the arrow key pressed."""
    if event.keysym == "Up":
        background.move(player1, 0, -STEP)
    elif event.keysym == "Down":
        background.move(player1, 0, STEP)
    elif event.keysym == "Left":
        background.move(player1, -STEP, 0)
        background.update_idletasks()
    elif event.keysym == "Right":
        background.move(player1, STEP, 0)

window.bind('<Up>', move_circle)
window.bind('<Down>', move_circle)
window.bind('<Left>', move_circle)
window.bind('<Right>', move_circle)
window.bind('<w>', move_circle)
window.bind('<a>', move_circle)
window.bind('<s>', move_circle)
window.bind('<d>', move_circle)

background.focus_set()
label.pack()
background.pack()
window.mainloop()

# 350, 200 out of 400x400
# 1750, 600
# 1740, 590
# 1760, 610


# Old key handling code:

# def move_square(event):
#     if event.key == "ArrowLeft":
#         player1.move(-10, 0)
#     if event.key == "ArrowRight":
#         player1.move(10,0)
#     if event.key == "ArrowUp":
#         player1.move(0, -10)
#     if event.key == "ArrowDown":
#         player1.move(0,10)

# Circle Geometry Rubric ~
#       pygame.draw.circle(surface, color, (center x, center y), radius, width)

# player1 geometry:
# pygame.draw.circle(screen, WHITE, (player1_x, player1_y), 10, 1)

# Old key handling code below:

#       add_key_down_handler(move_square)

# New keyboard handing code:

# with keyboard.Listener(on_press=move_square) as listener:
#    listener.join()


# def move_copter(event):
#     if event.key == "a":
#       player2.move(-10, 0)
#    if event.key == "d":3
#    player2.move(10, 0)
#    if event.key == "w":
#        player2.move(0, -10)
#    if event.key == "s":
#        player2.move(0, 10)


