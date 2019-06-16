# a mejorar -> tienen que tener la misma cantidad de cada elemento (por ejemplo, amar y mar no son anagramas)
# posible solución = sumar los valores numéricos de los caracteres, y si coinciden sabremos que es un anagrama
# otra posible solución es utilizar la función count()

def isAnagram(p1,p2):
    
    if len(p1) != len(p2): # si no tienen la misma cantidad de caracteres, ya sabemos que no es un anagrama y no necesitamos seguir con la función
        return False
    
    listaComparacionLetras = []
    palabra1 = list(dict.fromkeys(p1)) # convertimos la primera palabra en un array, eliminando los elementos que se repiten
    palabra2 = list(dict.fromkeys(p2)) # convertimos la segunda palabra en un array, eliminando los elementos que se repiten
    
    for caracter1 in palabra1:
        esTrue = 'nope' # declaramos una variable que nos ayudará a saber si hemos encontrado una coincidencia
        for caracter2 in palabra2:         
            if caracter1 == caracter2:
                #listaComparacionLetras.append(True) # si existe una coincidencia, añadimos un True al array listaComparacionLetras
                esTrue = 'yess'
                
                palabra2.remove(caracter1) # también borramos esa letra del array de la segunda palabra
        if esTrue != 'yess': 
            return False # si no ha habido coincidencia al terminar el bucle, devolvemos False: no existe un anagrama
    if len(palabra2) > 0:
        # si quedan letras sin eliminar del array de la segunda palabra significa que hay caracteres que no han coincidido,
        # devolvemos False: no existe un anagrama        
        return False 
    else:
        return True
