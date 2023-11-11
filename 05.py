def area_poligono(kind,base,height=0): #esta función recibirá el tipo, y un segundo o tercer parametro
    #para tener cubierto el caso del cuadrado, haremos que el segundo parametro por defecto sea nulo.
    kind = kind.lower() #con esto eliminamos la necesidad de usar minúsculas o mayúsculas
    if kind == "triangulo" or kind == "triángulo": #no importan los acentos
        return (base*height)*0.5 #usamos b*h/2
    elif kind == "cuadrado":
        return base**2 #devuelve el cuadrado del primer parámetro para que el segundo no importe si lo coloca o no
    elif kind == "rectangulo" or kind == "rectángulo":
        return base*height # b*h
    else:
        print("Oops, verifica lo siguiente: 1er parámetro puede ser cuadrado, triángulo o rectángulo")
print(area_poligono("cuadrado",3))