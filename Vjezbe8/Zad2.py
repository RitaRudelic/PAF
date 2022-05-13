import Projectile as Pr
import matplotlib.pyplot as plt

p1 = Pr.Projectile(10, 50, 0.12, 0, 1, 0.035, 0.1)
p1.gibanje()
plt.plot(p1.list_x, p1.list_y)
p1.back()
p1.Runge_Kutta()
plt.plot(p1.list_x, p1.list_y)
plt.show()
p1.reset()