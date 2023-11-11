#1er manera: for
for i in range(100):
    print(i+1) #para el rango imprimimos el número adecuado, se toma en cuenta que i llega hasta 99
#2da manera: while
r=1 #iniciamos la variable
while r<101: #mientras el número sea menor a 101
    print(r) #imprimimos el número
    r+=1 #sumamos uno
#3ra manera: listas con range
count = list(range(1,101)) #creamos una lista usando range
for element in count:
    print(element) #imprimimos cada elemento
#4ta manera: lista compacta
count = [i for i in range(1,101)] #podemos hacer compacta la lista
for element in count:
    print(element)
#5ta manera: aprovechando len y un str:
s = "l"
while len(s)<101:
    print(s.count("l"))
    s+="l"
#6ta manera: usando una lista y append:
l = [""]
while len(l)<101:
    print(len(l))
    l.append("")
#7ma manera: funciones recursivas
def count_to_100(n):
    if n ==101:
        return "listo" #si llega a 101 regresa "listo"
    else: #en caso contrario
        print(n) #imprime el número
        n+=1 #le incrementa 1
        count_to_100(n) #volvemos a aplicarle la función
count_to_100(1)
