import numpy as np
import math
import matplotlib.pyplot as plt

class Planet:
    
    def __init__(self, x):
        
        self.brzina = (x["brzina"])
        self.masa = (x["masa"])
        self.polozaj = (x["polozaj"])
        self.velicina = (x["velicina"])
        self.ime = (x["ime"])
        self.boja = (x["boja"])
        
        self.pomaci = [self.polozaj]
        
        self.akc = np.array([0, 0])

class Solar_Sistem:
    
    def __init__(self, x, y, z = 0, j = 0, k = 0):
        
        lista = [x, y, z, j, k]
        self.planeti = []
        
        self.dt = 60 * 6 * 24
        self.G =  6.67428 * (10**(-11))
        self.t = 365 * 24 * 3600
        self.dt = 3600
        
        for i in range (5):
            
            try:
                p = Planet(lista[i])
                self.planeti.append(p)
            
            except:
                
                continue
    
    def reset(self):
        
        del self.planeti

    def akc(self):
        
        for x in self.planeti:
            for y in self.planeti:
                if y != x and y !=0 and x != 0:
                    akc = -self.G * (y.masa * (np.subtract(x.polozaj, y.polozaj))/ np.linalg.norm(abs(np.subtract(x.polozaj,y.polozaj)))**3)
                    x.akc = np.add(akc,x.akc)
        
    def evolve(self):
        
        t = 0
        
        while t < self.t:
            
            self.akc()
            
            for i in range (len(self.planeti)):
                x = self.planeti[i]
                x.brzina1 = np.add(x.brzina, x.akc * self.dt)
                x.polozaj = np.add(x.polozaj , x.brzina1 * self.dt)
                x.pomaci.append(x.polozaj)
            
            t = t + self.dt

    def plot(self):
        
        self.evolve()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        
        for x in self.planeti:
            x_list = []
            y_list = []
            
            for i in range (len(x.pomaci)):
                
                x_list.append(x.pomaci[i][0])
                y_list.append(x.pomaci[i][1])
            
            ax.scatter(x_list[-1], y_list[-1], s = x.velicina , c = x.boja , label = x.ime)
            ax.plot(x_list, y_list, c = x.boja)
        
        plt.show()   