import pygame
import random
import numpy as np

pygame.init()

pygame.display.set_caption("Persuit Curve")
screen = pygame.display.set_mode((1400, 1000))


f = pygame.font.get_fonts()[0]
font = pygame.font.SysFont(f, 32)

position_text1 = font.render('Bomber Caught',True, (255,255,255), (0, 0, 0))

position_text2 = font.render('Bomber Escapped', True, (255, 255, 255), (0, 0, 0))

textRect1 = position_text1.get_rect()
textRect2 = position_text2.get_rect()

path_position = [(500.0, 500.0), (500.0, 500.0)]
P0 = path_position[0]
P1 = path_position[1]

textRect1.center = P0
textRect2.center = P1

vf = 20
t = 0
flag = 1

fighter_x = []
fighter_y = []
bomber_x = []
bomber_y = []

xf = random.randint(0, 1000)
yf = random.randint(0, 1000)
xb = random.randint(0, 1000)
yb = random.randint(0, 1000)

fighter_x.append(xf)
fighter_y.append(yf)

prev_F = (float(xf), float(yf))
prev_B = (float(), float())

screen.fill((0, 0, 0))
pygame.time.delay(50)

while(flag):
  xb = random.randint(0, 1000)
  yb = random.randint(0, 1000)
  
  bomber_x.append(xb)
  bomber_y.append(yb)
  
  dist = np.sqrt((xb - xf)**2 + (yb - yf)**2)
  
  if(dist <= 100):
    print('Target Cought')
    print('steps = {}'.format(t))
    flag = 0
    screen.blit(position_text1, textRect1)
    
    pres_F = (float(xf), float(yf))
    pres_B = (float(xb), float(yb))
    
    pygame.draw.line(screen,(255, 0, 0), pres_B, pres_F, 5)
    
  elif dist >= 900:
    print('Target Escapped')
    print('steps = {}'.format(t))
    flag = 0
    screen.blit(position_text2, textRect2)
  else:
    sin = (yb - yf)/dist
    cos = (xb - xf)/dist
    xf = xf + vf*cos
    yf = yf + vf*sin
    t += 1
  pres_F = (float(xf), float(yf))
  pres_B = (float(xb), float(yb))
  pygame.draw.line(screen, (55, 20, 150), prev_F,pres_F, 4)
  pygame.draw.line(screen, (200, 20, 150), prev_B, pres_B, 4)
  
  prev_F = pres_F
  prev_B = pres_B
  
  pygame.draw.circle(screen, (55, 20, 150), (round(xf), round(yf)), 4)
  pygame.draw.circle(screen, (200, 20, 150), (round(xb), round(yb)),4)
  pygame.time.delay(500)
  pygame.display.flip()
  
pygame.time.delay(5000)
pygame.quit()
  
