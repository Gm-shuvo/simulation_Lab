import pygame

pygame.init()
pygame.display.set_caption("Bezier Curve")
screenSize = (1000, 600)
screen = pygame.display.set_mode(screenSize)

f = pygame.font.get_fonts()[0]
font = pygame.font.SysFont(f, 32)

position_text1 = font.render("p0",True,(255,255,255),(0,0,0))
position_text2 = font.render("p1", True, (255, 255, 255), (0, 0, 0))
position_text3 = font.render("p2", True, (255, 255, 255), (0, 0, 0))
position_text4 = font.render("p3", True, (255, 255, 255), (0, 0, 0))

txt1_rect = position_text1.get_rect()
txt2_rect = position_text2.get_rect()
txt3_rect = position_text3.get_rect()
txt4_rect = position_text4.get_rect()

P0 = (100.0, 500.0)
P1 = (200.0, 100.0)
P2 = (600.0, 80.0)
P3 = (650.0, 410.0)

txt1_rect.center = P0
txt2_rect.center = P1
txt3_rect.center = P2
txt4_rect.center = P3

screen.blit(position_text1, txt1_rect)
screen.blit(position_text2, txt2_rect)
screen.blit(position_text3, txt3_rect)
screen.blit(position_text4, txt4_rect)

pygame.draw.line(screen, (0,255,0), P0, P1,1)
pygame.draw.line(screen, (255,0,255), P2,P3,1)

running = True
speed = 0.0004
t = 0
while running:
  while t < 1:
    t += speed
    
    BZ0 = (pow((1 - t),3)* P0[0]), (pow((1-t),3)*P0[1])
    BZ1 = (3 * t * pow((1 - t), 2) * P1[0]), (3 * t * pow((1-t), 2)* P1[1])
    BZ2 = (3 * t * t * (1 - t) * P2[0]), (3 * t * t * (1 - t) * P2[1])
    BZ3 = (pow(t,3)*P3[0]), (pow(t,3)*P3[1])
    
    p = (BZ0[0] + BZ1[0] + BZ2[0] + BZ3[0]) , (BZ0[1] + BZ1[1] + BZ2[1] + BZ3[1])
    
    x,y = round(p[0]),round(p[1])
    
    pygame.draw.circle(screen, (55,170,200),(x,y),2)
    
    pygame.display.flip()
  running = False
pygame.time.delay(5000)
pygame.QUIT()



