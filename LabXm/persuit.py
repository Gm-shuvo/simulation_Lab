import pygame
import random
import numpy as np

pygame.init()
pygame.display.set_caption('persuit')
screen = pygame.display.set_mode((1300, 1000))

f = pygame.font.get_fonts()[0]
font = pygame.font.SysFont(f, 32)

position_txt1 = font.render("Bomber Cought", True, (255,255,255),(0,0,0))
position_txt2 = font.render("Bomber Escapped", True, (255,255,255),(0,0,0))

txt1_rect = position_txt1.get_rect()
txt2_rect = position_txt2.get_rect()

p0 = (500.0, 500.0)
p1 = (500.0, 500.0)

txt1_rect.center = p0
txt2_rect.center = p1

screen.fill((0,0,0))
pygame.time.delay(50)

fighter_x = []
fighter_y = []
bomber_x = []
bomber_y = []
xf = random.randint(1,1000)
yf = random.randint(1, 1000)
prev_f = (float(xf), float(yf))
prev_b = ((float(), float()))

vf = 20
t = 0
flag = 1

while flag:
  xb = random.randint(1, 1000)
  yb = random.randint(1, 1000)
  
  dist = np.sqrt((xb - xf)**2 + (yb - yf)**2)
  
  if dist < 100:
    flag = 0
    print('Bomber Caught')
    print('steps = {}'.format(t))
    pres_f = (float(xf),float(yf))
    pres_b = (float(xb), float(yb))
    screen.blit(position_txt1, txt1_rect)
    pygame.draw.line(screen, (255, 0, 0), pres_f, pres_b, 4)
  elif dist > 900:
    flag = 0
    print('Bomber Escapped')
    print('steps = {}'.format(t))
    screen.blit(position_txt2, txt2_rect)
  else:
    t += 1
    sin = (yb - yf) / dist
    cos = (xb - xf) / dist
    xf = xf + cos * vf
    yf = yf + sin * vf
  pres_f = (float(xf), float(yf))
  pres_b = (float(xb), float(yb))
  pygame.draw.line(screen, (55, 20, 150), prev_f, pres_f, 5)
  pygame.draw.line(screen, (200, 20, 150), prev_b, pres_b, 5)
  prev_f = pres_f
  prev_b = pres_b
  pygame.draw.circle(screen, (55, 20, 150), (round(xf), round(yf)), 4)
  pygame.draw.circle(screen, (200, 20, 150), (round(xf), round(yf)), 4)
  pygame.time.delay(500)
  pygame.display.flip()

pygame.time.delay(5000)
pygame.quit()
