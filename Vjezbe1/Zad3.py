while True:
    a = input(" Napišite x koordinatu prve tocke: ")
    try:
        x1 = float(a) 
        break
    except ValueError:
        print(" Koordinata mora biti broj, ponovno upišite. ")

while True:
    b = input(" Napišite y koordinatu prve tocke: ")
    try:
        y1 = float(b)
        break
    except ValueError:
        print(" Koordinata mora biti broj, ponovite upišite.")

while True:
    c = input(" Napišite x koordinatu druge tocke: ")
    if c == a:
        print(" x druge tocke mora biti razlicit od x-a prve tocke, ponovno upišite ")
    else:
        try:
            x2 = float(c)
            break
        except ValueError:
            print(" Koordinata mora biti broj, ponovno upišite. ")

while True:
    d = input(" Napišite y koordinatu druge tocke: ")
    try:
        y2 = float(d)
        break
    except ValueError:
        print(" Koordinata mora biti broj, ponovno upišite")

k = (y2-y1)/(x2-x1)
l = k*(-x1) + y1

if l == 0:
    print(f" Jednadzba pravca glasi: y = {k}x ")
else:
    print(f" Jednadzba pravca glasi: y = {k}x + {l} ")
