import Projectile as Pr
import matplotlib.pyplot as plt

p1 = Pr.Projectile(10, 50, 0.15, 0, 1, 0.035, 0.1, 0.13, 1, 0)
p1.plot_k_k()

p2 = Pr.Projectile(10, 50, 0.15, 0, 1, 0.035, 0.1, 0.13, 0, 1)
p2.plot_k_k()

plt.legend()
plt.show()

p1.reset()
p2.reset()


