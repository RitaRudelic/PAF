import projectiledrop as pro
import matplotlib.pyplot as plt

avion1 = pro.pojectiledrop(2000, 200)
x, y, vx, vy, t = avion1.gibanje(0.01)

plt.figure(figsize=(12,5))

plt.subplot(1, 2, 1)
plt.plot(x, y)


plt.subplot(1, 2, 2)
plt.plot(t, vy)

plt.tight_layout()
plt.show()