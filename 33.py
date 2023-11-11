def chinese_symbol_and_element(year):
    simbols = ["rata","buey","tigre","conejo","dragón","serpiente","caballo","oveja","mono","gallo","perro","cerdo"] #creamos la lista de signos
    elements = ["madera","fuego","tierra","metal","agua"] #creamos la lista de elementos
    diff = year-1984 #calculamos la diferencia con el año que conocemos que inicia el ciclo.
    return simbols[diff%12]+" "+elements[(diff//2)%5] #devolvemos esto, explicación:
    # para simbolos usamos modulo 12 porque cada 12 años se repite
    # para los elementos, cada 2 cambia de símbolo (se usa la división entera), y se repite cada 5 cambios(módulo 5)
for i in range(120):
    print(chinese_symbol_and_element(1984+i),end=" || ")
#imprimimos 120 años y vemos que pasa, en este caso funciona adecuadamente
print(chinese_symbol_and_element(1996)) #mi simbolo y elemento