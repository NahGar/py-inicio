# pip install pygame
import pygame
import random

# Inicializar
pygame.init()

# Crear pantalla
pantalla = pygame.display.set_mode( (800,600) )

# Titulo e icono
pygame.display.set_caption("Invasión espacial")
icono = pygame.image.load("cohete_icon.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load('fondo.png')

# variables jugador
img_jugador = pygame.image.load("cohete.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# variables enemigo
img_enemigo = pygame.image.load("enemigo.png")
enemigo_x = random.randint(0,736)
enemigo_y = random.randint(50,200)
enemigo_x_cambio = 0.2
enemigo_y_cambio = 50

def jugador(x,y):
    pantalla.blit(img_jugador, (x, y))

def enemigo(x,y):
    pantalla.blit(img_enemigo, (x, y))

# Loop del juego
se_ejecuta = True
while se_ejecuta:
    # RGB
    # pantalla.fill((205, 144, 228))
    pantalla.blit(fondo, (0,0))

    for evento in pygame.event.get():
        # cerrar el programa
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        # presiona flechas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3
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

    jugador(jugador_x,jugador_y)

    # modificar ubicación enemigo
    enemigo_x += enemigo_x_cambio
    if enemigo_x < 0:
        enemigo_x_cambio = 0.3
        enemigo_y += enemigo_y_cambio
    if enemigo_x > 736:
        enemigo_x_cambio = -0.3
        enemigo_y += enemigo_y_cambio

    enemigo(enemigo_x, enemigo_y)

    # actualizar
    pygame.display.update()