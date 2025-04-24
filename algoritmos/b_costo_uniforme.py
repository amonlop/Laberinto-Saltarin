import heapq
from algoritmos.Nodo import Nodo

#en este problema, el costo de moverse entre nodos es 1
#considera el uso de priority_queue
def busqueda_costo_uniforme(inicio, destino):
    #se guarda un historial de coordenadas para pygame
    #(costo acumulado, nodo actual, historial del camino)
    # el id(inicio) se ignora, solo sirve para que heap ordene por costo
    cola_prioridad = [(0, id(inicio), inicio, [])] 
    
    #Dictionary to store the cost of the shortest path to each node
    visitados = {} 

    while cola_prioridad:
        #min-heap, se extrae el nodo con menor costo primero
        costo_acumulado, _id_, nodo_actual, camino = heapq.heappop(cola_prioridad)

        #si es que ya se visitó este nodo con menor costo, continue
        if nodo_actual in visitados and costo_acumulado >= visitados[nodo_actual]:
            continue

        # costo mínimo hasta el nodo y se añade al camino
        visitados[nodo_actual] = costo_acumulado
        camino = camino + [(nodo_actual.fila, nodo_actual.col)]
        
        #If we reached the goal, return the total cost and the path
        if nodo_actual == destino:
            return costo_acumulado, camino

        # expansión de vecinos
        for vecino in nodo_actual.vecinos:
            nuevo_costo = costo_acumulado + 1  # todos los movimientos tiensen coste 1
            heapq.heappush(cola_prioridad, (nuevo_costo, id(vecino), vecino, camino))

    return None, None  # si no hay solución entonces null
