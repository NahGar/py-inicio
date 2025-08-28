# pip install pygame
# generar exe
# pyinstaller --clean --onefile --windowed main.py
# --clean: elimina todos los archivos temporales y directorios creados por pyinstaller durante la construcción del archivo ejecutable.
# --onefile: crea un archivo ejecutable que contiene todos los archivos necesarios para ejecutar el script, incluyendo los módulos y bibliotecas utilizadas por el script.
# --windowed: crea un archivo ejecutable que se ejecuta en una ventana en lugar de en pantalla completa.

import pygame
import random
import math
from pygame import mixer
import io

# Inicializar
pygame.init()

mixer.music.load('ambiente.mp3')
mixer.music.set_volume(0.2)
mixer.music.play(-1) # -1 es para que se repita

def fuente_bytes(fuente):
    # abre en modo lectura binaria
    with open(fuente,'rb') as f:
        ttfbytes = f.read()
    return io.BytesIO(ttfbytes)


def jugador(x,y):
    pantalla.blit(img_jugador, (x, y))

def enemigo(x,y,e):
    pantalla.blit(img_enemigo[e], (x, y))

def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


def hay_colision(x_1,y_1,x_2,y_2):
    distancia = math.sqrt(math.pow(x_1-x_2,2) + math.pow(y_1-y_2,2))
    return True if distancia < 27 else False

def crear_enemigos():
    global cantidad_enemigos, img_enemigo, enemigo_x, enemigo_y
    global enemigo_x_cambio, enemigo_y_cambio
    for e in range(cantidad_enemigos):
        img_enemigo.append(pygame.image.load("enemigo.png"))
        enemigo_x.append(random.randint(0, 736))
        enemigo_y.append(random.randint(50, 200))
        enemigo_x_cambio.append(random.choice([-1, 1]) * 0.3)
        enemigo_y_cambio.append(50)


# Crear pantalla
pantalla = pygame.display.set_mode( (800,600) )

# Titulo e icono
pygame.display.set_caption("Invasión espacial")
icono = pygame.image.load("cohete_icon.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load('fondo.png')

# variables jugador
img_jugador = pygame.image.load("jugador.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# variables enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8
crear_enemigos()

# variables de la bala
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = jugador_y
bala_y_cambio = 1.5
bala_visible = False

puntaje = 0
fuente_como_bytes_puntaje = fuente_bytes('airstrikelaser.ttf')
#fuente_puntaje = pygame.font.Font('airstrikelaser.ttf',32)
fuente_puntaje = pygame.font.Font(fuente_como_bytes_puntaje,32)
texto_puntaje_x = 10
texto_puntaje_y = 10

fuente_como_bytes_fin = fuente_bytes('airstrikelaser.ttf')
#fuente_fin_juego = pygame.font.Font('airstrikelaser.ttf',60)
fuente_fin_juego = pygame.font.Font(fuente_como_bytes_fin,60)


def mostrar_puntaje(x,y):
    texto = fuente_puntaje.render(f"Puntaje: {puntaje}",True,(255,255,255))
    pantalla.blit(texto, (x,y))

def fin_juego():
    for e in range(cantidad_enemigos):
        enemigo_y[e] = 1000

    texto = fuente_fin_juego.render(f"JUEGO TERMINADO", True, (255, 255, 255))
    pantalla.blit(texto, (100, 250))


# Loop del juego
se_ejecuta = True
while se_ejecuta:
    # RGB
    # pantalla.fill((205, 144, 228))
    pantalla.blit(fondo, (0,0))

    mostrar_puntaje(texto_puntaje_x,texto_puntaje_y)

    for evento in pygame.event.get():
        # cerrar el programa
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        # presiona teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                    sonido_disparo = mixer.Sound('disparo.mp3')
                    sonido_disparo.set_volume(0.3)
                    sonido_disparo.play()

                    bala_x = jugador_x
                    disparar_bala(bala_x,bala_y)


        # suelta flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # modificar ubicación jugador
    jugador_x += jugador_x_cambio
    if jugador_x < 0:
        jugador_x = 0
    if jugador_x > 736:
        jugador_x = 736

    # modificar ubicación bala
    if bala_y <= -32:
        bala_y = jugador_y
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    # modificar ubicación enemigo
    for e in range(cantidad_enemigos):

        # fin del juego
        if enemigo_y[e] > 450:
            fin_juego()
            break

        enemigo_x[e] += enemigo_x_cambio[e]
        if enemigo_x[e] < 0 or enemigo_x[e] > 736:
            enemigo_x_cambio[e] = enemigo_x_cambio[e] * -1
            enemigo_y[e] += enemigo_y_cambio[e]

        colision = hay_colision(enemigo_x[e],enemigo_y[e],bala_x,bala_y)
        if colision:
            sonido_explosion = mixer.Sound('explosion.mp3')
            sonido_explosion.set_volume(0.3)
            sonido_explosion.play()

            bala_visible = False
            bala_y = jugador_y
            puntaje += 1
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)
            enemigo_x_cambio[e] = random.choice([-1, 1]) * 0.3

        enemigo(enemigo_x[e], enemigo_y[e],e)

    jugador(jugador_x, jugador_y)


    # actualizar
    pygame.display.update()