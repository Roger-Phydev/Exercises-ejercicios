def words_counter(frase):
    frase = frase.lower() #así evitamos que importen las mayúsculas o minúsculas
    frase = frase.replace(".","")#reemplazamos los valores de puntuación por una casilla en blanco
    frase = frase.replace(",","")
    frase = frase.replace(";","")
    frase = frase.replace(":","")
    frase = frase.split(" ") # hacemos una lista con los elementos
    frase.remove("") #quitamos los espacio de más
    words = frase.copy() #creamos una copia de todas las palabras de la frase
    words = set(words) #convertimos a conjunto para evitar repeticiones
    words = list(words) #una vez quitadas, lo volvemos a convertir a lista
    words.sort() #lo ordenamos
    repeats = [0 for i in range(len(words))] #creamos una lista en blanco
    for i in range(len(words)): #para cada indice
        for word in frase: #para cada palabra en la frase
            if words[i] == word: #si coincide con una palabra
                repeats[i]+=1 #aumentamos el contador de la palabra
    print("Palabra : veces que aparece")
    for i in range(len(words)): #imprimimos cada palabra con sus repeticiones
        print(f"{words[i]}: {repeats[i]}")
p = "Estoy muy feliz porque me agrada todo lo que he aprendido. Aunque me gustaría aprender más, la verdad es que nunca es suficiente; así es, esto es lo que pienso : soy feliz, dlr dlr dlr dlr"
words_counter(p)
