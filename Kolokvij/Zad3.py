from tkinter import Y
import matplotlib.pyplot as plt
import numpy as np
import math
import ProjectileDrop as pd

o = pd.ProjectileDrop(20, 20)
h, vy, t, x = o.ispustanje_projektila(0.01)

plt.plot(vy, t)
plt.show()

plt.plot(x, h)
plt.show()