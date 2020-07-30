Criptografía - Juego del Solitario

Se encomienda la siguiente tarea: el alumno debe construir una comunicación cifrada entre dos funciones
utilizando el algoritmo del solitario:
1.- Una primera función a la que enviemos una variable (que será una frase o cadena e texto) para que la
función lo cifre mediante el solitario. En programación existen diferentes tipos de variables: strings,
enteros, flotantes, booleanos, ... y en este caso la variable o parámetro que se le envía a la función es de
tipo String.
2.- Una segunda función que recoja el mensaje cifrado y lo descifre utilizando este mismo algoritmo.

En el código adjunto se especifica con comentarios todos los pasos a seguir. En resumen, he creado 3 diferentes funciones:
1) Solitario que es donde se desarrolla el algoritmo del solitario y que devuelve el stream para cifrar el mensaje original. Las cartas están barajadas utilizando la función shuffle
2) Cifrado donde se llama a la función solitario para obtener el stream con el que cifrar y donde se realiza la suma módulo 26 del mensaje original y el stream.
3) Descifrado en el que se llama a la función solitario para obtener el stream con el que cifrar y donde se realiza la resta módulo 26 entre el mensaje original y el stream

Por último, se llama a las funciones cifrado y descifrado y se muestran sus salidas. En el documento Salidas se muestran sus valores.

