#Básico (Desplegar la pantalla)
import pygame
pygame.init
screen = pygame.display.set_mode((1200, 780))

#Colores
Rojo1 = (230,41,41)
Rojo2 = (170,31,31)
Azul1 =(10,10,200)
Azul2 =(5,5,100)
Amarillo1 = (215,185,0)
Amarillo2 = (150,130,0)
Verde1 = (0,150,0)
Verde2 = (0,100,0)
Blanco1 = (220,220,220)
Bla_Roj = (220,220,220)
Gris1 = (150,150,150)

#Imágenes
img_galaxia = pygame.image.load('Galaxia.png')
img_marte = pygame.image.load('Marte.png')
img_tierra = pygame.image.load('Tierra.png')
img_nept = pygame.image.load('Neptuno.png')
img_sol = pygame.image.load('Sol.png')

#tamaños
g1 = 780 #Tamaño pestaña
c1 = 260 #Casillas de hogar
c2 = 25 #Radio borde Casillas de hogar
c2_1 = int(c2+c2/4) #Radio borde tablero
c3 = 25 #Margen tablero
c4 = 40 #Ancho borde casilla juego
c4_1 = 6  #Borde tablero
c4_2 = 5 #Borde casilla juego
c5 = 10 #Ancho limite derecho zona tablero
img1 = 175 #Tamaño foto de centro
img2 = 160 #Tamaño fotos hogar

running = True

clock = pygame.time.Clock()

while running:

    screen.fill((9,2,42))

    pygame.draw.line(screen, Blanco1, (g1+c5/2,0), (g1+c5/2,g1), c5)

    #Casillas de Hogar
    pygame.draw.rect(screen, Blanco1, (c3-c4_1, c3-c4_1, g1-2*c3+c4_1*2, g1-2*c3+c4_1*2),c4_1,c2_1,c2_1,c2_1,c2_1)  #Borde Tablero
    pygame.draw.rect(screen, Rojo2, (c3, c3, c1, c1),0,0,c2)  #Hogar Rojo Borde
    pygame.draw.rect(screen, Rojo1, (c3+c4, c3+c4, c1-c4*2, c1-c4*2),0,0,c2)  #Hogar Rojo
    img_marte2 = pygame.transform.scale(img_marte, (img2, img2))
    screen.blit(img_marte2,(c3+c1/2-img2/2,c3+c1/2-img2/2)) #Imagen Marte
    pygame.draw.rect(screen, Azul2, (g1-c1-c3, c3, c1, c1),0,0,0,c2)  #Hogar Azul Borde
    pygame.draw.rect(screen, Azul1, (g1-c1-c3+c4, c3+c4, c1-c4*2, c1-c4*2),0,0,0,c2)  #Hogar Azul
    img_nept2 = pygame.transform.scale(img_nept, (img2, img2))
    screen.blit(img_nept2,(g1-c3-c1/2-img2/2,c3+c1/2-img2/2)) #Imagen Neptuno
    pygame.draw.rect(screen, Amarillo2, (g1-c1-c3, g1-c1-c3, c1, c1),0,0,0,0,0,c2)  #Hogar Amarillo Borde
    pygame.draw.rect(screen, Amarillo1, (g1-c1-c3+c4, g1-c1-c3+c4, c1-c4*2, c1-c4*2),0,0,0,0,0,c2)  #Hogar Amarillo
    img_sol2 = pygame.transform.scale(img_sol, (img2, img2))
    screen.blit(img_sol2,(g1-c3-c1/2-img2/2,g1-c3-c1/2-img2/2)) #Imagen Sol
    pygame.draw.rect(screen, Verde2, (c3, g1-c1-c3, c1, c1),0,0,0,0,c2)  #Hogar Verde Borde
    pygame.draw.rect(screen, Verde1, (c3+c4, g1-c1-c3+c4, c1-c4*2, c1-c4*2),0,0,0,0,c2)  #Hogar Verde
    img_tierra2 = pygame.transform.scale(img_tierra, (img2, img2))
    screen.blit(img_tierra2,(c3+c1/2-img2/2, g1-c3-c1/2-img2/2)) #Imagen Tierra

    #Casillas de Juego
    x = (g1-(c3+c1)*2)+1
    x1 = x/3 #Ancho columna
    x2 = x-x1
    #Casillas verticales
    for i in range(0,7):
        for i2 in range (0,2):
           for i3 in range (0,2): 
               pygame.draw.rect(screen, Bla_Roj, (c3+c1+i2*x2, c3+(i*c1/7)+(x+c1)*i3, x1, c1/7),0,0,0,0,0)
               pygame.draw.rect(screen, Gris1, (c3+c1+i2*x2, c3+(i*c1/7)+(x+c1)*i3, x1, c1/7),c4_2,0,0,0,0)
    #Casillas horizontales
    for i in range(0,7):
        for i2 in range (0,2):
           for i3 in range (0,2): 
               pygame.draw.rect(screen, Bla_Roj, (c3+(i*c1/7)+(x+c1)*i3,c3+c1+i2*x2, c1/7 ,x1),0,0,0,0,0)
               pygame.draw.rect(screen, Gris1, (c3+(i*c1/7)+(x+c1)*i3, c3+c1+i2*x2, c1/7, x1),c4_2,0,0,0,0) 
    #Casillas Diagonales
        #Diagonales rojas
    pygame.draw.polygon(screen, Bla_Roj, ([c3+c1,c3+c1],[c2+c1,c3+c1+x1],[c3+c1+x1,c3+c1+x1]),0)  
    pygame.draw.polygon(screen, Gris1, ([c3+c1,c3+c1],[c2+c1,c3+c1+x1],[c3+c1+x1,c3+c1+x1]),c4_2*2)    
    pygame.draw.polygon(screen, Bla_Roj, ([c3+c1,c3+c1],[c2+c1+x1,c3+c1],[c3+c1+x1,c3+c1+x1]),0)  
    pygame.draw.polygon(screen, Gris1, ([c3+c1,c3+c1],[c2+c1+x1,c3+c1],[c3+c1+x1,c3+c1+x1]),c4_2*2)  
        #Diagonales azules
    pygame.draw.polygon(screen, Bla_Roj, ([g1-1-(c3+c1),c3+c1],[g1-1-(c2+c1),c3+c1+x1],[g1-1-(c3+c1+x1),c3+c1+x1]),0)  
    pygame.draw.polygon(screen, Gris1, ([g1-1-(c3+c1),c3+c1],[g1-1-(c2+c1),c3+c1+x1],[g1-1-(c3+c1+x1),c3+c1+x1]),c4_2*2)    
    pygame.draw.polygon(screen, Bla_Roj, ([g1-1-(c3+c1),c3+c1],[g1-1-(c2+c1+x1),c3+c1],[g1-1-(c3+c1+x1),c3+c1+x1]),0)  
    pygame.draw.polygon(screen, Gris1, ([g1-1-(c3+c1),c3+c1],[g1-1-(c2+c1+x1),c3+c1],[g1-1-(c3+c1+x1),c3+c1+x1]),c4_2*2)
        #Diagonales amarillas
    pygame.draw.polygon(screen, Bla_Roj, ([g1-1-(c3+c1),g1-1-(c3+c1)],[g1-1-(c2+c1),g1-1-(c3+c1+x1)],[g1-1-(c3+c1+x1),g1-1-(c3+c1+x1)]),0)  
    pygame.draw.polygon(screen, Gris1, ([g1-1-(c3+c1),g1-1-(c3+c1)],[g1-1-(c2+c1),g1-1-(c3+c1+x1)],[g1-1-(c3+c1+x1),g1-1-(c3+c1+x1)]),c4_2*2)    
    pygame.draw.polygon(screen, Bla_Roj, ([g1-1-(c3+c1),g1-1-(c3+c1)],[g1-1-(c2+c1+x1),g1-1-(c3+c1)],[g1-1-(c3+c1+x1),g1-1-(c3+c1+x1)]),0)  
    pygame.draw.polygon(screen, Gris1, ([g1-1-(c3+c1),g1-1-(c3+c1)],[g1-1-(c2+c1+x1),g1-1-(c3+c1)],[g1-1-(c3+c1+x1),g1-1-(c3+c1+x1)]),c4_2*2)
        #Diagonales verdes
    pygame.draw.polygon(screen, Bla_Roj, ([c3+c1,g1-1-(c3+c1)],[c2+c1,g1-1-(c3+c1+x1)],[c3+c1+x1,g1-1-(c3+c1+x1)]),0)  
    pygame.draw.polygon(screen, Gris1, ([c3+c1,g1-1-(c3+c1)],[c2+c1,g1-1-(c3+c1+x1)],[c3+c1+x1,g1-1-(c3+c1+x1)]),c4_2*2)    
    pygame.draw.polygon(screen, Bla_Roj, ([c3+c1,g1-1-(c3+c1)],[c2+c1+x1,g1-1-(c3+c1)],[c3+c1+x1,g1-1-(c3+c1+x1)]),0)  
    pygame.draw.polygon(screen, Gris1, ([c3+c1,g1-1-(c3+c1)],[c2+c1+x1,g1-1-(c3+c1)],[c3+c1+x1,g1-1-(c3+c1+x1)]),c4_2*2)


    #Casillas entrada rojo
    for i in range(0,8):
        pygame.draw.rect(screen, Rojo1, (c3+c1+x1, c3+(i*c1/7), x1, c1/7),0,0,0,0,0)
        pygame.draw.rect(screen, Rojo2, (c3+c1+x1, c3+(i*c1/7), x1, c1/7),c4_2,0,0,0,0)    
    #Casillas entrada amarillo
    for i in range(-1,7):
        pygame.draw.rect(screen, Amarillo1, (c3+c1+x1, c3+(i*c1/7)+x+c1, x1, c1/7),0,0,0,0,0)
        pygame.draw.rect(screen,Amarillo2, (c3+c1+x1, c3+(i*c1/7)+x+c1, x1, c1/7),c4_2,0,0,0,0) 
    #Casillas entrada verde
    for i in range(0,8):
        pygame.draw.rect(screen, Verde1, (c3+(i*c1/7), c3+c1+x1, c1/7, x1),0,0,0,0,0)
        pygame.draw.rect(screen, Verde2, (c3+(i*c1/7), c3+c1+x1, c1/7, x1),c4_2,0,0,0,0)   
    #Casillas entrada azul
    for i in range(-1,7):
        pygame.draw.rect(screen, Azul1, (c3+(i*c1/7)+x+c1, c3+c1+x1, c1/7, x1),0,0,0,0,0)
        pygame.draw.rect(screen, Azul2, (c3+(i*c1/7)+x+c1, c3+c1+x1, c1/7, x1),c4_2,0,0,0,0) 

    #Casilla salida rojo
    pygame.draw.rect(screen, Rojo1, (c3+c1, c3+(4*c1/7), x1, c1/7),0,0,0,0,0)
    pygame.draw.rect(screen, Rojo2, (c3+c1, c3+(4*c1/7), x1, c1/7),c4_2,0,0,0,0)
    #Casilla salida azul
    pygame.draw.rect(screen, Azul1, (c3+(2*c1/7)+(x+c1),c3+c1, c1/7 ,x1),0,0,0,0,0)
    pygame.draw.rect(screen, Azul2, (c3+(2*c1/7)+(x+c1), c3+c1, c1/7, x1),c4_2,0,0,0,0)
    #Casilla salida verde
    pygame.draw.rect(screen, Verde1, (c3+(4*c1/7),c3+c1+x2, c1/7 ,x1),0,0,0,0,0)
    pygame.draw.rect(screen, Verde2, (c3+(4*c1/7), c3+c1+x2, c1/7, x1),c4_2,0,0,0,0)
    #Casilla salida amarillo
    pygame.draw.rect(screen, Amarillo1, (c3+c1+x2, g1-(c3+(4*c1/7)), x1, c1/7),0,0,0,0,0)
    pygame.draw.rect(screen, Amarillo2, (c3+c1+x2, g1-(c3+(4*c1/7)), x1, c1/7),c4_2,0,0,0,0)

    #Casilla seguro rojo
    pygame.draw.rect(screen, Rojo1, (c3+(4*c1/7),c3+c1, c1/7 ,x1),0,0,0,0,0)
    pygame.draw.rect(screen, Rojo2, (c3+(4*c1/7), c3+c1, c1/7, x1),c4_2,0,0,0,0)
    #Casilla seguro azul
    pygame.draw.rect(screen, Azul1, (c3+c1+x2, c3+(4*c1/7), x1, c1/7),0,0,0,0,0)
    pygame.draw.rect(screen, Azul2, (c3+c1+x2, c3+(4*c1/7), x1, c1/7),c4_2,0,0,0,0)
    #Casilla salida amarillo
    pygame.draw.rect(screen, Amarillo1, (c3+(2*c1/7)+(x+c1),c3+c1+x2, c1/7 ,x1),0,0,0,0,0)
    pygame.draw.rect(screen, Amarillo2, (c3+(2*c1/7)+(x+c1), c3+c1+x2, c1/7, x1),c4_2,0,0,0,0)
    #Casilla salida verde
    pygame.draw.rect(screen, Verde1, (c3+c1, g1-(c3+(4*c1/7)), x1, c1/7),0,0,0,0,0)
    pygame.draw.rect(screen, Verde2, (c3+c1, g1-(c3+(4*c1/7)), x1, c1/7),c4_2,0,0,0,0)

    #Circulo central
    img_galaxia2 = pygame.transform.scale(img_galaxia, (img1, img1))
    imagen1 = screen.blit(img_galaxia2,((g1/2)-img1/2,g1/2-img1/2))
    rectang = imagen1
    pygame.draw.ellipse(screen,Blanco1,rectang)
    screen.blit(img_galaxia2,((g1/2)-img1/2,g1/2-img1/2))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    clock.tick(60)


pygame.quit()

