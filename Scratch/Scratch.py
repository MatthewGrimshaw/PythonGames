# import pygames and initialise the module
import pygame
pygame.init()

display_width = 800
display_height = 600

#colours
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue= (0,0,255)

#define the window size for the gam
gameDisplay = pygame.display.set_mode((display_width,display_height))


#Set the windows title
pygame.display.set_caption('A bit Racey')

#Timer for the game
clock = pygame.time.Clock()

#image to load
carImg = pygame.image.load('racecar.png')

#function to diplay the car
def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x = (display_width * 0.4)
y = (display_height * 0.6)
x_change = 0



crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

                  

        #print(event)
    
    x += x_change
    
    gameDisplay.fill(white)
    car(x,y)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()