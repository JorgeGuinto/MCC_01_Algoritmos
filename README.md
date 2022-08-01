# Repositorio de las actividades de programación de de la materia de Análisis y diseño de algoritmos

## * Actividad 02
### Fibonacci
Programa cuatro algoritmos que calculen el enésimo número de Fibonacci con las siguientes estrategias: (Anexa los códigos a tu reporte como texto)
- Usando un algoritmo iterativo
- Usando un algoritmo recurrente
- Usando la formula cerrada
- Usando divide y vencerás (este requiere investigar)


## * Actividad 03
### Conteo de Inversiones
- Programa el algoritmo de conteo de inversiones y calcula con el número de inversiones en el arreglo de enteros de “IntegerArray.txt”. Reporta tu código y resultado.
- Programa el algoritmo de MergeSort y ordena el arreglo de enteros en “IntegerArray.txt”. Reporta tu código.


## * Actividad 04
### QuickSort

En la clase demostramos de manera analítica el tiempo asintótico del algoritmo QuickSort. En la práctica suele ser muy complejo hacer este tipo de análisis en algoritmos aleatorios, por lo que solemos crear pruebas de Monte Carlo y sacar estadísticas de ellas. En esta actividad haremos justo eso para el algoritmo de QuickSort.

1.	Programa el algoritmo de QuickSort con pivote aleatorio
2.	Programa el algoritmo de Permutación aleatoria de Fisher-Yates
3.	Genera arreglos de tamaño n=10, 100, 200, 500, 1000, 2000, 5000, 10000. De manera que cada uno de estos arreglos contenga los números naturales desde 1 hasta n.
4.	Para cada uno de los arreglos anteriores realiza el siguiente proceso 50 veces:
a.	Permuta de manera aleatoria el arreglo
b.	Luego ordénalo con Quicksort, mide el tiempo que tarda este proceso y guárdalo.
5.	Grafica los resultados, donde el eje “x” sea el tamaño del arreglo y el eje “y” sea el tiempo medio que tardó el algoritmo de Quicksort en ordenarlo. 
6.	Reporta tu código y tu experimentación.
7.	Escribe tus conclusiones de esta manera de estudiar los algoritmos.
8.	Guarda tu reporte en formato PDF y somételo en la plataforma.

## * Actividad 05
### Búsqueda a profundidad (DFS) y Dijkstra
1. Codifica el algoritmo de búsqueda a profundidad. En el archivo “Grafo_no_conexo.txt”, está la descripción de un grafo simple no conexo. Usa el algoritmo de búsqueda en profundidad para encontrar los subgrafos conexos. Reporta los vértices de cada subgrafo conexo y tu código. Anexo imagen del grafo en cuestión:

2. Codifica el algoritmo de Dijkstra. En el archivo “Grafo_ponderado.txt”, encontraras la descripción de un dígrafo. Usa el algoritmo que codificaste, para encontrar la ruta mínima del nodo 0 al nodo 14. Reporta tu resultado y tu código. Anexo imagen del grafo en cuestión.

## * Actividad 06 (Extra)
1.	Implementa el algoritmo del par de puntos 2D más cercano
2.	Crea una simulación creando puntos aleatorios en 2D calcula los puntos más cercanos y dibuja una línea entre ellos.
3.	Crea un reporte con tu código y tus resultados.
4.	Sube tu reporte.

## * Actividad 07
### Algoritmo de Huffman

1. Codifica el algoritmo de Huffman que genere los códigos, valida con los datos anteriores.

## * Actividad 08
### Backtracking

1. Usando la técnica de Backtracking, codifica un algoritmo para encontrar la solución de un Sodoku en su variante regular. Resuelve los siguientes Sodokus. Reporta tu código y la solución de los ejercicios.
2. Opcional (Backtracking Backpack) Codifica un algoritmo usando la técnica de Ramificación y Poda que resuelva el problema de la mochila. Resuelve el siguiente ejemplo donde la capacidad de la mochila es de 101. Reporta código y la solución al ejercicio.
	    1	2	3	4	5	6	7	8	9
Valor	79	32	47	18	26	85	33	40	45
Peso	85	26	48	21	22	95	43	45	55


## * Actividad 09
### Dynamic Programming

1. Usa programación dinámica para resolver el problema de encontrar el máximo conjunto independiente con mayor peso. Usa el archivo MWIS.txt para obtener los datos, cada dato es el peso de un vértice en un grafo camino. Contesta los siguiente: ¿Cuáles de los vértices 1, 2, 3, 4, 17, 117, 517, y 997 forman parte de la solución óptima?

2. Usa programación dinámica para resolver el siguiente problema de la mochila. Suponga una capacidad máxima de 140 unidades. ¿Cuál es el valor óptimo de la mochila?, ¿Cuáles son los objetos que debemos tomar? 

	1	2	3	4	5	6	7	8	9	10
Valor	79	32	47	18	26	85	33	40	45	59
Peso	85	26	48	21	22	95	43	45	55	52


## * Actividad 10
### Dynamic Programming

1. Usa programación dinámica para resolver el problema de cortar la cuerda de la siguiente tabla. Encuentra para la cuerda de largo 11 cual sería el precio máximo para venderla, así como la descomposición óptima. Reporta tu código.
largo	1	2	3	4	5	6	7	8	9	10	11
precio	1	4	10	12	15	20	21	32	31	41	51

2. Usa programación dinámica para encontrar la parentización óptima de la sucesión de matrices multiplicándose p=[5, 10, 3, 12, 5, 50, 6]. Entrega el mínimo de multiplicaciones escalares con el que se puede ejecutar dicha operación y explicita la parentización usada. Reporta tu código.

3. Usando el algoritmo de Needleman-Wunch, alinea las siguientes secuencias. Utiliza las mismas penalizaciones que en clase. Reporta tu código y la penalización de la alineación óptima.

X = CGATGCTAGCGTATCGTAGTCTATCGTAC
Y = ACGATGCTAGCGTTTCGTATCATCGTA