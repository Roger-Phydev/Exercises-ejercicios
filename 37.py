from datetime import date
zelda_dict = { #creamos un diccionario con los títulos y fechas de lanzamientos
    "tloz":date(1986,2,21),
    "zelda ii":date(1987,1,14),
    "a link to the past":date(1991,11,21),
    "ocarina of time":date(1998,11,21),
    "majora's mask":date(2000,4,27),
    "the wind waker":date(2002,12,13),
    "four swords adventures":date(2004,3,18),
    "twilight princess":date(2006,11,19),
    "skyward sword":date(2011,11,18),
    "breath of the wild":date(2017,3,3),
    "tears of the kingdom":date(2023,5,12),
    "link's awakening":date(1993,6,6),
    "oracle of seasons":date(2001,2,27),
    "oracle of ages":date(2001,2,27),
    "the minish cap":date(2004,11,4),
    "phantom hourglass":date(2007,6,23),
    "spirit tracks":date(2007,12,7),
    "a link between worlds":date(2013,11,22),
    "triforce heroes":date(2015,10,22),
    "four swords":date(2001,11,20)
}
def years_between_zelda_titles(zelda_title_one,zelda_title_two):
    zelda_title_two = zelda_title_two.lower()
    zelda_title_one = zelda_title_one.lower()
    titles = list(zelda_dict.keys())
    date_one, date_two = 0,0 #creamos variables para guardar fechas
    if zelda_title_one in titles:#si el primer titulo se encuentra entre los permitidos
        date_one = zelda_dict[zelda_title_one] #le asociamos la fecha deseada
    else:
        print(f"tu primer título no es válido, verifica que se encuentre entre los siguientes {titles}")#le mostramos los títulos válidos
        return None
    if zelda_title_two in titles: #hacemos lo mismo con los el segundo título
        date_two = zelda_dict[zelda_title_two]
    else:
        print(f"tu segundo título no es válido, verifica que se encuentre entre los siguientes {titles}")
        return None
    diff = abs(date_two-date_one)
    return f"la diferencia entre los títulos es {diff.days//365} años y {diff.days%365} días, osea {diff.days} días en total"
years_between_zelda_titles("fesif","zelda ii") #primer titulo erroneo
years_between_zelda_titles("tloz","wind waker") #segundo título errorneo
print(years_between_zelda_titles("tloz","ocarina of time"))