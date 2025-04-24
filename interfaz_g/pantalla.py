import pygame
import os
from interfaz_g.Colores import *

# Configuración
MAX_ANCHO = 900
MAX_ALTO = 500
TIEMPO_SALTO = 800

def render_texto_footer(pantalla, texto, ancho_pantalla, alto_footer):
    max_tamano_fuente = alto_footer - 30
    for tamano in range(max_tamano_fuente, 5, -1):
        fuente_footer = pygame.font.Font(None, tamano)
        texto_render = fuente_footer.render(texto, True, (255, 255, 255))
        if texto_render.get_width() <= ancho_pantalla - 20:
            break
    texto_rect = texto_render.get_rect(center=(ancho_pantalla // 2, pantalla.get_height() - alto_footer // 2))
    pantalla.blit(texto_render, texto_rect)

def centrar_ventana():
    os.environ['SDL_VIDEO_CENTERED'] = '1'

def iniciar_pantalla(laberintos):
    pygame.init()
    corriendo = True
    index_laberinto = 0

    while corriendo and index_laberinto < len(laberintos):
        matriz, camino, num_pasos, nodo_inicio, nodo_destino, numero_laberinto = laberintos[index_laberinto]
        filas, cols = len(matriz), len(matriz[0])

        # espacio de footer
        ESPACIO_TEXTO = 50

        #tamaño de celda dinamico
        tamano_celda = min(MAX_ANCHO // cols, (MAX_ALTO - ESPACIO_TEXTO) // filas)
        ancho_pantalla = tamano_celda * cols
        alto_pantalla = tamano_celda * filas + ESPACIO_TEXTO

        fuente_tamano = max(16, tamano_celda // 2)
        fuente = pygame.font.Font(None, fuente_tamano)

        centrar_ventana()
        pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
        pygame.display.set_caption(f"Laberinto #{numero_laberinto}")

        recorrido_index = 0

        print(f"Laberinto #{numero_laberinto}")
        if camino:
            print(num_pasos)
        else:
            print("No hay solución")
            index_laberinto += 1
            continue
        
        # Animación paso a paso
        while recorrido_index < len(camino):
            pantalla.fill(COLOR_FONDO)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    corriendo = False

            # laberinto
            for fila in range(filas):
                for col in range(cols):
                    rect = pygame.Rect(col * tamano_celda, fila * tamano_celda, tamano_celda, tamano_celda)
                    
                    if (fila, col) == (nodo_inicio.fila, nodo_inicio.col) or (fila, col) in camino[1:recorrido_index + 1]:
                        pygame.draw.rect(pantalla, COLOR_CAMINO, rect)
                        if (fila, col) == (nodo_destino.fila, nodo_destino.col):
                            pygame.draw.rect(pantalla, COLOR_CASILLA_OBJETIVO, rect)
                    else:
                        pygame.draw.rect(pantalla, COLOR_CELDA, rect)

                    if (fila, col) == (nodo_destino.fila, nodo_destino.col):
                        texto = fuente.render("G", True, COLOR_LETRA_OBJETIVO)
                    else:
                        valor = str(matriz[fila][col].valor)
                        texto = fuente.render(valor, True, COLOR_TEXTO)

                    texto_rect = texto.get_rect(center=rect.center)
                    pantalla.blit(texto, texto_rect)

            # casilla inicio
            inicio_x = nodo_inicio.col * tamano_celda + tamano_celda // 2
            inicio_y = nodo_inicio.fila * tamano_celda + tamano_celda // 2
            pygame.draw.circle(pantalla, COLOR_CIRCULO, (inicio_x, inicio_y), tamano_celda // 3, 3)

            # casilla final
            texto_g = fuente.render("G", True, COLOR_LETRA_OBJETIVO)
            objetivo_rect = texto_g.get_rect(center=(
                nodo_destino.col * tamano_celda + tamano_celda // 2,
                nodo_destino.fila * tamano_celda + tamano_celda // 2
            ))
            pantalla.blit(texto_g, objetivo_rect)

            # footer
            if recorrido_index < num_pasos:
                pasos_actuales = recorrido_index if recorrido_index > 0 else 0
                render_texto_footer(pantalla, f"Número de pasos: {pasos_actuales}", ancho_pantalla, alto_footer=55)
            else :
                render_texto_footer(pantalla, f"Número de pasos: {num_pasos}. Presiona cualquier tecla", ancho_pantalla, alto_footer=55)

            pygame.display.flip()
            pygame.time.delay(TIEMPO_SALTO)
            recorrido_index += 1

        # Esperar tecla para avanzar
        esperando = True
        while esperando and corriendo:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    corriendo = False
                elif evento.type == pygame.KEYDOWN or evento.type == pygame.MOUSEBUTTONDOWN:
                    esperando = False

        index_laberinto += 1

    pygame.quit()
