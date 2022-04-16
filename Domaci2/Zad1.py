import matplotlib.pyplot as plt

class particle:
    
    def __init__(self, m, x0, v0, funkcija):
        
        self.x1 = []
        self.v1 = []
        self.a1 = []
        self.t1 = []
        
        self.m = m
        self.x = x0
        self.v = v0
        self.f = funkcija
        self.t = 0
        self.a = self.f(self.x,self.v,self.t)/self.m
       
        self.x1.append(self.x)
        self.v1.append(self.v)
        self.a1.append(self.a)
        self.t1.append(self.t)
    
    def move(self,dt,t):
            
            n = int(t/dt)
            for i in range(n):
                
                self.a = self.f(self.x, self.v, self.t)/self.m
                self.v = self.v + self.a*dt
                self.x = self.x + self.v*dt
                self.t += dt
                
                self.x1.append(self.x)
                self.v1.append(self.v)
                self.a1.append(self.a)
                self.t1.append(self.t)
            
            return self.x1, self.v1, self.a1, self.t1
    
    def plot_trajectory(self,dt,t):
        
        x,v,a,t = self.move(dt,t)
        
        plt.subplot(2,4,2)
        plt.plot(t,x)
        
        plt.subplot(2,4,3)
        plt.plot(t,v)
        
        plt.subplot(2,5,5)
        plt.plot(t,a)
        
        plt.show()
    
    def reset(self):
        
        del self.k
        del self.m
        del self.x
        del self.v
        del self.a
        del self.t
        del self.x1
        del self.v1
        del self.a1
        del self.t1