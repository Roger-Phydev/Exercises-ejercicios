import re
def handles_in(an_string):
    website = r"(https://|http:|www.)[^\s]+\.[a-z\.0-9]{2,6}" #se compone de un inicio, caracteres que no sean un espacio un punto y luego
    #de 2 a seis caracteres que sean una letra minúscula, un número o un punto ejemplo: com.mx2
    users_matches = list(re.finditer("@[a-zA-Z0-9]+",an_string)) #creamos una lista con todas las coincidencias de usuarios
    hashtags_matches = list(re.finditer("#[a-zA-Z0-9]+",an_string)) #creamos otra lista para todas las coincidencias de hashtags
    websites_matches = list(re.finditer(website,an_string)) #creamos una lista con todas las coincidencias de inicio de página web
    users = []
    hashtags = []
    websites = []
    for element in users_matches:
        start,end = element.span() #tomamos el inicio y final de la coincidencia
        users.append(an_string[start:end]) #la agregamos a la lista
    for element in hashtags_matches:
        start,end = element.span()
        hashtags.append(an_string[start:end])
    for element in websites_matches:
        start,end = element.span()
        websites.append(an_string[start:end])
    handles = {} #creamos un diccionario que guarde cada cosa
    handles["users"] = users
    handles["hashtags"] = hashtags
    handles["websites"] = websites
    return handles #devolvemos el diccionario
proof = "#mario #listening @holly43 @josua4 www.aber.com.es dario @MATIAS13 #Learning https://dragon-quest.com http:final_fantasy_17.com.jp www.google/jl%$sdhj/hsajhf.com.es"
print(handles_in(proof)) #en efecto, devuelve lo que esperabamos