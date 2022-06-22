import matplotlib.pyplot as plt
import numpy as np 

def kosi_hitac(v0, theta, dt= 0.1):
    
    x = [0]
    y = [0]
    vx = [v0*np.cos((theta/180)*np.pi)]
    vy = [v0*np.sin(theta/180)*np.pi]
    ax = [0]
    ay = [-9,81]
    t = [0]

    for i in range(int(10/dt)):
        
        t.append(i*dt)
        ax.append(0)
        ay.append(-9.81)
        vx.append(vx[i]+ax[i]*dt)
        vy.append(vy[i]+ay[i]*dt)
        x.append(x[i]+ vx[i]*dt) 
        y.append(y[i]+ vy[i]*dt)

    plt.figure("grafovi")
    fig = plt.subplot()
    plt.subplot(2,2,1)
    plt.plot(x,y)
    plt.xlabel("x")
    plt.ylabel("y")
   
    plt.subplot(2,2,2)
    plt.plot(t,x)
    plt.xlabel("t")
    plt.ylabel("x")
   
    plt.subplot(2,2,3)
    plt.plot(t,y)
    plt.xlabel("t")
    plt.ylabel("y")
    
    plt.subplots_adjust(wspace = 0.4, hspace = 0.6, bottom = 0.1)
    plt.show()   

kosi_hitac(20, 40)