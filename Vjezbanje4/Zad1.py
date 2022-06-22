import calculus as cal
import matplotlib.pyplot as plt
import numpy as np

#ako je m=2 koristi se twostep metoda

(x, dfx) = cal.der1(np.sin, 0, 8, 0.01, m=2)
plt.plot(x,dfx, lw= 2, ls="--")
plt.plot(x, np.cos(x))
plt.show()