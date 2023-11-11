a = 10
b = 6
def mcd(number_one,number_two):
    N = max(abs(number_one),abs(number_two)) #buscamos el máximo y el mínimo
    m = min(abs(number_one),abs(number_two))
    r = N%m
    while r!=0: #mientras el resto sea no nulo
        N = m #ahora usamos el número por el que dividiamos
        m = r #cambiamos al residuo
        r = N%m #y cambiamos el residuo
    return m #regresamos el m que quede
def MCM(number_one,number_two):
    return abs(number_one*number_two)//(mcd(number_one,number_two)) #aprovechamos la relación mcd(a,b)*MCM(a,b) = |a*b|
print(mcd(324,180))
print(MCM(10,4))