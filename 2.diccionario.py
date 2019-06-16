# Please, notice this program uses variables, strings and comments in Spanish. 

miTexto = "tres palabras para ti"
frecuencias = dict()

for caracter in miTexto:
    if caracter in frecuencias:

        frecuencias[caracter] += 1
    else:
        frecuencias[caracter] = 1

for letra in frecuencias.keys():
    
    print(letra, "-", frecuencias[letra])