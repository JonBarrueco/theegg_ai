
# Inicializamos los parámetros de entrada
numero_frases = 3
frase_1 ="this is a test"
frase_2 = "foobar"
frase_3 ="all your base"
frases = []

# Función que itera hasta el número total de frases, llama a la función invertir_orden y muestra en pantalla el resultado
def escoger_palabra(numero_palabras,frase_1,frase_2,frase_3):
    frases = [frase_1,frase_2,frase_3]
    for i in range(0,len(frases)):
        palabra_invertida = invertir_orden(frases[i])
        print("Case ",i,": ",palabra_invertida)

def invertir_orden(palabra):
    palabra = palabra.split()
    palabra.reverse()
    palabra = " ".join(palabra)
    return palabra

escoger_palabra(numero_frases,frase_1,frase_2,frase_3)