c  = 0
a = 1
b = 3
m = 10
cnt = 12

Xp = c
print(Xp, end=' ')
while cnt:
  Xi = (a * Xp + b) % m
  print(Xi, end=' ')
  if Xi == Xp:
    break
  Xp = Xi
  cnt -= 1