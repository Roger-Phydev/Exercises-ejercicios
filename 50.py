import re
def karaka_crypt(an_string):
    if type(an_string)==str and re.match("[\w]+",an_string)!=None and re.findall("[0-9]",an_string)!=list(an_string):
        #debe ser un str, contener al menos un alfanumérico y no debe contener solo números
        listed = list(an_string.lower())
        listed.reverse()
        code = ""
        for element in listed:
            code+=element
        #hasta aquí invertimos la cadena
        vowels = list("aeiou") #definimos una lista de vocales
        tail = "aca" #y la coletilla
        print(code)
        if code.startswith(tail) and len(tail)<len(code) and re.match(r".+[0-4]+",code)!=None:
            #si contiene al menos un número del 0 al 4, es más largo que aca e inicia con ello, esta encriptado:
            code = code[3:] #quitamos los primeros 3 caracteres, quitando aca
            for i in range(5):
                code = code.replace(str(i),vowels[i],-1) #reemplazamos todos los números entre 0 y 4 por su letra
        else:
            for i in range(5): #para cada número de 0 a 4
                if code.find(vowels[i])!=-1: #si hay alguna vocal
                    code = code.replace(vowels[i],str(i),-1) #las remplazamos por su equivalente numérico
            code+=tail #y le pegamos la coletilla
        return code

a = "rogeliO"
print(karaka_crypt("    ")) #no funciona por ser solo espacios
print(karaka_crypt("12324435546")) #no funciona al ser solo números
print(karaka_crypt(21243)) #no funciona al no ser str
print(karaka_crypt(a)) #aqui funciona
print(karaka_crypt(karaka_crypt(a))) #como era de esperarse, al aplicar dos veces, regresa el original en minúsculas