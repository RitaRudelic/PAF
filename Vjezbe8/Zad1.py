import Projectile as Pr 
import matplotlib.pyplot as plt

p1 = Pr.Projectile(10, 50, 0.12, 0, 1, 0.035, 0.1)
p1.gibanje()
p1.plot()
p1.reset()

p2 = Pr.Projectile(10, 50, 0.12, 0, 1, 0.035, 0.1)
p2.Runge_Kutta()
p2.plot()
p2.reset()


