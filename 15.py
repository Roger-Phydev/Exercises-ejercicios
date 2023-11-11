import re
import datetime
def how_may_days_between(first_date,second_date):
    try:#como ponemos un try, evitamos errores y así...
        first_date = first_date.split("/")#presuponemos que cumple el formato
        second_date = second_date.split("/")#separamos usando los separadores
        date_1 = datetime.date(int(first_date[2]),int(first_date[1]),int(first_date[0])) #de esta manera, agregamos según el formato,a un date
        date_2 = datetime.date(int(second_date[2]),int(second_date[1]),int(second_date[0])) #cada caso
        delay = abs(date_2-date_1) #calculamos la diferencia absoluta
        return delay.days #y regresamos los días
    except:#en caso que no cumpla el formato, señalamos esto
        print("Hubo un error en alguno de tus argumentos, debe tener el formato: dd/mm/aaaa") #mostramos un mensaje según que falle.
        return None #y devolvemos none

begin = "10/05/1996"
end = "7/7/1996"
print(how_may_days_between(begin,end))#vemos que el poner 05 no afecta el funcionamiento
print(how_may_days_between(end,begin))#vemos que da igual el orden
print(how_may_days_between("1996/23/11","11/06/1998")) #aquí falla el primer argumento
