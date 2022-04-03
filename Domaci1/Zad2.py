import matplotlib.pyplot as plt
import particle as prt

def ovisnost_dometa_o_kutu():
    theta_lista = []
    D_lista = [] 
    
    p1 = prt.particle()

    for theta in range(100):
        p1.set_initial_conditions(10, theta, 0, 0,  0.01)
        D = p1.range()
        theta_lista.append(theta)
        D_lista.append(D)
        p1.reset()

    plt.figure("Graf 1")
    plt.plot(theta_lista,D_lista)
    plt.xlabel("Kut otklona [°]")
    plt.ylabel("Domet [m]")
    plt.title("Ovisnost dometa o pocetnom kutu otklona")
    plt.show()

def ovisnost_vremena_o_kutu():
    theta_lista = []
    t_lista = []

    p1 = prt.particle()

    for theta in range(100):
        p1.set_initial_conditions(10, theta, 0, 0, 0.01)
        t = p1.total_time()
        theta_lista.append(theta)
        t_lista.append(t)
        p1.reset()

    plt.figure("Graf 2")
    plt.plot(theta_lista,t_lista)
    plt.xlabel("Kut otklona [°]")
    plt.ylabel("Vrijeme trajanja [s]")
    plt.title("Ovisnost vremena trajanja o pocetnom kutu otklona")
    plt.show()

def ovisnot_dometa_o_brzini():
    v_lista = []
    D_lista = [] 

    p1 = prt.particle()
    for v in range(100):
        p1.set_initial_conditions(v, 45, 0, 0, 0.01)
        D = p1.range()
        v_lista.append(v)
        D_lista.append(D)
        p1.reset()

    plt.figure("Graf 1")
    plt.plot(v_lista,D_lista)
    plt.xlabel("Iznos pocetne brzine [m/s]")
    plt.ylabel("Domet [m]")
    plt.title("Ovisnost dometa o iznosu pocetne brzine")
    plt.show()

def ovisnost_vremena_o_brzini():
    v_lista = []
    t_lista = []

    p1 = prt.particle()

    for v in range(101):
        p1.set_initial_conditions(v, 45, 0, 0, 0.01)
        t = p1.total_time()
        v_lista.append(v)
        t_lista.append(t)
        p1.reset()

    plt.figure("Graf 2")
    plt.plot(v_lista,t_lista)
    plt.xlabel("Iznos pocetne brzine [m/s]")
    plt.ylabel("Vrijeme trajanja [s]")
    plt.title("Ovisnost vremena trajanja o iznosu pocetne brzine")
    plt.show()

ovisnost_dometa_o_kutu()
ovisnost_vremena_o_kutu()
ovisnot_dometa_o_brzini()
ovisnost_vremena_o_brzini()