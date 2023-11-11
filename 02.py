def is_anagram(word_one,word_two):#creamos la función / this is the function we need
    word_one = word_one.lower() #I turn each word into lower case, in order to simplify the code
    word_two = word_two.lower() #con esto evitamos que importe si las letras son mayúsculas o minúsculas
    if word_one == word_two: #descartamos el caso de que sean iguales
        return False #if they're the same word, it's false
    elif sorted(word_one) == sorted(word_two): #if, after order each word, they are the same
        return True #they're anagrams
    else: 
        return False
print(is_anagram("jalisco","Amor"))
print(is_anagram("amor","roma"))