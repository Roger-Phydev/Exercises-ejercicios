def draw_pascal_triangle(size):
    if type(size)!=int or size<0:
        print("error, el tamaño debe ser entero positivo o cero")
    else:
        if size == 0:
            print("1")
        elif size == 1:
            print(" 1 ")
            print("1 1")
        else:
            rows = [[1],[1,1]]
            for i in range(size-1): #repetimos n-2 veces, pues ya tenemos dos filas
                actual = [1]
                for j in range(len(rows[-1])-1): #añadimos la parte de enmedio recursivamente
                    actual.append(rows[-1][j]+rows[-1][j+1])
                actual.append(1)
                rows.append(actual)
            for list in rows:
                print(" "*(len(actual)-len(list)),list)
draw_pascal_triangle(-1)
draw_pascal_triangle([])
draw_pascal_triangle({})
draw_pascal_triangle(2.3)
draw_pascal_triangle("sd")
draw_pascal_triangle(0)
draw_pascal_triangle(1)
print(draw_pascal_triangle(10))