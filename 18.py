#una matriz en python no existe como tal
# Para ello recurriremos a las listas dentro de listas
def who_won_game(matriz):
    if len(matriz)==3==len(matriz[0])==len(matriz[1])==len(matriz[2]):#checamos si tiene las dimensiones equivocadas
        valid_symbols = {"","O","X"} #creamos un conjunto con los símbolos válidos
        if set(matriz[0]).issubset(valid_symbols) and set(matriz[1]).issubset(valid_symbols) and set(matriz[2]).issubset(valid_symbols): #vemos si solo contiene simbolos válidos
            x = matriz[0].count("X") + matriz[1].count("X") + matriz[2].count("X") #creamos variables que cuenten las x y o presentes
            o = matriz[0].count("O") + matriz[1].count("O") + matriz[2].count("O")
            if abs(x-o)<=1: #solo procedemos si la diferencia entre la cantidad de x y o es uno a lo más (correspondiente a que van tirando uno a uno)
                win = [] #nos serevirá para saber las coincidencias con una manera de ganar
                for i in range(3): #para cada índice
                    if matriz[i][0] == matriz[i][1] == matriz[i][2] and matriz[i][0]!="": #si coincide un renglón y no son vacíos
                        win.append(matriz[i][0]) #agregamos el símbolo que ganó
                    elif matriz[0][i] == matriz[1][i] == matriz[2][i] and matriz[0][i]!="": #si coincide una columna
                        win.append(matriz[0][i]) #agregamos el símbolo que ganó
                if matriz[0][0] == matriz[1][1] == matriz[2][2] and matriz[1][1]!="": #si se forma esta diagonal sin ser vacíos
                    win.append(matriz[1][1])#agregamos el simbolo ganador
                if matriz[0][2] == matriz[1][1] == matriz[2][0] and matriz[1][1]!="": #si se forma la otra diagonal sin ser vacíos
                    win.append(matriz[1][1]) #agregamos el símbolo ganador
                if win.count("X") == win.count("O") == 0 :# en caso que no haya ganadores
                    return "TIE" #regresa tie, al no haber ganador, significa un empate
                elif win.count("X") == 1 and win.count("O") == 0: #en caso que solo haya ganado X
                    return "X" #regresa X
                elif win.count("X") == 0 and win.count("O") == 1: #en caso que solo haya ganado O
                    return "O" #regresa O
                else:
                    return "both won"  #el caso restante es cuando hay por lo menos uno ganado para cada uno, es decir, ambos ganaron
            else:#este caso corresponde a cuando la proporción de X y O no es correcta
                return None #en tal caso regresamos none
        else:#si no contiene solo símbolos válidos lo informamos
            print(f"Tu matriz solo debe incluir alguno de los siguientes símbolos {valid_symbols}\nEn forma escrita son: un espacio en blanco, una equis mayúscula o una o mayúscula")
    else: #si no es de la proporción correcta lo señalamos
        print("Tu matriz debe ser 3x3, se forma con una lista con tres elementos, los cuales también son listas de 3 elementos")
matriz_tie = [["O","X","X"],["X","X","O"],["O","O","X"]]
matriz_win_x = [["X","O",""],["X","X","X"],["O","","O"]]
matriz_win_o = [["O","","X"],["","O","X"],["","X","O"]]
matriz_both_win = [["X","X","O"],["O","O","O"],["X","X","X"]]
matriz_out_range = [["","X","O","X"],["X","X","O","O"],["","X","","O"],["O","O","O","X"]]
matriz_not_valid_symbols = [["o","x","o"],["","",""],["o","x","x"]]
matriz_too_many_o = [["","",""],["","X",""],["O","O","O"]]
matriz_too_many_x = [["X","",""],["","X",""],["","O","X"]]
print(who_won_game(matriz_tie))
print(who_won_game(matriz_win_x))
print(who_won_game(matriz_win_o))
print(who_won_game(matriz_both_win))
print(who_won_game(matriz_out_range))
print(who_won_game(matriz_not_valid_symbols))
print(who_won_game(matriz_too_many_o))
print(who_won_game(matriz_too_many_x))