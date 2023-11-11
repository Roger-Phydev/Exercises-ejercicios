from datetime import date
def thirty_bisiest_next_years_to(year):
    years_list = [] #creamos la lista donde guardamos los años
    while len(years_list)<31: #mientras haya menos de 31 años bisiestos
        try: #ponemos a prueba el código
            date(year,2,29) #si existe el 29 de feb, no habrá error
            years_list.append(year) #continuará por aquí y agrega el año
            year+=1 #pasamos al siguiente año
        except: #en caso que no exista, marcará error
            year+=1 #simplemente aumentamos el año
    return years_list #regresamos la lista
print(thirty_bisiest_next_years_to(1995))
print(thirty_bisiest_next_years_to(1900))
#en la última presentación, se muestra porque no se debe usar un año que es bisiesto como comparación e ir sumando 4, pues hay años como 1900 que
#no obedecen esta regla, pues a pesar de ser multiplos de 4 no son bisiestos, al no se divisibles por 400.
#al verificar que exista tal día, nos evitamos este error.
