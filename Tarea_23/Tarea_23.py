import random
# Definir la frase a enviar y encriptar
frase = "DO NOT USE PC"


# La primera parte consiste en crear la baraja de póker: el número 53 corrsponde al comodín A y el 54 al B

#baraja = list(range(1,55))

# Barajamos la baraja utilizando el método shuffle
#random.shuffle(baraja)

# Algoritmo Solitario 
def solitario():

# Generamos stream mediante Solitario 

# Paso 1: Buscamos el comodín A que equivale a la carta 53 de nuestra baraja y lo intercambiamos con la carta de debajo suyo
# Hay que checkear con sentencia if si A está en última posición para pasarlo al principio de la baraja   
    #print(baraja)
    baraja = [18, 8, 53, 17, 48, 24, 11, 35, 22, 27, 10, 16, 51, 23, 47, 2, 40, 44, 43, 19, 49, 6, 3, 1, 25, 12, 38, 54, 20, 21, 52, 45, 37, 26, 42, 32, 39, 14, 4, 50, 28, 5, 9, 29, 36, 33, 46, 13, 15, 34, 41, 30, 31, 7]

    baraja2 = baraja
    posicion_A = baraja2.index(53)

    if posicion_A == 53:

        baraja2[posicion_A] = baraja2[0]
        baraja2[0] = 53
    else:
        baraja2[posicion_A] = baraja2[posicion_A+1]
        baraja2[posicion_A+1] = 53

    #print(baraja2)

# Paso 2: Buscamos el comodín B que equivale a la carta 54 de nuestra baraja y lo movemos debajo de la segunda carta
# Hay que checkear con sentencia if si B está en penúltima o última posición para pasarlo al principio de la baraja
    posicion_B = baraja2.index(54)
    
    if posicion_B == 52: #El comodín se desplaza al principio de la baraja

        baraja2[posicion_B] = baraja2[posicion_B+1]
        baraja2[posicion_B+1] = baraja2[0]
        baraja2[0] = 54

    elif posicion_B == 53: # El comodín se desplaza a la segunda posición de la baraja

        baraja2[posicion_B] = baraja2[0]
        baraja2[0] = baraja2[1]
        baraja2[1] = 54

    else:
    
        baraja2[posicion_B] = baraja2[posicion_B+1]
        baraja2[posicion_B+1] = baraja2[posicion_B+2]
        baraja2[posicion_B+2] = 54

    #print(baraja2)

# Paso 3: Corta la baraja en tres, intercambiando las cartas antes del primer comodín con las cartas que están detrás del segundo comodín.

    posicion_A = baraja2.index(53)
    posicion_B = baraja2.index(54)

    if posicion_A < posicion_B: # El comodín A está antes que el comodín B

        baraja_corte_1 = baraja2[0:posicion_A]
        baraja_corte_2 = baraja2[posicion_A:(posicion_B+1)]
        baraja_corte_3 = baraja2[(posicion_B+1):54]

        

    else: # El comodín B está antes que el comodín A

        baraja_corte_1 = baraja2[0:posicion_B]
        baraja_corte_2 = baraja2[posicion_B:(posicion_A+1)]
        baraja_corte_3 = baraja2[(posicion_A+1):54]

    baraja_corte = baraja_corte_3+baraja_corte_2+baraja_corte_1

    #print(baraja_corte)
# Paso 4: Mira la última carta. Conviértela a un número de 1 a 53 (usa el orden normal: tréboles, diamantes, corazones y picas. Si la carta es un trébol, toma su número tal cual. Si es de diamantes, suma 13 a su valor. Si es de corazones, súmale 26. Si es de picas, súmale 39. Ambos comodines suman 53). Cuenta el valor valor obtenido empezando en la carta superior (normamente yo cuento de 1 a 13 una y otra vez, si es preciso; es más fácil que contar hasta un número alto de forma secuencial). Corta tras esa carta, dejando la última carta de la baraja a final.

    ultima_carta = baraja_corte[53]

    baraja_corte2_1 = baraja_corte[0:ultima_carta]
    baraja_corte2_2 = baraja_corte[ultima_carta:53]
    
    barajada = baraja_corte2_2+baraja_corte2_1+[ultima_carta]

    #print(barajada)

    return barajada

# Definimos función que tiene como parámetro la cadena de caracteres a cifrar y devuelve el mensaje cifrado
def cifrado(frase):

# Paso 1: Toma el mensaje cifrado y divídelo en grupos de cinco letras (ya debería estar en ese formato)
# Quitamos los espacios en blanco de la cadena de caracteres

    frase_sinesp = frase.replace(" ","")

# Paso 2: Usa Solitario para generar la ristra. Si el receptor usa la misma clave que el transmisor, la ristra será la misma.
# Definimos función que tiene como parámetro el mensaje cifrado y devuelve el mensaje original
    alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    stream = list(range(1,11))
    stream_alfabeto = list(range(1,11))
    suma = list(range(1,11))
    mensaje_original = list(range(1,11))

    for i in range(0, 10):
        baraja_solitario = solitario()

# Mira la primera carta. Conviértela en un número de 1 a 53, de la misma manera que en el paso 4. Cuenta esas cartas (la primera carta es la uno)    
        while baraja_solitario[0] == 53 or baraja_solitario[0] == 54: #Comprobamos que la primera carta no es un comodín
            baraja_solitario = solitario()
    
        contar = baraja_solitario[0]
        #numero = baraja_solitario[contar-1]

        if contar > 26:
            contar = contar - 26 #Necesitamos que llegue a 26
        else:
            contar = contar
        stream[i] = contar
        

# Paso 3: Convertimos el mensaje original de letras a números, A=1, B=2, etc 

        mensaje_original[i] = alfabeto.index(frase_sinesp[i])


# Sumamos el mensaje original y el stream de Solitario, módulo 26.

        suma[i] = mensaje_original[i] + stream[i]
        if suma[i] > 26:
            suma[i] = suma[i]-26
        else:
            suma[i] = suma[i]
        stream_alfabeto[i] = alfabeto[suma[i]-1]

    #print(stream_alfabeto)
    #print(suma)
    return suma,stream_alfabeto


def descifrado(suma):

# Paso 1 Usa Solitario para generar la ristra. Si el receptor usa la misma clave que el transmisor, la ristra será la misma.

    alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    stream = list(range(1,11))
    stream_alfabeto = list(range(1,11))
    resta = list(range(1,11))

    for i in range(0, 10):
        baraja_solitario = solitario()

# Mira la primera carta. Conviértela en un número de 1 a 53, de la misma manera que en el paso 4. Cuenta esas cartas (la primera carta es la uno)    
        while baraja_solitario[0] == 53 or baraja_solitario[0] == 54: #Comprobamos que la primera carta no es un comodín
            baraja_solitario = solitario()

        contar = baraja_solitario[0]
        #numero = baraja_solitario[contar-1]
        if contar > 26:
            contar = contar - 26 #Necesitamos que llegue a 26
        else:
            contar = contar
        stream[i] = contar
        


# Restamos el mensaje original y el stream de Solitario, módulo 26.

        resta[i] = suma[i] - stream[i]
        if resta[i] < 0:
            resta[i] = resta[i]+ 26
        else:
            resta[i] = resta[i]
        stream_alfabeto[i] = alfabeto[resta[i]]

    #print(stream_alfabeto)
    #print(resta)

    return stream_alfabeto
# Llamamos a las dos funciones para cifrar y descifrar el mensaje y mostramos por pantalla el mensaje cifrado y descifrado

suma,mensaje_cifrado = cifrado(frase)

print(mensaje_cifrado)

mensaje_descifrado = descifrado(suma)

print("El mensaje original es:",frase)

print("El mensaje cifrado es:",mensaje_cifrado)

print("El mensaje descifrado es:", mensaje_descifrado)