Se nos presenta el siguiente reto a resolver:

En esta tarea debes desarrollar (en el lenguaje o lenguajes de programación que tú quieras) el siguiente
algoritmo:
Usted es un original empresario de Azkoitia, y tiene la brillante idea de abrir una tienda de la leche en la
Plaza del pueblo. Como es una persona muy prudente, desea que la leche que venderá sea
perfectamente natural y fresca, y por esa razón, va a traer unas sanísimas vacas de desde Tolosa.
Dispone de un camión con un cierto límite de peso, y un grupo de vacas disponibles para la venta. Cada
vaca puede tener un peso distinto, y producir una cantidad diferente de leche al día.
Debes elegir qué vacas comprar y llevar en su camión, de modo que pueda maximizar la producción de
leche, observando el límite de peso del camión.
1.- Para este propósito tienes que definir las siguientes entradas:
Entrada: Número total de vacas en la zona de Tolosa que están a la venta.
Entrada: Peso total que el camión puede llevar.
Entrada: Lista de pesos de las vacas.
Entrada: Lista de la producción de leche por vaca, en litros por día.
2.- El algoritmo que programes tiene que calcular la siguiente salida:
Salida: Cantidad máxima de producción de leche se puede obtener.

La primera opción que se me ha ocurrido es el de reducir el número de casos a comprobar reordenando el array baasándome en el array con los datos de eficiencia en litros/(kg*día).
Para no dejarme ninguna vaca cuya eficiencia sea menor pero que resulta que entraría en el camión, el algoritmo comprobará todas las vacas ordenadas por orden de mayor a menor 
eficiencia. Sin embargo, esta solución presenta varios casos en los que el resultado no es el óptimo.

Por ello, decidí ponerme a investigar sobre algoritmia en la siguiente bibliografía (Aditya Y. Bhargava "Algoritmos. Una guía ilustrada para programadores y curiosos" y G. Brassard and
P. Bratley "Fundamentos de algoritmia") y di con el algoritmo de recursividad y la búsqueda dinámica. El primero de ellos (recursividad) aunque encuentra siempre la solución óptima,
presenta una complejidad similar a la de la fuerza bruta O(N^2). Sin embargo, la búsqueda dinámica, que reduce un problema complejo a varios subproblemas más sencillos y utiliza los 
resultados de estos subproblemas para calcular el resultado final, presenta una complejidad O(MxN) lineal y mucho menor que las anteriores donde N es el número de vacas y M el límite de
peso. 

El algoritmo que se basa en crear una matriz N x M donde N es el número de vacas y M el límite de peso donde cada celda representa la producción óptima de leche por día de cada
vaca. Es imprescidible verificar que nunca se supera el límite de peso de las vacas seleccionadas (ningún código existente en internet lo tiene en cuenta ni calcula correctamente
el resultado). El código que yo presento en el archivo Tarea_22.py calcula correctamente la solución y comprueba todos los límites. Al código le he añadido comentarios para
que cada paso se entienda perfectamente.
