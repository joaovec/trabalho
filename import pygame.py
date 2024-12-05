
import pygame
pygame.init()
x = 293
y = 350


y1 = -50
y2 = -30
y3 = -30
y4 = -25

v = 10
v1 = -20
v2 = -15
v3 =  -30
v4 = -15

fundo = pygame.image.load('pista.png.png')
pista1 = pygame.image.load('movimento.png')
carro2 = pygame.image.load('carro2.png')
moto = pygame.image.load('moto.png')
carro3 = pygame.image.load('carro3.png')
carro = pygame.image.load('carro-1.png.png')
janela = pygame.display.set_mode((587,626))
pygame.display.set_caption('game')

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y-= v 
    if comandos[pygame.K_DOWN]:  
        y+= v  
    if comandos[pygame.K_RIGHT]:
        x+= v 
    if comandos[pygame.K_LEFT]:
        x-= v   
    y1 -= v1
    y2 -= v2
    y3 -= v3
    y4 -= v4

    if(y1 >=900):

        y1 = -50    
    if(y1 >=800):
        y2 = -20
    if(y3 >=780):
        y3 = -30  
    if(y4 >=750):
        y4 = -25 
 

    janela.blit(fundo,(0,0))
    janela.blit(pista1,(293,y1))
    janela.blit(carro2,(100,y2))
    janela.blit(moto,(255,y3))
    janela.blit(carro3,(370,y4))
    janela.blit(carro, (x,y))
    pygame.display.update()
pygame.quit()
