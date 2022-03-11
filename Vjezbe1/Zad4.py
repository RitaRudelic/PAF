def nadi_jednadzbu_pravca(x1,x2,y1,y2):
    k = (y2-y1)/(x2-x1)
    l = k*(-x1) + y1
    if l == 0: 
        print(f"Jednadzba pravca je: y = {k}x")
    else:
        print(f"Jednadzba pravca je: y = {k}x + {l}")

while True:
    a = input("Napišite x koordinatu prve tocke: ")
    try:
        x1 = float(a)
        break
    except ValueError:
        print("Koordinata mora biti broj, ponovno upišite.")

while True:
    b = input("Napišite y koordinatu prve tocke: ")
    try:
        y1 = float(b)
        break
    except ValueError:
        print("Koordinata mora biti broj, ponovno upišite.")

while True:
    c = input("Napišite x koordinatu druge tocke: ")
    if c == a:
        print("x druge tocke mora biti razlicit odo x-a prve tocke, ponovno upišite!")
    else:
        try:
            x2 = float(c)
            break
        except ValueError:
            print("Koordinata mora biti broj, ponovno upišite.")

while True:
    d = input("Unesite y koordinatu druge tocke: ")
    try:
        y2 = float(d)
        break
    except ValueError:
        print("Koordinata mora biti broj, ponovite unos.")

nadi_jednadzbu_pravca(x1,x2,y1,y2)