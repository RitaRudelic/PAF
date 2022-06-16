import numpy as np
import modul as m
import matplotlib.pyplot as plt


Sun = {
  
  "polozaj" : np.array([0, 0]),
  "masa": 1.989E30,
  "brzina": np.array([0, 0]),
  "velicina": 500,
  "ime":"Sunce",
  "boja" : "y"

}

Mercury = {
 
  "polozaj" : np.array([6.925E10, 0]),
  "masa": 3.3022E23,
  "brzina": np.array([0, 47362]),
  "velicina": 53,
  "ime" : "Merkur",
  "boja" : "gray"

}

Venus = {
 
  "polozaj" : np.array([1.08E11, 0]),
  "masa": 4.867E24,
  "brzina": np.array([0, 35020]),
  "velicina": 58,
  "ime" : "Venera",
  "boja" : "orange"

}

Earth = {
 
  "polozaj" : np.array([1.486E11, 0]),
  "masa": 5.9742E24,
  "brzina": np.array([0, 29783]),
  "velicina": 100,
  "ime" : "Zemlja",
  "boja" : "g"

}

Mars = {

  "polozaj" : np.array([2.475E11, 0]),
  "masa": 6.417E23,
  "brzina": np.array((0, 24007)),
  "velicina": 75,
  "ime" : "Mars",
  "boja" : "r"
}

p1 = m.Universe(Sun, Mercury, Venus, Earth, Mars)
p1.plot()
p1.reset()