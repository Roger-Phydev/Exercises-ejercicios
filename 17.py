import re
def is_obstacule_race_completed(racer,course):
    if len(course)==course.count("|")+course.count("_") and re.match(r"[^run|jump]",racer)==None: 
        #para que funcione, solo debe haber run y jump en racer, por ello el match debe ser nulo
        #también solo debe haber | y _ en course, por lo que la longitud debe ser la suma de la cantidad de ambos
        racer_comparative = [] #este será el corredor que buscamos
        course = list(course) #en caso afirmativo, a la pista solo la separamos caracter por caracter
        while re.match("run|jump",racer)!=None: #mientras haya run o jump en la cadena
            start,end = re.match("run|jump",racer).span()
            racer_comparative.append(racer[start:end])#agregamos la palabra
            racer = racer[0:start]+racer[end:] #removemos la parte que coincidió
        if len(course)<=len(racer_comparative):#si hay más o igual cantidad de cosas en el corredor
            for i in range(len(course)): #para cada parte de la pista revisamos
                if racer_comparative[i]=="jump" and course[i]=="_":#si salta en parte plana
                    course[i]="x"#variamos esa entrada
                elif racer_comparative[i]=="run" and course[i]=="|":#si corre en valla
                    course[i]="/"#variamos la entrada
            if course.count("x")>0 or course.count("/")>0: #en caso de que la pista tenga por lo menos algún x o /
                m = course.count("/")+course.count("x")
                print(f"el corredor cometió {m} error(es)")
                return False#no se habrá completado
            else:
                return True #caso contrario cuando no tiene ninguno
        else: #en caso que el corredor haya tenido menos movimientos que la pista
            print("la pista debe ser de igual o menor tamaño que las acciones del corredor")
            return False #directamente no lo consiguió
    else:
        print("Hubo un error en tus entradas:")
        print("racer solo debe incluir expresiones run y jump sin espacios, ej. (jumprunjumpjump) pero no puede ser (jump run jump great) ")
        print("la pista course solo debe incluir caracteres | y _, _=suelo |=vaya, ej. (___|||__||_) está bien, pero no (__|p )")
        

corr = "jumprunjumprunrun"
pista = "|_|__"
print(is_obstacule_race_completed(corr,pista))
corr+="jump"
print(is_obstacule_race_completed(corr,pista)) #aún si agregamos más acciones al corredor, no altera el resultado
pista+="_" #si agregamos a la pista, se debe ver que pasa
print(is_obstacule_race_completed(corr,pista)) #si cometió un error, nos muestra cuantos cometió y devuelve false
pista+="||"
print(is_obstacule_race_completed(corr,pista)) #si la pista de mayor tamaño nos muestra el error y devuelve false
pista+="lpsdfger"
print(is_obstacule_race_completed(corr,pista)) #si la pista no contiene solo lo señalado, nos manda un mensaje para que corrijamos
