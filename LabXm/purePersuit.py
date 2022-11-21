import numpy as np
import random
import matplotlib.pyplot as plt

vf = 20
t = 0
flag = 1

caughtAt = 100
escappedAt = 900

xf = random.randint(0,1000)
yf = random.randint(0,1000)

bomber_x = []
bomber_y = []
fighter_x = []
fighter_y = []
fighter_x.append(xf)
fighter_y.append(yf)

while(flag):
  xb = random.randint(0, 1000)
  yb = random.randint(0, 1000)
  
  bomber_x.append(xb)
  bomber_y.append(yb)
  dist = np.sqrt((xf - xb)**2 + (yf - yb)**2)
  
  if dist <= caughtAt:
    print('Target caught')
    print('step = {}'.format(t))
    flag = 0
  elif dist >= escappedAt:
    flag = 0
    print('Escapped')
    print('step = {}' .format(t))
  else:
    sin = (yb - yf) / dist
    cos = (xb - xf) / dist
    xf = xf + vf*cos
    yf = yf + vf*sin
    t += 1
  fighter_x.append(xf)
  fighter_y.append(yf)
plt.plot(fighter_x,fighter_y,'r*')
plt.plot(bomber_x,bomber_y,'b*')
plt.show()
