import random
import time
import pygame
import pynput
from pygame import *
from pynput import keyboard

# Stuff to figure out later...

# my_music = html.AUDIO(src="https://codehs.com/uploads/8179d3793582c02c44438d0160d6f0a5")
# my_music.loop = True
# my_music.play()



pygame.init()


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tag with George v0.1.0")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

screen.fill(WHITE)

# (surface, color, (x, y, width, height))
pygame.draw.rect(screen, green, (0, 0, 1000, 1000))

# "pygame.display.flip()" updates screen
# "pygame.quit()" exits window

player1_x = 350
player1_y =  200


# New key handling code:

def move_square(key):
    try:
        if key == keyboard.Key.left:
            global player1_x
            player1_x = player1_x - 10
            global player1_y
            player1_y = player1_y + 0
        elif key == keyboard.Key.right:
            global player1_x
            player1_x = player1_x + 10
            global player1_y
            player1_y = player1_y + 0
        elif key == keyboard.Key.up:
            global player1_x
            player1_x = player1_x + 0
            global player1_y
            player1_y = player1_y - 10
        elif key == keyboard.Key.down:
            global player1_x
            player1_x = player1_x + 0
            global player1_y
            player1_y = player1_y + 10

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
pygame.draw.circle(screen, WHITE, (player1_x, player1_y), 10, 1)

# Old key handling code below:

#       add_key_down_handler(move_square)

# New keyboard handing code:

with keyboard.Listener(on_press=move_square) as listener:
    listener.join()







def move_copter(event):
    if event.key == "a":
        player2.move(-10, 0)
    if event.key == "d":
        player2.move(10,0)
    if event.key == "w":
        player2.move(0, -10)
    if event.key == "s":
        player2.move(0,10)




player2 = Circle(10)
player2.set_position(50, 200)
player2.set_color(Color.white)
add(player2)

add_key_down_handler(move_copter)
#fencing around the map in the program.
rect = Rectangle(500, 10)
rect.set_position(0, 470)
rect.set_color("#573c21")
add(rect)
rec = Rectangle(10, 500)
rec.set_position(390, 0)
rec.set_color("#573c21")
add(rec)
rectd = Rectangle(10, 500)
rectd.set_position(0, 0)
rectd.set_color("#573c21")
add(rectd)
recte = Rectangle(500, 10)
recte.set_position(0, 0)
recte.set_color("#573c21")
add(recte)
#bushes and bush generation.
def bush(x, y):
    r = x - 5
    R = x - 15
    F = x - 30
    t = y - 5
    circ = Circle(15)
    circ.set_position(R, t)
    circ.set_color(Color.red)
    add(circ)
    circ1 = Circle(10)
    circ1.set_position(x, y)
    circ1.set_color(Color.red)
    add(circ1)
    rect = Rectangle(40, 10)
    rect.set_position(F, y)
    rect.set_color(Color.blue)
    add(rect)
    circ.set_color('#0e6101')
    circ1.set_color('#0e6101')
    rect.set_color('#0e6101')
#checks the collision on the player and the fence.
def block(player):
    fence1 = rect.get_x()
    fence2 = rec.get_y() 
    fence3 = recd.get_y()
    fence4 = rece.get_x()
def collision_checker():
    fencex = player1.get_x()
    fencey = player1.get_y() 
    player1set = player1.get_x()
    player1place = player1.get_y()
    player2set = player2.get_x()
    player2place = player2.get_y()
    if player2place == player1place:
        if player2set == player1set:
            block(player)
for i in range (10):
    random_gen_x = random.randint(50, 350)
    random_gen_y = random.randint(50, 500)
    bush(random_gen_x, random_gen_y)
def end_game():
    rect = Rectangle(1000, 1000)
    rect.set_position(0, 0)
    rect.set_color(Color.black)
    txt = Text("J")
    txt.set_position(150, 250)
    txt.set_color(Color.white)
    txt.set_font("70pt wingdings")
    add(rect)
    add(txt)
    txt2 = Text("The tagger won.")
    txt2.set_position(155, 270)
    txt2.set_color(Color.white)
    txt2.set_font("10pt cursive")
    add(txt2)
    
def ending():
    rect = Rectangle(1000, 1000)
    rect.set_position(0, 0)
    rect.set_color(Color.black)
    txt = Text("J")
    txt.set_position(150, 250)
    txt.set_color(Color.white)
    txt.set_font("70pt wingdings")
    add(rect)
    add(txt)
    txt2 = Text("The tagger won.")
    txt2.set_position(155, 270)
    txt2.set_color(Color.white)
    txt2.set_font("10pt cursive")
    add(txt2)
def ef():
    player1set = player1.get_x()
    player1place = player1.get_y() 
    player2set = player2.get_x()
    player2place = player2.get_y()
    if player2place == player1place:
        if player2set == player1set:
            end_game()
timer = timer.set_interval(ef, 10)
random_num = random.randint(1, 2)
if random_num == 1:
    player1.set_color(Color.red)
    player2.set_color(Color.white)
if random_num == 2:
    player2.set_color(Color.red)
    player1.set_color(Color.white)