class Nodo:
    def __init__(self, fila, col, valor):
        self.fila = fila
        self.col = col
        self.valor = valor  
        self.vecinos = []  

    def agregar_vecino(self, nodo):
        self.vecinos.append(nodo)

    def __repr__(self):
        return f"Nodo({self.fila}, {self.col}, valor={self.valor})"
