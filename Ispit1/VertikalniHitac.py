 
import math as m
import matplotlib.pyplot as plt

class VertikalniHitac:
    
    def __init__(self, v0, h0):
        
        self.h0 = h0
        self.v0 = v0
        self.vrijeme = 0
        self.visina = [h0]
        self.brzina = [v0]
        self.vremena = [0]
        self.polozaj  = 0
        
        print(f" Objekt je uspješno stvoren. Početna brzina je {self.v0}, a visina {self.h0}.")

    def reset(self):
        
        del self.h0
        del self.v0
        del self.vrijeme 
        
        self.visina.clear()
        self.brzina.clear()
        self.vremena.clear()
        
        del self.brzina 
        del self.vremena
        del self.polozaj

    def promjena_pocetne_brzine(self,v):
        
        self.v0 = v
        
        return print(f" Promjenjena brzina je {self.v0}. ")

    def promjena_pocetne_visine(self,h):
       
        self.h0 = h
        
        return print(f" Promjenjena visina je {self.h0}. ")
    
    def Euler(self, dt):
        
        a = -9.81
        self.v0 = self.v0 + a*dt 
        self.h0 = self.h0 + self.v0 * dt 
        self.vrijeme = self.vrijeme + dt
        self.visina.append(self.h0)
        self.brzina.append(self.v0)
        self.vremena.append(self.vrijeme)
        
    def gibanje(self, dt):
        
        while self.h0 > 0:
            self.Euler(dt)
        
        return self.brzina, self.visina, self.vremena

    def plot(self,dt):
        
        self.gibanje(dt)
        
        plt.plot(self.vremena, self.visina, color = "b")
        plt.xlabel('vrijeme', fontweight = "bold")
        plt.ylabel('visina', fontweight = "bold")
        plt.show()
        
        plt.plot(self.vremena, self.brzina, color = "b")
        plt.xlabel('vrijeme', fontweight = "bold")
        plt.ylabel('brzina', fontweight = "bold")
        plt.show()

    def vrijeme_trajanja(self,dt):
        
        a, b, vrijeme = self.gibanje(dt)
        t = max(vrijeme)
        
        return t 

    def maksimalna_visina(self,dt):
        
        a, visina, vrijeme = self.gibanje(dt) 
        h = max(visina)
        
        return h