#Definimos variables
multiplier=10000

#Solicitamos el número al usuario
num = float(input("Ingresa un número: "))

#Lo multiplicamos por 10,000 para obtener el numerador
numerador = int(num * multiplier)
denominador = 10000

#Comprobamos si el número es divisible entre 2. Si lo es, seguimos dividiendo entre 2. Si no, pasamos a dividir entre 5
numerador2 = numerador
denominador2 = denominador

while numerador2 % 2 == 0 and denominador2 % 2 ==0:
        
    numerador2 = numerador / 2
    denominador2 = denominador / 2
    numerador = numerador2
    denominador = denominador2

#Comprobamos si el número es divisible entre 5. Si lo es, seguimos dividiendo entre 5. Si no, printeamos la solución
numerador3 = numerador2  
denominador3 = denominador2  
   
while numerador3 % 5 == 0 and denominador3 % 5 == 0:
        
    numerador3 = numerador2 / 5
    denominador3 = denominador2 / 5
    numerador2 = numerador3
    denominador2 = denominador3

# Pasamos de float a enteros y printeamos la mínima raíz
numerador3 = int(numerador3)
denominador3 = int(denominador3)
print('La mínima raíz es:' + str(numerador3) + '/' + str(denominador3))
