letters_and_code = { #creamos un diccionario con la conversión
    "a":".-",
    "b":"-...",
    "c":"-.-.",
    "ch":"----",
    "d":"-..",
    "e":".",
    "f":"..-.",
    "g":"--.",
    "h":"....",
    "i":"..",
    "j":".---",
    "k":"-.-",
    "l":".-..",
    "m":"--",
    "n":"-.",
    "ñ":"--.--",
    "o":"---",
    "p":".--.",
    "q":"--.-",
    "r":".-.",
    "s":"...",
    "t":"-",
    "u":"..-",
    "v":"...-",
    "w":".--",
    "x":"-..-",
    "y":"-.--",
    "z":"--..",
    "0":"-----",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    ".":".-.-.-",
    ",":"--..--",
    "?":"..--..",
}
def reverse_code(my_string): #creamos una función que busque la letra correspondiente a un código
    codes = list(letters_and_code.values()) #creamos la lista de codigos
    return list(letters_and_code.keys())[codes.index(my_string)] #devolvemos el elemento de las claves que tenga el indice acorde al argumento
def morse_coder(an_string):
    if an_string.count("-")>0:#si hay más de un signo - será clave morse
        normal = str() #iniciamos este string que guardará la oración
        an_string = an_string.split("   ") #convertimos a lista considerando separación con tres espacios entre palabras
        for word in an_string: #para cada palabra
            word = word.split(" ") #cada palabra la separamos en sus letras considerando que estan se separan por un espacio
            for letter in word:#para cada letra en la palabra
                normal+=reverse_code(letter) #le agregamos cada letra
            normal+=" "#dejamos un espacio entre palabras, como en la escritura normal
        return normal #devolvemos la expresión
    else: #en el caso contrario, nos meten texto y debemos mostrar código
        an_string = an_string.lower() #volvemos todo minúsculas para que funcione
        morse = str() #iniciamos la cadena donde guardaremos todo
        an_string = an_string.split(" ") #separamos usando espacio en blanco
        for j in range(len(an_string)): #para cada palabra
            for i in range(len(an_string[j])): #para cada letra
                morse+= letters_and_code[an_string[j][i]] #le añadimos el código equivalente
                if i < len(an_string[j])-1: #si la letra no es la última
                    morse+= " "#metemos el espacio de separación entre letras
            if j < len(an_string)-1: #si no es la última palabra
                morse+="   "#añadimos los tres espacios para separar palabras
        return morse #devolvemos lo que nos quedó
b = morse_coder("brian")
print(b) #convierte a morse
print(morse_coder(b)) #naturalmente al aplicarla dos veces, devuelve lo que metimos originalmente
a = "sOS"
print(a)
print(morse_coder(a))
print(morse_coder(morse_coder(a)))