def draw_an(kind,dimension):
    if kind == "square" and dimension>1:
        for i in range(dimension):
            print("*"*dimension)
    elif kind == "triangle" and dimension>1:
        t=1
        while t<=dimension:
            print("*"*t,""*((dimension-t)//2))
            t+=1
    elif kind == "trapezoid" and dimension>1:
        t=1
        while t<=dimension:
            print(" "*(dimension-t),"*"*dimension)
            t+=1
    elif dimension<=1:
        print("dimensión incorrecta, debe ser mayor a 1")
    else:
        "palabra no encontrada válida para dibujar"
    
draw_an("square",3)
draw_an("triangle",2)
draw_an("trapezoid",6)