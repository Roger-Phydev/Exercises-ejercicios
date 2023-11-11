import time
def delayed_sum(a,b,seconds_delay):
    time.sleep(seconds_delay)#espera el tiempo señalado 
    return a+b #luego devuelve el valor
print(delayed_sum(1,1,0.5))