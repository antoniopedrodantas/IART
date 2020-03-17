import pygame
from sys import exit

from level import *


#initializes the screen 500x500
screen = pygame.display.set_mode((500, 500))

#inits game
pygame.get_init()

#sets window caption
pygame.display.set_caption("Box World")

# Creates a clock object to keep track of time
clock = pygame.time.Clock()

#specifies the level
level = Level(2)

#while loop
run = True
while run:
    
    #press delay for increased playability
    pygame.time.delay(90)

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

    if keys[pygame.K_ESCAPE]:
        run = False

    #checks if player does not go beyond arena boundaries
    if movement_player.x != 0 or movement_player.y != 0:
        rect = screen.get_rect().inflate(-6, -6)
        moved = level.player.move(movement_player.x, movement_player.y)
        
        for box in level.boxes:
            box_moved = moved

        for ice in level.iceBoxes:
            ice_moved = moved
        
        #if the player is inside the arena he can move
        if moved.collidelist(level.arena) == -1 and box_moved.collidelist(level.arena) == -1:
            level.player = moved

            for box in level.boxes:
                #if the player collides any box it moves
                if level.player.colliderect(box):
                    box_moved = box.move(movement_player.x, movement_player.y)
                    #if the box collides with the arena or another box it does not move
                    if box_moved.collidelist(level.arena) == -1 and box_moved.collidelist(level.boxes) == -1 and box_moved.collidelist(level.iceBoxes) == -1:
                        box.x += movement_player.x
                        box.y += movement_player.y
                    else:
                        level.player.x -= movement_player.x
                        level.player.y -= movement_player.y

            for hole in level.holes:
                #if the player collides any box it moves
                if level.player.colliderect(hole):
                    run = False
            #ice
            for ice in level.iceBoxes:
                if level.player.colliderect(ice):
                    ice_moved = ice.move(movement_player.x, movement_player.y)
                    #check when icebox collides
                    while(ice.collidelist(level.arena) == -1 and ice.collidelist(level.boxes) == -1 and ice.collidelist(level.holes) == -1):
                        ice.x += movement_player.x
                        ice.y += movement_player.y
                    
                    if(ice.collidelist(level.holes) != -1):
                        level.player.x -= movement_player.x
                        level.player.y -= movement_player.y
                    else:
                        #compensating for last move
                        ice.x -= movement_player.x
                        ice.y -= movement_player.y
                        level.player.x -= movement_player.x
                        level.player.y -= movement_player.y

            del_holes = level.holes
            del_boxes = level.boxes
            del_ice = level.iceBoxes

            for i in del_holes:
                for k in del_boxes:
                    if i.colliderect(k):
                        level.boxes.remove(k)
                        level.holes.remove(i)
                for j in del_ice:
                    if i.colliderect(j):
                        level.iceBoxes.remove(j)
                        level.holes.remove(i)


            #winning mechanism
            if level.player.colliderect(level.finish):
                print("\n")
                print("YOU WON!")
                run = False



    screen.fill((0,0,0))

    #draws arena
    for wall in level.arena:
        pygame.draw.rect(screen, (0, 255, 0), (wall.x, wall.y, wall.width, wall.height))

    
   #draws floor
    for tile in level.floor:
        pygame.draw.rect(screen, pygame.Color('pink'), tile)

    
    #draws finish
    pygame.draw.rect(screen, pygame.Color('blue'), level.finish)
    

    #draws player
    pygame.draw.rect(screen, pygame.Color('red'), level.player)

    #draws box
    for box in level.boxes:
        pygame.draw.rect(screen, pygame.Color('yellow'), box)

    # #draws holes
    for hole in level.holes:
        pygame.draw.rect(screen, pygame.Color('grey'), hole)
    #draws ice
    for ice in level.iceBoxes:
        pygame.draw.rect(screen, pygame.Color(0, 255, 255), ice)


    # Update the full Surface to the screen
    pygame.display.flip()

    # Run the program at 60 frames per second
    clock.tick(60)

pygame.quit()
