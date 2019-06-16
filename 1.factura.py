# Please, notice this program uses variables, strings and comments in Spanish. 

precio = 0      # precio del producto
aPrecios = []   # array de precios de cada producto
unidades = 0    # unidades del producto
aUnidades = []  # array de cada producto
producto = 0    # coste total producto * unidades
total = 0       # total precio
cantidad = 0    # total productos * unidades
comprando = True

def pideCifra(mensaje):
    cifra = False
    while not cifra:
        cifra = input(mensaje)
    
        try:
            if (mensaje == "precio: "):
                esNumero = float(cifra)
            else:
                esNumero = int(cifra)
            if esNumero >= 0:
                return cifra
            else:
                print("Tiene que ser un número positivo")
                cifra = False
        except ValueError:
            print("Tiene que ser un número")
            cifra = False

# pedimos precio y cantidad
while comprando:
    #precio = input("precio: ")
    precio = float(pideCifra("precio: "))
    #precio = float(precio)
    unidades = int(pideCifra("unidades: "))
    unidades = int(unidades)
    
    if precio == 0 or unidades == 0:
        comprando = False
    else:
        #precio = float(precio)
        #unidades = int(unidades)

        producto = precio * unidades
        total += producto
        cantidad += unidades
        
                
        aPrecios.append(precio)
        aUnidades.append(unidades)

# Salida de datos
for indice in range(0, len(aPrecios)):
    precio = aPrecios[indice]
    unidades = aUnidades[indice]
    
    print(precio , "€ - " , unidades , " unidades - " , precio*unidades , "€")



print("---------------------------\nTotal:\t{}\nUnidades:\t{}".format(round(total,2),cantidad))
