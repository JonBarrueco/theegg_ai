# Programa que convierte un número decimal a binario. Supondremos que el número se refiere a la componente de luminancia de un LED en formato 8 bits

numero_decimal = 36 # Valor decimal a convertir

if numero_decimal > 255: # Comprobamos que el valor decimal no supera el límite de 8 bits
    print("El número ha de estar comprendido entre 0-255")

numero = 128 # Inicializamos el valor más alto en base 2: 2^7

valor = list(range(1,9)) # Inicializamos la lista en la que guardar el número en binario

def convertidor_digital_analogico(numero_decimal):

    for i in range(0,8): # Vamos comprobando si el valor en base dos es mayor o igual al número decimal
        limite = 2**(7-i)
        if numero_decimal >= limite:
            valor[i] = 1
            numero_decimal = numero_decimal - limite

        else:
            valor[i] = 0

    return valor

numero_binario = convertidor_digital_analogico(numero_decimal)

print("El valor digital de",numero_decimal,"es: ",numero_binario)