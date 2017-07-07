import pygame
import time

game_hero = Actor("mbros")
game_hero.pos = 400, 500
game_bad = Actor("alien")
game_bad.pos = 200, 500

WIDTH = 1000
HEIGHT = game_hero.height + 500

def draw():
    screen.clear()
    game_hero.draw()
    game_bad.draw()
    screen.draw.text("Text", (400, 500), color="blue")

def update():
    game_hero.left += 2
    if game_hero.left > WIDTH:
        game_hero.right = 0
    game_bad.left += 1
    if game_bad.left > WIDTH:
        game_bad.right = 0

def on_mouse_down(pos):
    if game_hero.collidepoint(pos):
        screen.draw.text("Ekk!", (400, 500), color="blue")
        game_hero.image = "pi"
    else:
        screen.draw.text("You missed me!", (400, 800), color="blue")
        time.sleep(0.5)
        game_hero.image = "mbros"
        sounds.eep.play()

def on_mouse_up(pos):
    if game_bad.collidepoint(pos):
        print("Ahh!")
        game_bad.image = "mbros"
    else:
        print("Missed!")
        game_bad.image = "alien"
