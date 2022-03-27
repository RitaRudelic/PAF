import matplotlib.pyplot as plt
import math
import numpy as np

class particle:
   
    def __init__(self):
        self.g = -9.81
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
       
    def set_initial_conditions(self, v0, theta, x0, y0, dt):
        self.vx += [v0*np.cos(np.radians(theta))]
        self.vy += [v0*np.sin(np.radians(theta))]
        self.theta = theta
        self.x += [x0]
        self.y += [y0]
        self.v0=v0
        self.dt=dt
   
    def reset(self):
        self.vx = []
        self.vy = []
        
        self.x = []
        self.y = []

    def __move(self):
        self.vx += [self.vx[len(self.vx)-1]]
        self.vy += [self.vy[len(self.vy)-1]+self.g*self.dt]
       
        self.x += [self.x[len(self.x)-1]+self.vx[len(self.vx)-1]*self.dt]
        self.y += [self.y[len(self.y)-1]+self.vy[len(self.vy)-1]*self.dt]

    def range(self):
        while(self.y[-1]>=0):
            self.__move()
        return(self.x[-1])

   
    def plot_trajectory(self):
        plt.figure("Graf za trenutno stanje")
        plt.plot(self.x,self.y)
        plt.title("x-y graf")
        plt.xlabel("x[m]")
        plt.ylabel("y[m]")
        plt.show()

    def analiticki_domet(self):
        D = ((self.v0**2)*math.sin(2*np.radians(self.theta)))/9.81
        return D
