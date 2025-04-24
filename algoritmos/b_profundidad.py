
#busqueda en profundidad recursiva
def dfs(nodo_actual, nodo_destino, visitados, camino, pasos):
    #se añade la ruta hasta ahora
    camino.append((nodo_actual.fila, nodo_actual.col))

    #verifica si se llega al destino
    if nodo_actual == nodo_destino:
        return pasos, camino

    visitados.add(nodo_actual)

    for vecino in nodo_actual.vecinos:
        if vecino not in visitados:
            #dfs recursivo
            #camino[:] crea una copia del camino, de forma que no se modifique la misma lista siempre.
            pasos_ac, camino_ac = dfs(vecino, nodo_destino, visitados, camino[:], pasos + 1)
            
            #los pasos indican q se encontró un camino válido
            if pasos_ac is not None:
                return pasos_ac, camino_ac
            
     #si no hay solución o más camino
    return None, None

def busqueda_profundidad(nodo_inicio, nodo_destino):
    #nodo_inicial, nodo_destino, un set de nodos visitados, una lista de camino, num_pasos
    #el set no permite elementos duplicados
    return dfs(nodo_inicio, nodo_destino, set(), [], 0)
