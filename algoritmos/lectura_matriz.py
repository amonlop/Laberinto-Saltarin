from algoritmos.Nodo import Nodo
from algoritmos.b_costo_uniforme import busqueda_costo_uniforme
from algoritmos.b_profundidad import busqueda_profundidad
from interfaz_g import pantalla

def construir_grafo(nombre_archivo):
    #laberintos = []

    with open(nombre_archivo, "r") as archivo:
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
                print(linea2)
                valores = list(map(int, linea2))
                if len(valores) != n:
                    raise ValueError(f"Error en la lectura: se esperaban {n} columnas, pero se obtuvo {len(valores)}")

                fila_nodos = [Nodo(fila, col, valores[col]) for col in range(n)]
                matriz.append(fila_nodos)

            # Generar conexiones (movimientos válidos)  agregar a nodos vecinos
            for fila in range(m):
                for col in range(n):
                    nodo = matriz[fila][col]
                    salto = nodo.valor

                    # Movimientos permitidos: izquierda, derecha, arriba, abajo
                    posibles_movimientos = [
                        (fila + salto, col), (fila - salto, col),  # Vertical
                        (fila, col + salto), (fila, col - salto)   # Horizontal
                    ]
                    
                    #se añaden solo los vecinos dentro del rango de movimiento posible
                    for nueva_fila, nueva_col in posibles_movimientos:
                        if 0 <= nueva_fila < m and 0 <= nueva_col < n:
                            nodo.agregar_vecino(matriz[nueva_fila][nueva_col])

            nodo_inicio = matriz[inicio_fila][inicio_col]
            nodo_destino = matriz[destino_fila][destino_col]

            camino_ucs = busqueda_costo_uniforme(nodo_inicio, nodo_destino)
            camino_dfs = busqueda_profundidad(nodo_inicio, nodo_destino)
            
            camino = min(camino_dfs, camino_ucs)
            
            if camino:
                print(camino)
                #pantalla.iniciar_pantalla(matriz, camino, nodo_inicio, nodo_destino)
            else:
                print("No hay solución")
                
