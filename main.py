from algoritmos import lectura_matriz
from interfaz_g import pantalla

if __name__ == "__main__":
    nombre_archivo = "laberintos.txt"
    laberintos = lectura_matriz.construir_grafo(nombre_archivo)
    
    pantalla.iniciar_pantalla(laberintos)
