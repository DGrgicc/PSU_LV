try:
    ocjena = float(input("Unesi ocjenu: "))
    while ocjena > 1 or ocjena < 0:
        ocjena = float(input())
    if ocjena >= 0.9:
        print("A")
    elif ocjena >= 0.8:
        print("B")
    elif ocjena >=0.7:
        print("C")
    elif ocjena >=0.6:
        print("D")
    else:
        print("F")
except:
    print("An exception occurred")



