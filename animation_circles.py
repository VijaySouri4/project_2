import pygame
import environment
import math
import sys

env_size = 10
environment1 = environment.Env(env_size)
node_cords = []

for i in range(env_size):
    con = 360/env_size * i
    x_pos = (1*math.cos(math.radians(con)))
    y_pos = (1*math.sin(math.radians(con)))
    node_cords.append((x_pos,y_pos))

# constants 
display_width = 1000
display_height = 900
radius = 5 # node size

def run():
  pygame.init()

  screen = pygame.display.set_mode((display_width, display_height))
  clock = pygame.time.Clock()

  screen.fill((0,0,0)) # param is color tuple

  # loop to draw cicle at each node center
  for centerxy in node_cords:
    pygame.draw.circle(screen, # draw need buffer
      (255,255,200), # color of circle
      centerxy, radius) # default is filled circle
    pygame.draw.circle(screen, 
      (0,150,150), centerxy, radius-4)

  pygame.display.update() # copy screen to display

  while 1:  
    clock.tick(5)

def main():
    run()

if __name__ == '__main__':
    main()