import matplotlib.pyplot as plt
import numpy as np 
import math

#Mmodul za kosi hitac

def crtaj_graf(v0, theta, dt= 0.1): #funkcija koja crtan putanju, ali zaustavlja gibanje kad projektiludari na tlo (y=0)
    x = [0]
    y = [0]
    vx = [v0*np.cos((theta/180)*np.pi)]
    vy = [v0*np.sin(theta/180)*np.pi]
    ax = [0]
    ay = [9,81]
    t = [0]

    for i in range(int(10/dt)):
        t.append(i*dt)
        ax.append(0)
        ay.append(9.81)
        vx.append(vx[i]+ax[i]*dt)
        vy.append(vy[i]+ay[i]*dt)
        x.append(x[i]+ vx[i]*dt) 
        y.append(y[i]+ vy[i]*dt)
        if y == 0:
            x.append(x[i]+ vx[i]*dt) 
            y.append(y[i]+ vy[i]*dt)
    
    plt.figure("Graf")
    plt.plot(x,y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("x-y graf")
    plt.show() 


def maksimalna_visina(v0,theta,dt=0.1): #maksimalna visina tijela
    y = [0]
    vy = [v0*np.sin(theta/180)*np.pi]
    ay = [9,81]
    t = [0]
    theta = [(theta/180)*np.pi]

    for i in range(int(10/dt)):
        t.append = (dt)
        vy.append = (vy[i]+ay[i]*dt)
        y.append(y[i]+ vy[i]*dt)
        if y >= 0:
            y.append(y[i]+ vy[i]*dt)

    h = max(y)
    print(f"Maksimalna visina koju tijelo postigne je: {h}m.")


def domet(v0,theta,dt=0.1): #domet tijela
    x = [0]
    y = [0]
    t = [0]
    ay = 9.81
    theta = [(theta/180)*np.pi]
    vx = [v0*np.cos((theta/180)*np.pi)]
    vy = [v0*np.sin(theta/180)*np.pi]

    for i in range(int(10/dt)):
        t.append = (i*dt)
        vy.append = (vy[i]+ay[i]*dt)
        x.append = (x[i]+ vx[i]*dt) 
        y.append = (y[i]+ vy[i]*dt)
        yi = yi + vy*dt
        if y >= 0:
            y.append = (y[i]+ vy[i]*dt)
            
    domet = max(x)
    print(f"Domet iznosi: {domet}m.") 


def maksimalna_brzina(v0,theta,dt=0.1): #maksimalna brzina tijela tijekom gibanja
    v = [0]
    t = [0]
    y =[0]
    ay = 9.81
    theta = [(theta/180)*np.pi]
    vx = [v0*np.cos((theta/180)*np.pi)]
    vy = [v0*np.sin(theta/180)*np.pi]

    vi = math.sqrt((vx**2) + (vy**2))
    v.append(vi)

    for i in range(int(10/dt)):
        t.append = (i*dt)
        vy.append = (vy[i]+ay[i]*dt)
        y.append = (y[i]+ vy[i]*dt)
        if y >= 0:
            vi = math.sqrt((vx**2)+(vy**2))
            v.append(vi)

    vmax = max(v)
    print(f"Maksimalna brzina iznosi: {vmax}m/s")


def provjera_mete(v0,theta,dt,sx,sy,r):
    x = [0]
    y = [0]
    d = []
    xm = []
    ym = []
    t = [0]
    ay = 9.81
    theta = [(theta/180)*np.pi]
    vx = [v0*np.cos((theta/180)*np.pi)]
    vy = [v0*np.sin(theta/180)*np.pi]
    d_meta = math.sqrt(sx**2 + sy**2)

    pogodena = False
    
    for i in range(int(10/dt)):
        t.append = (i*dt)
        x.append = (x[i]+ vx[i]*dt)
        vy.append = (vy[i]+ay[i]*dt)
        y.append = (y[i]+ vy[i]*dt)
        if y < 0:
            break
        x.append()
        y.append()
        d_tm = math.sqrt((sx-x)**2 + (sy-y)**2)
        if d_tm <= r:
            pogodena = True
            break
        else:
            d.append(d_tm)

            
    if pogodena:
        print("Projektil je pogodio metu.")
    else:
        d_min = min(d)
        print("Projektil ne pogodi metu.")
        print(f"Najmanja udaljenost projektila od mete: {d_min}m")

    for fi in range(3600):
        xmi = sx + r*math.cos(fi)
        ymi = sy + r*math.sin(fi)
        xm.append(xmi)
        ym.append(ymi)

    plt.figure("Putanja i meta")
    plt.plot(x,y)
    plt.plot(xm,ym)
    plt.show()