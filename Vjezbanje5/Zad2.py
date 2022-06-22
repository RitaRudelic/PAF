import harmonic_oscillator as har


h1=har.HarmonicOscillator()
h1.set_initial_conditions(10, 5, 2, 5, 20, 0.1)
h1.period(0.1,5)
h1.reset()

h1=har.HarmonicOscillator()
h1.set_initial_conditions(10, 5, 2, 5, 20, 0.1)
h1.period(0.01,5)
h1.reset()

h1=har.HarmonicOscillator()
h1.set_initial_conditions(10, 5, 2, 5, 20, 0.1)
h1.period(0.001,5)

h1.T_analiticki()