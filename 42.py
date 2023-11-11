import re
def temperature_conversor(temperature):
    celsius = r"[-]{0,1}[0-9]+°C|[-]{0,1}[0-9]*.[0-9]+°C" #creamos patrones según el caso de cada escala
    farenheit = r"[-]{0,1}[0-9]+°F|[-]{0,1}[0-9]*.[0-9]+°F"
    if type(temperature)!=str:
        print("error, tu entrada debe ser un string")
        return None
    if re.match(celsius,temperature)!=None:
        temperature = temperature.replace("°C","") #quitamos la coletilla
        temperature = float(temperature) #reconvertimos
        return round(temperature*(9/5)+32,2) #regresamos el valor querido
    elif re.match(farenheit,temperature)!=None:
        temperature = temperature.replace("°F","")
        temperature = float(temperature)
        return round((temperature-32)*(5/9),2)
    else:
        print("error, no concuerda con alguno de los formatos: número°C o número°F")
temperature_conversor(123)
temperature_conversor("24")
print(temperature_conversor("0.0°C"))
print(temperature_conversor("32°F"))
print(temperature_conversor("-10°C"))
