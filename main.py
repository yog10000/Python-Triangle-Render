import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 400))

def px(x, y):
  y = (-1 * y) + 400
  screen.set_at((int(x), int(y)), (0, 0, 0))
  

def triangle(p1, p2, p3):
  pass


#set points

triangle((50, 150), (200, 50), (300, 250))


while True:
    screen.fill((255, 255, 255))
    
    pygame.display.flip()