import Projectile as Pr 
import matplotlib.pyplot as plt

p1 = Pr.Projectile(25, 10, 0.1, 0, 1, 0.005, 0.1, 0.11, 1, 0)
print(p1.plot_target(13, 3, 1))
p1.reset()

p1 = Pr.Projectile(25, 10, 0.1, 0, 1, 0.05, 0.1, 0.11, 1, 0)
print(p1.plot_target(0, 25, 13))
p1.reset()

p1 = Pr.Projectile(25, 10, 0.1, 0, 1, 0.05, 0.1, 0.11, 1, 0)
print(p1.plot_target(13,23,2))
p1.reset()

p1 = Pr.Projectile(25, 10, 0.1, 0 , 1, 0.05, 0.1, 0.11, 1, 0)
print(p1.plot_target(-13, 10, 1.3))
p1.reset()