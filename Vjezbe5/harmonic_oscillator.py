
import matplotlib.pyplot as plt
import numpy as np
import math

class HarmonicOscillator:
    
    def __init__(self):
        self.a = []
        self.v = []
        self.x = []
        self.t = []
        
    def reset(self):
        self.__init__()
        
    def set_initial_conditions(self, x0, v0, k, m, vrijeme, dt):
        self.a.append((-k/m)*x0)
        self.v.append(v0)
        self.x.append(x0)
        self.t.append(0)
        self.dt = dt
        self.vrijeme = vrijeme
        self.k = k
        self.m = m
    
    def __move(self):
        self.a.append((-self.k/self.m)*self.x[-1])
        self.v.append(self.v[-1]+self.a[-1]*self.dt)
        self.x.append(self.x[-1]+self.v[-1]*self.dt)
        self.t.append(self.t[-1]+self.dt)
      
    def gibanje(self):
        for i in range(int(self.vrijeme/self.dt)):
            self.__move()
            
    def plot_trajectory(self):
        self.t.pop(0)
        for i in self.t:
            self.__move()
        self.t.insert(0,0)

        plt.figure(figsize=(12,6))
        
        plt.subplot(5,3,3)
        plt.scatter(self.t, self.x, s=2)
       
        plt.subplot(5,2,4)
        plt.scatter(self.t, self.v, s=2)
        
        plt.subplot(5,3,5)
        plt.scatter(self.t, self.a, s=2)
        
        plt.tight_layout()
        plt.show()

    def preciznost(self,dt,t=20):
        self.dt = dt
        self.vrijeme = t
        self.gibanje()
        plt.scatter(self.t,self.x)
        plt.title('x-t graf')

    def analiticki(self,dt,t1=2):
        self.omega = math.sqrt(self.k/self.m)
        A = np.sqrt(self.x[0]**2+(self.v[0]/self.omega)**2)
        fi = np.arctan(-self.v[0]/self.omega/self.x[0])
        
        while self.t[-1]<=t1:
            self.x.append(A*math.cos(self.omega*self.t[-1]+fi))
            self.t.append(self.t[-1]+dt)
        
        return self.x,self.t

    def period(self,dt,t):
        self.dt = dt
        A = self.x
        T = 0
        self.gibanje()
        for x in self.x:
                if x*self.x[0] < 0:
                    T += dt
                elif T!= 0:
                    break
        print(2*T)

    def T_analiticki(self):
        T = 2*math.pi*math.sqrt(self.m/self.k)
        print(T)