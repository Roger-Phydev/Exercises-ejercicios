def inv_string(an_string):
    inv = ""#creamos un string vacío
    for i in range(len(an_string)): #para cada índice
        inv+= an_string[-i-1] #lo invertimos
    return inv #devolvemos lo pedido
print(inv_string("Hola mundo"))