def ohm_law_for(voltaje=0,resistance=0,current=0):
    if type(voltaje) not in [int,float] or type(current) not in [int,float] or type(resistance) not in [int,float]:
            print("error, todos los parámetros deben ser entero o float")
            return None
    if [voltaje,resistance,current].count(0)>=2:
        print("error en parámetros, debes colocar al menos dos de ellos que no sean cero")
        return None
    else:
        if voltaje == 0:
            voltaje = round(resistance*current,2) #convertimos a solo 2 decimales
            return voltaje
        elif current == 0:
            current = round(voltaje/resistance,2)
            return current
        else:
            resistance = round(voltaje/current,2)
            return resistance
ohm_law_for("20","30")
ohm_law_for(20)
ohm_law_for(31,0)
print(ohm_law_for(10,1))
print(ohm_law_for(voltaje=10,resistance=6))