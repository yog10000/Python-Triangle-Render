import pygame,  sys

pygame.init()
screen = pygame.display.set_mode((600, 400))

def px(x, y):
  y = (-1 * y) + 400
  screen.set_at((int(x), int(y)), (0, 0, 0))
  

def triangle(p1, p2, p3):
   m1 = (p2[1]-p1[1])/(p2[0]-p1[0])
   m2 = (p3[1]-p2[1])/(p3[0]-p2[0])
   m3 = (p1[1]-p3[1])/(p1[0]-p3[0])
   
   b1 = p1[1] - m1 * p1[0]
   b2 = p2[1] - m2 * p2[0]
   b3 = p3[1] - m3 * p3[0]
   
   max_x1 = max(p1[0], p2[0])
   max_x2 = max(p2[0], p3[0])
   max_x3 = max(p3[0], p1[0])
   
   min_x1 = min(p1[0], p2[0])
   min_x2 = min(p3[0], p2[0])
   min_x3 = min(p1[0], p3[0])
   
   for x in range(min_x1, max_x1+1):
     y1 = m1*x+b1
     px(x,y1)
   for x in range(min_x2, max_x2+1):
     y2 = m2*x+b2
     px(x,y2)
   for x in range(min_x3, max_x3+1):
     y3 = m3*x+b3
     px(x,y3)
   
   

while True:
  screen.fill((255, 255, 255))
  triangle((50, 150), (200, 50), (300, 250))
  pygame.display.flip()
