import projectiledrop as pro
import matplotlib.pyplot as plt
import numpy as np

avion1 = pro.pojectiledrop(2000, 200)

delta_t = np.linspace(0.001, 0.1, 100)
vrijeme = []

for i in delta_t:
    vrijeme.append(avion1.vrijeme_padanja(i))

plt.scatter(delta_t, vrijeme, s=5)

plt.show()