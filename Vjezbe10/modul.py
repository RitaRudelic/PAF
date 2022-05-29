import numpy as np
import matplotlib.pyplot as plt

class polje:
    
    def __init__(self, m, y0, x0, z0, q, v, EM, EE):
        
        self.masa = m
        self.polozaj = np.array([x0, y0, z0])
        self.polozaj0 = np.array([x0, y0, z0])
        
        self.polozaji_x = [x0]
        self.polozaji_y = [y0]
        self.polozaji_z = [z0]
        
        self.q = q
        self.EM = EM
        self.v0 = v
        self.v = v
        self.EE = EE
        
        self.dt = 0.005

    def reset(self):
        
        del self.polozaj
        del self.masa
        del self.polozaj0
        
        del self.polozaji_x
        del self.polozaji_y
        del self.polozaji_z
        
        del self.q
        del self.EM
        del self.v0
        del self.v
        del self.EE
        del self.dt
    
    def back(self):
        
        self.polozaj = self.polozaj0
        self.v = self.v0
        
        self.polozaji_x.clear()
        self.polozaji_y.clear()
        self.polozaji_z.clear()
    
    def akc(self, x):
        
        Fe  = np.dot(self.q, self.EE) + np.dot(self.q, np.cross(self.v + x, self.EM))
        akc = Fe / self.masa
        
        return akc

    def Runge_Kutta(self):
        
        t = 0.1
        
        while t < 10:
            
            k1v = self.akc(0) * self.dt
            k1 = (self.v * self.dt)

            k2v = self.akc(0.5 * k1v) * self.dt
            k2 = (self.v + 0.5 * k1v) * self.dt

            k3v = self.akc(0.5 * k2v) * self.dt
            k3 = (self.v + 0.5 * k2v) * self.dt

            k4v = self.akc(0.5 * k3v) * self.dt
            k4 = (self.v + 0.5 * k3v) * self.dt

            self.v = self.v + (1/6) * (k1v + 2 * k2v + 2 * k3v + k4v)
            self.polozaj = self.polozaj + (1/6)*(k1 + 2 * k2 + 2 * k3 + k4)
            
            self.polozaji_x.append(self.polozaj[0])
            self.polozaji_y.append(self.polozaj[1])
            self.polozaji_z.append(self.polozaj[2])
            
            t = t + self.dt

    def Euler(self):
       
        t = 0
        
        while t < 10:
            
            akc = self.akc(0)
            self.v = self.v + akc * self.dt
            self.polozaj = self.polozaj + self.v * self.dt
            
            self.polozaji_x.append(self.polozaj[0])
            self.polozaji_y.append(self.polozaj[1])
            self.polozaji_z.append(self.polozaj[2])
            
            t = t + self.dt

    def plot(self, list1, list2, list3, list4, list5, list6, label1, label2):
        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        ax.scatter(list1, list2, list3, s = 1, label = label1, c = 'r', marker ='o')
        ax.scatter(list4, list5, list6, s = 1, label = label2, c = 'b', marker ='o')
    
        ax.legend()
        
        plt.show()

    def zad1(self):
        
        self.q = 1
        self.Runge_Kutta()
        lista = [[],[],[],[],[],[],[]]
        
        for i in range(len(self.polozaji_x)):
            
            lista[0].append(self.polozaji_x[i])
            lista[1].append(self.polozaji_y[i])
            lista[2].append(self.polozaji_z[i])
        
        self.back()
        self.q = -1
        self.Runge_Kutta()
        
        for i in range(len(self.polozaji_x)):
            
            lista[3].append(self.polozaji_x[i])
            lista[4].append(self.polozaji_y[i])
            lista[5].append(self.polozaji_z[i])
        
        self.plot(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5],"pozitron","elektron")

    def zad2(self):
        
        self.q = -1
        self.Runge_Kutta()
        lista = [[],[],[],[],[],[],[]]
        
        for i in range(len(self.polozaji_x)):
            
            lista[0].append(self.polozaji_x[i])
            lista[1].append(self.polozaji_y[i])
            lista[2].append(self.polozaji_z[i])
        
        self.back()
        self.Euler()
        
        for i in range(len(self.polozaji_x)):
            lista[3].append(self.polozaji_x[i])
            lista[4].append(self.polozaji_y[i])
            lista[5].append(self.polozaji_z[i])
        
        self.plot(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],"Runge-Kutta","Euler")

    