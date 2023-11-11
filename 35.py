def damage_pokemon_attack(attack_type,deffense_type,attack_stat,deffense_stat):
    attack_type = attack_type.lower() #ponemos todo en minúsculas para que todo funcione bien
    deffense_type = deffense_type.lower()
    w = "agua" #creamos variables con los nombres para no cometer errores
    f = "fuego"
    p = "planta"
    e = "electrico"
    effectivity = 0 #inicializamos la efectividad
    if (attack_type,deffense_type) in [(w,w),(f,f),(p,p),(e,e),(f,w),(w,p),(p,f),(e,p)]: #revisamos si coincide con algún caso
        effectivity = 0.5 #asociamos la efectividad correspondiente
    elif (attack_type,deffense_type) in [(f,e),(w,e,),(p,e),(e,f)]:
        effectivity = 1
    elif (attack_type,deffense_type) in [(f,p),(w,f),(p,w),(e,w)]:
        effectivity = 2
    else:
        print("tipos no válidos, verifica que no tenga acentos, los únicos tipos disponibles son: agua,fuego,planta y electrico")
        return None #en este caso se acaba
    damage = 50 * (attack_stat/deffense_stat) * effectivity
    return (f"el daño hecho por el ataque {attack_type} al defensor {deffense_type} es {damage} con efectividad {effectivity}")
example = ["planta","fuego","agua","electrico"]
for element in example:#imprimimos todos los casos
    for item in example:
        print(damage_pokemon_attack(element,item,100,100))#con stat de 100 en cada caso

    
