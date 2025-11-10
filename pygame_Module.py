import pygame

pygame.init() #Initialize pygame

#Set up display
screen = pygame.display.set_mode((500,400))
pygame.display.set_caption("My First Game")

#Colors (R, G, B)
white = (255,255,255)
red = (255, 0, 0)

#Clock to control Fps
clock = pygame.time.Clock()

#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#Close Window
            running = False

    #Fill screen
    screen.fill(white)

    #Draw a red rectangle
    pygame.draw.rect(screen, red, (150,100,200,100))


    #update display
    pygame.display.flip()

    #Limit FPS
    clock.tick(60)

#Quit pygame
pygame.quit()


#Other functions
'''
# Draw a circle
pygame.draw.circle(screen, blue, (x, y),20)
#Load images
pygame.image.load
#play sounds
pygame.mixer.Sound
'''

#Moving  a player
'''
#player
x, y = 200,200
speed = 5

running = True
while running:
    for event in pygame.event.get(): #Handling Events
        if event.type == pygame.QUIT:
            running = False

    #Get keys pressed(Keyboard events)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
        
    screen.fill(white)
    pygame.draw.circle(screen, blue, (x, y),20)
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
'''
