# pip install pygame
import pygame
import random
import math

# Inicializar
pygame.init()

def jugador(x,y):
    pantalla.blit(img_jugador, (x, y))

def enemigo(x,y):
    pantalla.blit(img_enemigo, (x, y))

def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))

def hay_colision(x_1,y_1,x_2,y_2):
    distancia = math.sqrt(math.pow(x_1-x_2,2) + math.pow(y_1-y_2,2))
    return True if distancia < 27 else False

def aparece_enemigo():
    global enemigo_x
    global enemigo_y
    global enemigo_x_cambio
    enemigo_x = random.randint(0, 736)
    enemigo_y = random.randint(50, 200)
    enemigo_x_cambio = random.choice([-1, 1]) * 0.3

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
img_enemigo = pygame.image.load("enemigo.png")
enemigo_x = 0
enemigo_y = 0
enemigo_x_cambio = 0
enemigo_y_cambio = 50
aparece_enemigo()

# variables de la bala
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = jugador_y
bala_y_cambio = 1.5
bala_visible = False

puntaje = 0


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
        # presiona teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
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

    # modificar ubicación enemigo
    enemigo_x += enemigo_x_cambio
    '''
    if enemigo_x < 0:
        enemigo_x_cambio = 0.5
        enemigo_y += enemigo_y_cambio
    if enemigo_x > 736:
        enemigo_x_cambio = -0.5
        enemigo_y += enemigo_y_cambio
    '''
    if enemigo_x < 0 or enemigo_x > 736:
        enemigo_x_cambio = enemigo_x_cambio * -1
        enemigo_y += enemigo_y_cambio

    # modificar ubicación bala
    if bala_y <= -32:
        bala_y = jugador_y
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x,bala_y)
        bala_y -= bala_y_cambio

    colision = hay_colision(enemigo_x,enemigo_y,bala_x,bala_y)
    if colision:
        bala_visible = False
        bala_y = jugador_y
        puntaje += 1
        aparece_enemigo()

    jugador(jugador_x, jugador_y)
    enemigo(enemigo_x, enemigo_y)

    # actualizar
    pygame.display.update()