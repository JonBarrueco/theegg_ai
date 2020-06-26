En esta tarea tenemos que encontrar la fracción irreducible de un número comprendido entre [0.0001 – 0.9999]. Para pasarlo a fracción, multiplicamos el número por 10,000 y 
lo dividimos entre 10,000. La fracción irreducible va a estar determinada por los divisores de 10,000 que no sean múltiplos de ningún otro número aparte de 1 y él mismo. 
En el caso de 10,000 estos dos divisores son 2 y 5. También podría ser 4, 10, etc pero son múltiplos de 2 y de 2 y 5, respectivamente. De esta forma, al programa ya le 
proporcionamos los valores con los que hallar la fracción irreducible. Otra forma que requiere algo más de complejidad computacional es chequear todos los números entre el 1
y el número proporcionado por el usuario multiplicado por 10,000.

El diagrama de flujo de la solución se presenta en el archivo “Diagrama_Flujo.png”. El programa funciona de la siguiente manera: primero se pide al usuario que introduzca por
teclado un número comprendido entre [0.0001 – 0.9999]. Después se multiplica este número por 10,000 y se obtiene el numerador. El denominador, como hemos dicho más arriba es 
10,000. Ahora, mientras tanto el numerador como el denominador sean divisibles por 2, el programa va reduciendo la fracción entre 2. Cuando compruebe que uno de los dos valores
no es entero, saldrá de este while y pasará a un mismo bucle while pero, esta vez, dividiendo entre 5. Cuando el numerador o denominador ya no sea un número entero divisible entre
5, ya tenemos la fracción irreducible del número leído por teclado. Lo último que hacemos es mostrar este número.
