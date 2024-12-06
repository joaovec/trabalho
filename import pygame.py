import pygame


pygame.init()


LARGURA_TELA = 587
ALTURA_TELA = 626


x = 293
y = 350
y1 = -50
y2 = -30
y3 = -30
y4 = -25

v = 10
v1 = -20
v2 = -15
v3 = -30
v4 = -15


fundo = pygame.image.load('pista.png.png')
pista1 = pygame.image.load('movimento.png')
carro2 = pygame.image.load('carro2.png')
moto = pygame.image.load('moto.png')
carro3 = pygame.image.load('carro3.png')
carro = pygame.image.load('carro-1.png.png')


janela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption('Game')


carro_rect = pygame.Rect(x + 20, y + 20, carro.get_width() - 40, carro.get_height() - 40)  
carro2_rect = pygame.Rect(100 + 20, y2 + 20, carro2.get_width() - 40, carro2.get_height() - 40)  
moto_rect = pygame.Rect(255 + 20, y3 + 20, moto.get_width() - 40, moto.get_height() - 40)  
carro3_rect = pygame.Rect(370 + 20, y4 + 20, carro3.get_width() - 40, carro3.get_height() - 40)  

janela_aberta = True


def reposicionar_carros():
    global y1, y2, y3, y4
    y1 = -50
    y2 = -30
    y3 = -30
    y4 = -25


def verificar_colisao():
    if carro2_rect.colliderect(carro_rect):
        print("Colisão com o carro 2 detectada!")
        return True  
    if moto_rect.colliderect(carro_rect):
        print("Colisão com a moto detectada!")
        return True
    if carro3_rect.colliderect(carro_rect):
        print("Colisão com o carro 3 detectada!")
        return True
    return False


while janela_aberta:
    pygame.time.delay(50)  
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= v
    if comandos[pygame.K_DOWN]:
        y += v
    if comandos[pygame.K_RIGHT]:
        x += v
    if comandos[pygame.K_LEFT]:
        x -= v
    
    
    y1 -= v1
    y2 -= v2
    y3 -= v3
    y4 -= v4

    
    if y1 >= 900:
        reposicionar_carros()
    if y2 >= 800:
        reposicionar_carros()
    if y3 >= 780:
        reposicionar_carros()
    if y4 >= 750:
        reposicionar_carros()

    
    carro_rect.topleft = (x + 20, y + 20)
    carro2_rect.topleft = (100 + 20, y2 + 20)
    moto_rect.topleft = (255 + 20, y3 + 20)
    carro3_rect.topleft = (370 + 20, y4 + 20)

    
    if (carro2_rect.top < ALTURA_TELA and carro2_rect.bottom > 0) and verificar_colisao():
        janela_aberta = False  

    if (moto_rect.top < ALTURA_TELA and moto_rect.bottom > 0) and verificar_colisao():
        janela_aberta = False  

    if (carro3_rect.top < ALTURA_TELA and carro3_rect.bottom > 0) and verificar_colisao():
        janela_aberta = False  

    
    janela.blit(fundo, (0, 0))
    janela.blit(pista1, (293, y1))
    janela.blit(carro2, (100, y2))
    janela.blit(moto, (255, y3))
    janela.blit(carro3, (370, y4))
    janela.blit(carro, (x, y))

    
    pygame.display.update()


pygame.quit()

