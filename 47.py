def most_common_vowel(an_string):
    m = 0
    an_string = an_string.lower() #ponemos todo en minúsculas para simplificar
    vowels = ["a","e","i","o","u"] #creamos listos de vocales
    changed_vowels = ["á","é","í","ó","ú"] #y vocales con acento
    #primero quitamos las versiones con acento
    for i in range(len(vowels)): #para cada indice
        while an_string.count(changed_vowels[i])!=0: #mientras hayan letras con acento
            an_string.replace(changed_vowels[i],vowels[i]) #las reemplazamos por su versión sin acento
    m = 0 #este será la cantidad que más se repite.
    for vowel in vowels:
        m = max(m,an_string.count(vowel)) #calculamos el máximo número de las vocales
    common = "" #esta señalará la vocal más común
    if m == 0: #en caso que no haya vocales
        return common+" " #simplemente retornamos nada
    else:
        for vowel in vowels: #para cada vocal
            if an_string.count(vowel)==m:#si concuerda con el máximo
                common+=vowel+" " #la añadimos
        return common #regresamos la cadena resultante
print(most_common_vowel("aeiou   ")) #todas son lo máximo
print(most_common_vowel("comida"))
print(most_common_vowel("pwrt"))
print(most_common_vowel("rata"))