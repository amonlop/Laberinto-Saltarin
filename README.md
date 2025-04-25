# Laberinto-Saltarin
Antonia Montero López

Un laberinto saltarín se define como una grilla de m por n de números saltarines, una celda
inicial (en un círculo arriba), y una celda de destino (marcada “G”). En base al número
saltarín de cada celda, un movimiento corresponde a moverse esa cantidad exacta de
celdas ya sea de forma horizontal o vertical, en línea recta. No está permitido moverse de
manera diagonal ni cambiar de dirección a medio camino. Sólo se permiten movimientos en
que el número de celdas a mover no sobrepasa alguno de los límites del laberinto. El
objetivo del laberinto saltarín es encontrar el camino más corto, es decir, la menor cantidad
de movimientos desde la celda inicial hasta la celda de destino.

En la carpeta algoritmos se encuentran dos métodos de búsqueda: DFS y UCS.
En la carpeta interfaz_g se encuentra la implementación gráfica de los laberintos


Para ejecutar el programa, es necesario tener instalado python. Revisar el archivo requirements.txt para las librerías:
python main.py

En el archivo laberintos.txt se encuentran los laberintos de input.
