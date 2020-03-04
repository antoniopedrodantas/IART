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
player = pygame.Rect(325, 175, 25, 25)

#box
box = pygame.Rect(200, 175, 25, 25)

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
    movement_player = pygame.Vector2(0, 0)

    if keys[pygame.K_LEFT]:
        movement_player.x -= 25

    if keys[pygame.K_RIGHT]:
        movement_player.x += 25

    if keys[pygame.K_UP]:
        movement_player.y -= 25

    if keys[pygame.K_DOWN]:
        movement_player.y += 25

    #checks if player does not go beyond arena boundaries
    if movement_player.x != 0 or movement_player.y != 0:
        rect = screen.get_rect().inflate(-6, -6)
        moved = player.move(movement_player.x, movement_player.y)
        box_moved = box.move(0, 0)
        #if the player is inside the arena he can move
        if moved.collidelist(arena) == -1 and box_moved.collidelist(arena) == -1:
            player = moved
            #if the player collides with the box it moves
            if player.colliderect(box):
                box_moved = box.move(movement_player.x, movement_player.y)
                #if the box collides with the arena it does not move
                if box_moved.collidelist(arena) == -1:
                    box = box_moved
                else:
                    player.x -= movement_player.x
                    player.y -= movement_player.y



    screen.fill((0,0,0))

    #draws arena
    for wall in arena:
        pygame.draw.rect(screen, (0, 255, 0), (wall.x, wall.y, wall.width, wall.height))

    #draws player
    pygame.draw.rect(screen, pygame.Color('red'), player)

    #draws box
    pygame.draw.rect(screen, pygame.Color('yellow'), box)

    # Update the full Surface to the screen
    pygame.display.flip()

    # Run the program at 60 frames per second
    clock.tick(60)

pygame.quit()





