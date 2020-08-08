# Inicializar cadenas de ADN
cadena1 = ['A','T','G','T','C','T','T','C','C','T','C','G','A']
cadena2 = ['T','G','C','T','T','C','C','T','A','T','G','A','C']

# Inicializar matriz de coincidencias
matriz = [[0 for x in range(0,len(cadena1)+1)] for y in range(0,len(cadena2)+1)]
mayor_coincidencia = [[0 for x in range(0,len(cadena1)+1)] for y in range(0,len(cadena2)+1)]
mayor = []
cadena_larga = [] # Va almacenando el valor n-1 más largo de caracteres

# Rellenar matriz
for i in range(1,len(cadena2)+1):
    matriz[0][i] = cadena2[i-1]
for j in range(1,len(cadena1)+1):
    matriz[j][0] = cadena1[j-1]

for i in range(1,len(cadena2)+1):
    for j in range(1,len(cadena1)+1):
        if matriz[0][i] == matriz[j][0]:
            matriz[j][i] = 1
        else:
            matriz[j][i] = 0

# Buscamos coincidencias entre letras adyacentes en la matriz. Comprobamos la longitud de las diagonales con valor 1 
for i in range(1,len(cadena2)):
    a=i
    for j in range(1,len(cadena1)):
        coincidencia = []
        if matriz[a][j] == 1:
            while matriz[i][j] == 1:
                coincidencia = coincidencia + [matriz[0][j]]          
                i = i+1
                j = j+1
                if i > len(cadena2) or j > len(cadena1): # Comprobamos que los índices no se salen de la matriz
                    break
            if len(mayor) >= len(coincidencia):
                mayor = mayor
            else:
                mayor = coincidencia

print(mayor)