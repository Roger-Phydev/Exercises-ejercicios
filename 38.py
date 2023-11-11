def binary_to_dec(binary_number):
    binary_number = list(str(binary_number)) #lo convertimos a lista
    if len(binary_number)!=binary_number.count("1")+binary_number.count("0"):#verificamos que sea algo que solo contenga 0 y 1
        print("verifica tu numero binario") 
        return None
    n = 0
    for i in range(len(binary_number)):
        n+= (2**(len(binary_number)-i-1))*int(binary_number[i]) #multiplicamos por la potencia de 2 adecuada y sumamos
    return n
a = "en efecto"
b = 10.1
c = 1001
d = 1000101010
binary_to_dec(a)
binary_to_dec(b)
print(binary_to_dec(c))
print(binary_to_dec(d))