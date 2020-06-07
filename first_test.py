import pgzrun
# import pygame

WIDTH=700
HEIGHT=490

map_data=[[1,0,1,0,0,0,0,0,0,0],
          [1,0,1,1,1,0,1,1,1,0],
          [1,0,0,0,0,0,0,0,0,0],
          [1,1,0,1,1,1,1,1,1,0],
          [0,0,0,1,0,0,0,1,1,0],
          [0,1,1,1,0,1,0,0,0,1],
          [0,0,0,0,0,1,0,1,0,0]]

box = Actor('box',topleft=(0,0))
floor = Actor('floor',topleft=(0,0))
# floor=pygame.image.load("./images/floor.png")
hero = Actor('player',topleft=(70,0))
# hero=pygame.image.load("./images/player.png")

def draw():
    screen.clear()
    for y in range(7):
        for x in range(10):
            floor.topleft=(70*x,70*y)
            floor.draw()
            # if map_data[x][y]==1:
            #     # box.topleft=(70*x,70*y)
            #     # box.draw()
            #     pass
    # floor.draw()
    box.draw()
    hero.draw()
# def update():
#     hero.x+=1

pgzrun.go()
