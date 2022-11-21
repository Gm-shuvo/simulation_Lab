import matplotlib.pyplot as plt


a0 = 100
b0 = 50
c0 = 0
del_t = 0.1
t = 0
A = [a0]
B = [b0]
C = [c0]
YD = [del_t]
k1 = 0.002
k2 = 0.008
T = 5

print("\tTime\t \tA(i)\t \tB(i)\t \tC(i)\t")
print("%12.2f %16.2f %15.2f %15.2f" % (t, a0, b0, c0))

t += del_t

while t < T:
  ai = a0 + (k1 * c0 - k2 * a0 * b0) * del_t
  bi = b0 + (k1 * c0 - k2 * a0 * b0) * del_t
  ci = c0 + (2 * k2 * a0 * b0 - 2 * k1 * c0) * del_t
  A.append(ai);B.append(bi);C.append(ci);YD.append(t)
  a0 = ai
  b0 = bi
  c0 = ci
  
  print("%12.2f %16.2f %15.2f %15.2f" % (t, a0, b0, c0))

  t += del_t


plt.plot(YD,A,color = 'red',label = 'a' )
plt.plot(YD,B,color = 'green',label = 'b' )
plt.plot(YD,C,color = 'yellow',label = 'c' )

plt.show()