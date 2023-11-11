import datetime
def adev_calendar(datetime_type_day):
    try: #ponemos esto para ver que no ocurra un problema
        if type(datetime_type_day)==datetime.date: #si el tipo es date
            datetime_type_day = datetime.datetime(datetime_type_day.year,datetime_type_day.month,datetime_type_day.day) #lo convertimos a datetime
        prizes = { #creamos un diccionario con los premios
            datetime.date(2022,12,1):"Iphone",
            datetime.date(2022,12,2):"Xbox SX",
            datetime.date(2022,12,3):"Ps5",
            datetime.date(2022,12,4):"Nintendo Switch",
            datetime.date(2022,12,5):"Xbox SS",
            datetime.date(2022,12,6):"Iphone",
            datetime.date(2022,12,7):"RTX 4090",
            datetime.date(2022,12,8):"RTX 3090",
            datetime.date(2022,12,9):"Steam deck",
            datetime.date(2022,12,10):"Oculus rift",
            datetime.date(2022,12,11):"Iwatch",
            datetime.date(2022,12,12):"Ipad",
            datetime.date(2022,12,13):"2 años gamepass ultimate",
            datetime.date(2022,12,14):"Core i9",
            datetime.date(2022,12,15):"Ryzen 9",
            datetime.date(2022,12,16):"Pc gamer gama media baja",
            datetime.date(2022,12,17):"Xbox SX",
            datetime.date(2022,12,18):"Pc gamer gama media alta",
            datetime.date(2022,12,19):"Ipad",
            datetime.date(2022,12,20):"Pc gamer gama media alta",
            datetime.date(2022,12,21):"Nintendo switch",
            datetime.date(2022,12,22):"Xbox series S + Nintendo switch",
            datetime.date(2022,12,23):"Ps5 + Ps4",
            datetime.date(2022,12,24):"PC gamer gama alta"
        }
        before = datetime.datetime(2022,12,1) - datetime_type_day #calculamos esta diferencia para saber si fue antes. esto inicia en 0
        after = datetime_type_day - datetime.datetime(2022,12,25) #esto sirve para saber si se pasó de la fecha #acaba a las 23 59 59
        if before.total_seconds()>0: #mientras el total de segundos sea positivo
            time_part = int(before.total_seconds()) - before.days*3600*24 #calculamos los segundos no debidos a días
            time_part = [time_part//3600,(time_part%3600)//60,time_part%60] #calculamos horas, minutos y segundos
            print(f"Aún faltan {before.days} días {time_part[0]} horas {time_part[1]} minutos y {time_part[2]} segundos para que inicie el sorteo") #mostramos cuanto falta
        elif after.total_seconds()>0: #si está después del final
            time_part = int(after.total_seconds()) - after.days*3600*24
            time_part = [time_part//3600,(time_part%3600)//60,time_part%60]
            print(f"Lamentablemente el sortéo termino hace {after.days} días {time_part[0]} horas {time_part[1]} minutos y {time_part[2]} segundos") #mostramos hace cuanto acabó
        # no puede ocurrir ambas condiciones a la vez, pues si ocurre la primera, fecha<inicio => fecha< final
        #viceversa, si fecha>final => fecha>final
        else:
            remaining = int((datetime.datetime(datetime_type_day.year,datetime_type_day.month,datetime_type_day.day+1)-datetime_type_day).total_seconds()) #vemos cuanto falta para el días siguiente
            remaining = [remaining//3600,(remaining%3600)//60,remaining%60] #calculamos lo restante en forma adecuada
            print(f"El premio del día de hoy {datetime_type_day.date()} es: {prizes[datetime_type_day.date()]}") #mostramos la fecha y premio
            print(f"Y restan {remaining[0]} horas {remaining[1]} minutos y {remaining[2]} segundos para reclamarlo ") #mostramos cuanto queda para que acabe
    except:
        print("verifica que tu fecha sea un datetime o date ejemplo: datetime.datetime(1990,9,23,4,50,34) | datetime.date(2013,9,16)")
antes = datetime.date(2022,11,1)
después = datetime.datetime(2023,4,1,10,1,1)
inicio = datetime.datetime(2022,12,1,10,0,0)
final = datetime.date(2022,12,24)
intermedio = datetime.datetime(2022,12,18,16,30,0)
adev_calendar(antes) #aquí falta para que inicie, el formato date no es problema
adev_calendar(después) #aquí ya pasó el sorteo, tampoco importa el tipo date time
adev_calendar(inicio) #aquí es el primer día de sorteo
adev_calendar(final) #aquí es el último día de sorteo
adev_calendar(intermedio) #aquí es un día intermedio