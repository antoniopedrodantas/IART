import pygame
from sys import exit


#initializes the screen 500x500
screen = pygame.display.set_mode((500, 500))

#inits game
pygame.get_init()

#sets window caption
pygame.display.set_caption("Box World")

# Creates a clock object to keep track of time
clock = pygame.time.Clock()

#player 
player = pygame.Rect(300, 175, 25, 25)

run = True
#while loop
while run:
    
    #press delay for increased playability
    pygame.time.delay(75)

    # creates the arena 
    arena = (
        pygame.Rect(100, 125, 250, 25),
        pygame.Rect(100, 125, 25, 125),
        pygame.Rect(350, 125, 25, 125),
        pygame.Rect(100, 225, 250, 25)
    )

    
    #adds key functionality
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    #creates movement vector that is later used for checking arena boundaries
    movement = pygame.Vector2(0, 0)

    if keys[pygame.K_LEFT]:
        movement.x -= 25

    if keys[pygame.K_RIGHT]:
        movement.x += 25

    if keys[pygame.K_UP]:
        movement.y -= 25

    if keys[pygame.K_DOWN]:
        movement.y += 25

    #checks if player does not go beyond arena boundaries
    if movement.x != 0 or movement.y != 0:
        rect = screen.get_rect().inflate(-6, -6)
        moved = player.move(movement.x, movement.y)
        if moved.collidelist(arena) == -1 and rect.contains(moved):
            player = moved

    screen.fill((0,0,0))

    #draws arena
    for wall in arena:
        pygame.draw.rect(screen, (0, 255, 0), (wall.x, wall.y, wall.width, wall.height))

    #draws player
    pygame.draw.rect(screen, pygame.Color('red'), player)

    # Update the full Surface to the screen
    pygame.display.flip()

    # Run the program at 60 frames per second
    clock.tick(60)

pygame.quit()





