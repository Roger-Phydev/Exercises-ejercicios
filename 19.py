def mili_conversor(days=0,hours=0,minutes=0,seconds=0):#por defecto, cada variable se anula
    return days*24*60*60*1000 + hours*60*60*1000 + minutes*60*1000 + seconds*1000
#simplemente multiplicamos por el factor adecuado cada cantidad:
# 1 segundo = 1000 milisegundos
# 1 minuto = 60 segundos
# 1 hora = 60 minutos
# 1 día = 24 horas
print(mili_conversor(seconds=1)) #1 segundo
print(mili_conversor(0,0,30))#30 minutos