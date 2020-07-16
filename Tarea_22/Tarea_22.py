n = 6
camion = 700
peso = [360, 250, 400, 180, 50, 90]
produccion = [40, 35, 43, 28, 12, 13]

# Variable que almacena la máxima producción de leche por día
maximo = 0

# Defino matriz para la programación dinámica
celda = [[0 for x in range(camion+1)] for y in range(n+1)]
pesos = [[0 for x in range(camion+1)] for y in range(n+1)]

# Debido a la complejidad de evaluar todas las alternativas O(2^n), se utiliza programación dinámica con una complejidad O(n)

# Primero, inicializo la columna en la posicion 0 con el valor 0. Esto es debido a que esta columna en la matriz no tiene que tener valores asignados
# Segundo, como la primera fila siempre se va a comprobar sólo una vaca, compruebo que su peso no supera el límite del peso del camión y, si es así,
# la añado a la matriz
for j in range(1,camion+1):
    if peso[0] <= camion: 
        celda[1][j] = produccion[0]
        pesos[1][j] = peso[0]

# Para el resto de las celdas de la matriz, utilizo la fórmula del máximo valor. Hay que comprobar que no estamos fuera de índice en la matriz y
# que el valor máximo no supera el límite del camión
for i in range(2,n+1):
    for j in range(1,camion+1):
        if j < peso[i-1]:
            celda[i][j]=celda[i-1][j]
            pesos[i][j]=pesos[i-1][j]
        elif pesos[i-1][j-peso[i-1]] + peso[i-1] <= camion:    
            celda[i][j] = max([celda[i-1][j], celda[i-1][j-peso[i-1]] + produccion[i-1]])
            pesos[i][j] = max([pesos[i-1][j], pesos[i-1][j-peso[i-1]] + peso[i-1]])
        else:
            celda[i][j] = 0

may=-1
V=0

for i in range(0,n+1):
    for j in range(0,camion+1):
    	if celda[i][j]>may:
    		may=celda[i][j]
    		V=celda[i][j]

print("La produccion total es:", V)