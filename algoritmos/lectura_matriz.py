from algoritmos.Nodo import Nodo
from algoritmos.b_costo_uniforme import *
from algoritmos.b_profundidad import *
from interfaz_g import pantalla

def construir_grafo(nombre_archivo):
    #laberintos = []

    with open(nombre_archivo, "r") as archivo:
        i = 1
        while True:
            
            linea = archivo.readline().strip()
            
            #lectura termina cuando encuentra un 0
            if linea == "0":
                break
            
            # Leer dimensiones y posiciones
            m, n, inicio_fila, inicio_col, destino_fila, destino_col = map(int, linea.split())

            # matriz de nodos
            matriz = []
            for fila in range(m):
                #se crea una lista de nodos y se añaden a la matriz
                linea2= archivo.readline().strip().split()
                valores = list(map(int, linea2))
                if len(valores) != n:
                    raise ValueError(f"Error en la lectura: se esperaban {n} columnas, pero se obtuvo {len(valores)}")

                fila_nodos = [Nodo(fila, col, valores[col]) for col in range(n)]
                matriz.append(fila_nodos)

            # Generar conexiones (movimientos válidos)  agregar a nodos vecinos
            for fila in range(m):
                for col in range(n):
                    nodo = matriz[fila][col]
                    #print("(",nodo.fila, nodo.col, nodo.valor, ")")
                    salto = nodo.valor

                    # Movimientos permitidos: izquierda, derecha, arriba, abajo
                    posibles_movimientos = [
                        (fila + salto, col), (fila - salto, col),  # Vertical
                        (fila, col + salto), (fila, col - salto)   # Horizontal
                    ]
                    
                    #se añaden solo los vecinos dentro del rango de movimiento posible
                    for nueva_fila, nueva_col in posibles_movimientos:
                        if 0 <= nueva_fila < m and 0 <= nueva_col < n:
                            vecino = matriz[nueva_fila][nueva_col]
                            #print("vecino de ", "(",nodo.fila, nodo.col, nodo.valor, ") es: ", "(",vecino.fila, vecino.col, vecino.valor, ")")
                            nodo.agregar_vecino(vecino)

            nodo_inicio = matriz[inicio_fila][inicio_col]
            nodo_destino = matriz[destino_fila][destino_col]
            
            costo_camino_ucs, camino_ucs = busqueda_costo_uniforme(nodo_inicio, nodo_destino)
            costo_camino_dfs, camino_dfs = busqueda_profundidad(nodo_inicio, nodo_destino)
            print("Laberinto #",i)
            print("costo camino ucs: ", costo_camino_ucs, "camino_ucs: ", camino_ucs)
            print("costo camino dfs: ", costo_camino_dfs, "camino_dfs: ", camino_dfs)
            i += 1
            """ if camino:
                print(camino)
                #pantalla.iniciar_pantalla()
            else:
                print("No hay solución") """
  