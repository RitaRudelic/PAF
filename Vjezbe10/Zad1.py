import numpy as np
import modul as em
import matplotlib.pyplot as plt

p = em.polje(0.4, 0, 0, 0, 1, np.array([0.1, 0.1, 0.1]), np.array([0, 0, 1]), np.array([0, 0, 0]))
p.zad1()
p.reset()