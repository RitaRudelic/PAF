import math
import matplotlib.pyplot as plt

from Zad1 import BJ

Bungee = BJ(100, 10, 0, 200, 50, False)
Bungee.jump(50)

fig = plt.subplot()

plt.subplot(4, 4, 2)
plt.plot(Bungee.t1, Bungee.h1)

plt.subplot(2,2,2)
plt.plot(Bungee.t1, Bungee.E1)
plt.plot(Bungee.t1, Bungee.K1)
plt.plot(Bungee.t1, Bungee.U1)
plt.plot(Bungee.t1, Bungee.Ee1)

Bungee.reset()

Bungee = BJ(100, 10, 0, 200, 50, True)    
Bungee.jump(50)

plt.subplot(3, 3, 5)
plt.plot(Bungee.t1, Bungee.h1)

plt.subplot(2,2,4)
plt.plot(Bungee.t1, Bungee.E1)
plt.plot(Bungee.t1, Bungee.K1)
plt.plot(Bungee.t1, Bungee.U1)
plt.plot(Bungee.t1, Bungee.Ee1)

plt.show()