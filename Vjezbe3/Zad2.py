import matplotlib.pyplot as plt
import math
import particle as prt

dt_lista = []
aps_greska = []

p1 = prt.particle()

dt = 0.000
for i in range(100):
    dt += 0.001
    p1.set_initial_conditions(10,60,0,0, dt)
    greska = abs(p1.range() - p1.analiticki_domet())/p1.analiticki_domet()*10
    dt_lista.append(dt)
    aps_greska.append(greska)
    p1.reset()

plt.figure("Ovisnost relativne apsolutne pogreske o vremenskom intervalu")
plt.plot(dt_lista,aps_greska)
plt.xlabel("dt[s]")
plt.ylabel("apsolutna pogreska [%]")
plt.show()  