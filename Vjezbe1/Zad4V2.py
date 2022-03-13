def jednadzba(x1,y1,x2,y2):
    k = (y2-y1)/(x2-x1)
    l = k*(-x1) + y1

    print("y=" + str(k) + "x +" + str(l))

jednadzba(2, 3, 4, 5)   