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

#boxes
boxes = [
    pygame.Rect(175, 150, 25, 25),
    pygame.Rect(200, 175, 25, 25),
    pygame.Rect(225, 200, 25, 25),
    pygame.Rect(125, 150, 25, 25),
    pygame.Rect(150, 175, 25, 25),
    pygame.Rect(175, 200, 25, 25),
]

#holes
holes = [
    pygame.Rect(300, 175, 25, 25),
]

#game floor
floor = [
    pygame.Rect(125, 200, 225, 25),
    pygame.Rect(125, 150, 225, 25),
    pygame.Rect(125, 175, 225, 25),
]
    
#finish station
finish = pygame.Rect(100, 175, 25, 25)

#while loop
run = True
while run:
    
    #press delay for increased playability
    pygame.time.delay(90)

    #arena
    arena = (
        pygame.Rect(75, 125, 300, 25),
        pygame.Rect(75, 125, 25, 125),
        pygame.Rect(350, 125, 25, 125),
        pygame.Rect(100, 225, 250, 25),
        pygame.Rect(100, 150, 25, 25),
        pygame.Rect(100, 200, 25, 25)
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

    if keys[pygame.K_ESCAPE]:
        run = False

    #checks if player does not go beyond arena boundaries
    if movement_player.x != 0 or movement_player.y != 0:
        rect = screen.get_rect().inflate(-6, -6)
        moved = player.move(movement_player.x, movement_player.y)
        for box in boxes:
            box_moved = moved
        #if the player is inside the arena he can move
        if moved.collidelist(arena) == -1 and box_moved.collidelist(arena) == -1:
            player = moved

            for box in boxes:
                #if the player collides any box it moves
                if player.colliderect(box):
                    box_moved = box.move(movement_player.x, movement_player.y)
                    #if the box collides with the arena or another box it does not move
                    if box_moved.collidelist(arena) == -1 and box_moved.collidelist(boxes) == -1:
                        box.x += movement_player.x
                        box.y += movement_player.y
                    else:
                        player.x -= movement_player.x
                        player.y -= movement_player.y

            for hole in holes:
                #if the player collides any box it moves
                if player.colliderect(hole):
                    run = False

            del_holes = holes
            del_boxes = boxes

            for i in del_holes:
                for k in del_boxes:
                    if i.colliderect(k):
                        boxes.remove(k)
                        holes.remove(i)

            #winning mechanism
            if player.colliderect(finish):
                print("YOU WON!")
                run = False



    screen.fill((0,0,0))

    #draws finish
    pygame.draw.rect(screen, pygame.Color('blue'), finish)

    #draws arena
    for wall in arena:
        pygame.draw.rect(screen, (0, 255, 0), (wall.x, wall.y, wall.width, wall.height))

    
    #draws floor
    for tile in floor:
        pygame.draw.rect(screen, pygame.Color('pink'), tile)
    

    #draws player
    pygame.draw.rect(screen, pygame.Color('red'), player)

    #draws box
    for box in boxes:
        pygame.draw.rect(screen, pygame.Color('yellow'), box)

    # #draws holes
    for hole in holes:
        pygame.draw.rect(screen, pygame.Color('grey'), hole)

    # Update the full Surface to the screen
    pygame.display.flip()

    # Run the program at 60 frames per second
    clock.tick(60)

pygame.quit()
