import pygame
import argparse

from sys import exit

from level import *
from state import *



def move(movement_player, movement):
    if(movement == "left"):
        movement_player.x -= 25
        return movement_player
    elif(movement == "right"):
        movement_player.x += 25
        return movement_player
    elif(movement == "up"):
        movement_player.y -= 25
        return movement_player
    elif(movement == "down"):
        movement_player.y += 25
        return movement_player  



def calculateGameState(movement, st):

    #checks if player does not go beyond arena boundaries
    if movement.x != 0 or movement.y != 0:
        rect = screen.get_rect().inflate(-6, -6)
        moved = st.player.move(movement.x, movement.y)
        
        for box in st.boxes:
            box_moved = moved

        for ice in st.iceBoxes:
            ice_moved = moved
        
        #if the player is inside the arena he can move
        if moved.collidelist(st.arena) == -1 and box_moved.collidelist(st.arena) == -1:
            st.player = moved

            for box in st.boxes:
                #if the player collides any box it moves
                if st.player.colliderect(box):
                    box_moved = box.move(movement.x, movement.y)
                    #if the box collides with the arena or another box it does not move
                    if box_moved.collidelist(st.arena) == -1 and box_moved.collidelist(st.boxes) == -1 and box_moved.collidelist(st.iceBoxes) == -1:
                        box.x += movement.x
                        box.y += movement.y
                    else:
                        st.player.x -= movement.x
                        st.player.y -= movement.y

            for hole in st.holes:
                #if the player collides any box it moves
                if st.player.colliderect(hole):
                    #return False
                    st.player.x -= movement.x
                    st.player.y -= movement.y

            #ice
            for ice in st.iceBoxes:
                if st.player.colliderect(ice):
                    ice_moved = ice.move(movement.x, movement.y)
                    #check when icebox collides
                    while(ice.collidelist(st.arena) == -1 and ice.collidelist(st.boxes) == -1 and ice.collidelist(st.holes) == -1):
                        ice.x += movement.x
                        ice.y += movement.y
                    
                    if(ice.collidelist(st.holes) != -1):
                        st.player.x -= movement.x
                        st.player.y -= movement.y
                    else:
                        #compensating for last move
                        ice.x -= movement.x
                        ice.y -= movement.y
                        st.player.x -= movement.x
                        st.player.y -= movement.y

            del_holes = st.holes
            del_boxes = st.boxes
            del_ice = st.iceBoxes

            for i in del_holes:
                for k in del_boxes:
                    if i.colliderect(k):
                        st.boxes.remove(k)
                        st.holes.remove(i)
                for j in del_ice:
                    if i.colliderect(j):
                        st.iceBoxes.remove(j)
                        st.holes.remove(i)


            #winning mechanism
            if st.player.colliderect(st.finish):
                print("\n")
                print("YOU WON!")
                return False


def drawGameState(level):

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


def nextMove():

    #creates movement
    movement = pygame.Vector2(0, 0)

    #creates list with possible states
    possibleStates = []


    #creates all tmp variables
    tmp1 = State(state.level)

    tmp2 = State(state.level)

    tmp3 = State(state.level)

    tmp4 = State(state.level)

    # is it left?
    movement = move(movement, "left")
    calculateGameState(movement, tmp1.level)
    tmp1.addMove("left")
    possibleStates.append(tmp1)

    # is it right?
    movement = move(movement, "right")
    calculateGameState(movement, tmp2.level)
    tmp2.addMove("right")
    possibleStates.append(tmp2)

    # is it up?
    movement = move(movement, "up")
    calculateGameState(movement, tmp3.level)
    tmp3.addMove("up")
    possibleStates.append(tmp3)

    # is it down?
    movement = move(movement, "down")
    calculateGameState(movement, tmp4.level)
    tmp4.addMove("down")
    possibleStates.append(tmp4)

    for st in possibleStates:
        queue.append(st)
        







#initializes the screen 500x500
screen = pygame.display.set_mode((500, 500))

#inits game
pygame.get_init()

#sets window caption
pygame.display.set_caption("Box World")

# Creates a clock object to keep track of time
clock = pygame.time.Clock()

#gets the level
parser = argparse.ArgumentParser(description='Gets game level')
parser.add_argument('level', type=int, help='Game level')
args = parser.parse_args()
l = args.level

#specifies the level
level = Level(l)

#game states the player has already been in
visited = []

#current game state
state = State(level)

#queue with nodes
queue = []

#initial state added to the queue
queue.append(state)


#while loop
run = True
while True:
    
    
    state = queue[0]

    #adds key functionality
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    #creates movement vector that is later used for checking arena boundaries
    #movement_player = pygame.Vector2(0, 0)

    #calculates player movement
    """
    if keys[pygame.K_LEFT]:
        move(movement_player, "left")

    if keys[pygame.K_RIGHT]:
        move(movement_player, "right")

    if keys[pygame.K_UP]:
        move(movement_player, "up")

    if keys[pygame.K_DOWN]:
        move(movement_player, "down")
    """

    if keys[pygame.K_r]:
        level = Level(l)

    if keys[pygame.K_ESCAPE]:
        run = False
    


    #calculates next move
    nextMove()


    #press delay for increased playability
    pygame.time.delay(90)

    #draws game state
    drawGameState(queue[0].level)

    # Update the full Surface to the screen
    pygame.display.flip()

    # Run the program at 60 frames per second
    clock.tick(60)

    queue.remove(queue[0])
    print(state.moves)
    


    #calculates game state
    #if calculateGameState(movement_player) == False:
        #run = False

    screen.fill((0,0,0))

    #draws game state
    #drawGameState(level)

    # Update the full Surface to the screen
    #pygame.display.flip()

    # Run the program at 60 frames per second
    #clock.tick(60)

    #break condition
    if run == False:
        break
    

pygame.quit()
