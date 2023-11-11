def second_greatest(numbers_list):
    copy = numbers_list.copy() #creamos esta copia para no modificar la lista
    m = max(copy) #calculamos su máximo
    while m in copy: #mientras ese número esté en la lista
        copy.remove(m)#lo removemos
    return max(copy)#y el retornamos el nuevo máximo, que será el segundo valor más grande, pues ya quitamos el anterior
a = [1,4,5,2,8,10,10]
print(second_greatest(a))
a.append(12)
print(second_greatest(a))
a.remove(8)
a.remove(10)
a.remove(10)
print(second_greatest(a))