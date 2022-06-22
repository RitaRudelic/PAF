import projectiledrop as pro

avion1 = pro.pojectiledrop(1000, 400)
avion2 = pro.pojectiledrop(1500, 600)

avion1.promjena_visine(1200)
avion1.promjena_brzine(-100)
print(avion1.h)
print(avion1.vx0)

avion2.promjena_visine(500)
avion2.promjena_brzine(200)
print(avion2.h)
print(avion2.vx0)