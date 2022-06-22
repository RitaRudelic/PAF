import Zadatak1 as part

def funkcija_1(x, v, t):
    
    f = 150
    return f

def funkcija_2(x, v, t):
    
    k = 20
    f = -k*x
    return f 

p1 = part.particle(5, 1, 5, funkcija_1)
p1.plot_trajectory(0.02,6)

p2 = part.particle(5, 1, 5, funkcija_2)
p2.plot_trajectory(0.02,6)