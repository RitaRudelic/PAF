import particle as prt
import matplotlib.pyplot as plt
import math

#Objekt za zadatak 1

p1 = prt.particle()

p1.set_initial_conditions(30,15,10,10, 0.01)
print("Domet je {:.2f}m.".format(p1.range()))
p1.plot_trajectory()
p1.reset()

p1.set_initial_conditions(20,60,0,0, 0.01)
print("Domet je {:.2f}m.".format(p1.range()))
p1.plot_trajectory()
p1.reset()  