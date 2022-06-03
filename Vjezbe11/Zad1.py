import numpy as np
import modul as em
import matplotlib.pyplot as plt


Sun = {
 
  "polozaj" : np.array([0, 0]),
  "masa":1.989 * 10**30,
  "brzina":np.array([0, 0]),
  "velicina": 500,
  "ime":"Sunce",
  "boja" : "y"
}

Earth = {
  
  "polozaj" : np.array([1.486 * 10**11, 0]),
  "masa" : .9742 * 10**24,
  "brzina" : np.array([0, 29783]),
  "velicina": 100,
  "ime" : "Zemlja",
  "boja" : "g"
}

p = em.Solar_Sistem(Sun, Earth)
p.plot()
p.reset()

    