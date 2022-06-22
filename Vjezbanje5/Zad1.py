import matplotlib.pyplot as plt
import harmonic_oscillator as har
import numpy as np

h1=har.HarmonicOscillator()
h1.set_initial_conditions(10, 5, 2, 5, 20, 0.1)
h1.preciznost(0.01)
h1.reset()

h1=har.HarmonicOscillator()
h1.set_initial_conditions(10, 5, 2, 5, 20, 0.1)
h1.preciznost(0.04)
h1.reset()

h1=har.HarmonicOscillator()
h1.set_initial_conditions(10, 5, 2, 5, 20, 0.1)
h1.preciznost(0.1)
h1.reset()

h1=har.HarmonicOscillator()
h1.set_initial_conditions(10, 5, 2, 5, 20, 0.1)
x,t= h1.analiticki(0.01, 20)
plt.plot(t,x)
plt.show()
h1.reset()
