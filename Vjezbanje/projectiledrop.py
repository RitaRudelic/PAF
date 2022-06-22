
class pojectiledrop:
    
    def __init__(self, h, vx0): #avion #self.vx oznaka za 'globalno' obicna npr. vx oznaka za 'lokalno'
        
        self.h = h
        self.vx0 = vx0

        print("Objekt je uspješno stvoren. Visina je (h), a horizontalna brzina je (vx).")
 
    def promjena_visine(self, h): #promjena cijele visine (redefiniranje)
        self.h = h

    def promjena_brzine(self, delta_vx): #promjena za delta_vx
        self.vx0 = self.vx0 + delta_vx

    def gibanje(self, dt): #sadrži korak jer nema zadano vrijeme u kojem se giba

        self.x = [0] #lista za crtanje grafa, treba mi svaka točka za nacrtat graf, logično
        self.y = [self.h] #početna točka gdje počinje y je na visina h odnosno self.h
        self.vx = [self.vx0] #svaka iduća brzina je nastavak na poočetnu
        self.vy = [0] #lista mora biti od 0 kako ne bi bilo 'out od range'
        self.ax = 0 #logično
        self.ay = - 9.81 #logično

        #vrijeme se inače ne mora zadavati u listi nego se piše u listi ako se traži ovisnost npr. vy o vremenu

        self.t = [0] #u listi jer se mijenja, a 0 je jer je početno vrijeme 0
        self.dt = dt

        #AKO ZADATAK KAZE 'DOK NE PADNE' ONDA KORISTIMO WHILE PETLJU

        while self.y[-1] > 0: #-1 označava zadnji element u listi
            
            self.t.append(self.t[-1] + dt)
            self.vx.append(self.vx[-1] + self.ax * dt) 
            self.vy.append(self.vy[-1] + self.ay * dt)
            self.x.append(self.x[-1] + self.vx[-1] * dt)
            self.y.append(self.y[-1] + self.vy[-1] * dt)

            #ovo su zakoni kinematike i oni su uvijek isti! 
            #ukoliko mi akceleracija ovisi o vremenu, i nju stavljam u listu kao [-1]
            #cijela dinamika je u tome da su akceleracije konstantne

        return self.x, self.y, self.vx, self.vy, self.t 

    def vrijeme_padanja(self, dt):

        #pozivamo funkciju gibanja jer nam je ona potrebna za vrijeme padanja, logično

        self.gibanje(dt)
        return self.t[-1]

        #pri izračunavanju određenih komponenata kao npr. range, vrijeme padanja i sl. treba paziti na to je li gibanje već odrađeno ili nije ni počelo
