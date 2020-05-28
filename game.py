import pygame
import argparse
import math
import time
#import qlearn
import random
from matplotlib import pyplot as plt

from sys import exit
from copy import deepcopy

from level import *
from state import *
from qlearn import *

try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

run = True
solution = []
max_depth = 10
run2 = True

solutions = []

# ============================================== FUNCTIONS ==============================================


def move(movement_player, movement):
    if movement == "left":
        movement_player.x -= 25
        return movement_player
    elif movement == "right":
        movement_player.x += 25
        return movement_player
    elif movement == "up":
        movement_player.y -= 25
        return movement_player
    elif movement == "down":
        movement_player.y += 25
        return movement_player


def calculateGameState(movement, st):
    global run
    global solution
    global run2

    # cheks if it is impossible to complete
    if st.level.finish.collidelist(st.level.boxes) != -1:
        if args.algorithm != "qlearning":
            return False

    # checks if player does not go beyond arena boundaries
    if movement.x != 0 or movement.y != 0:
        rect = screen.get_rect().inflate(-6, -6)
        moved = st.level.player.move(movement.x, movement.y)

        for box in st.level.boxes:
            box_moved = moved

        for ice in st.level.iceBoxes:
            ice_moved = moved

        # if the player is inside the arena he can move
        # and box_moved.collidelist(st.level.arena) == -1
        if moved.collidelist(st.level.arena) == -1:
            st.level.player = moved

            for box in st.level.boxes:
                # if the player collides any box it moves
                if st.level.player.colliderect(box):
                    box_moved = box.move(movement.x, movement.y)
                    # if the box collides with the arena or another box it does not move
                    if box_moved.collidelist(st.level.arena) == -1 and box_moved.collidelist(
                            st.level.boxes) == -1 and box_moved.collidelist(st.level.iceBoxes) == -1:
                        box.x += movement.x
                        box.y += movement.y
                    else:
                        st.level.player.x -= movement.x
                        st.level.player.y -= movement.y

            # ice
            for ice in st.level.iceBoxes:

                if st.level.player.colliderect(ice):
                    ice_moved = ice.move(movement.x, movement.y)
                    # check when icebox collides
                    while (ice_moved.collidelist(st.level.arena) == -1 and ice_moved.collidelist(st.level.boxes) == -1 and ice_moved.collidelist(st.level.holes) == -1 and ice_moved.collidelist(st.level.iceBoxes) == -1):
                        ice_moved.x += movement.x
                        ice_moved.y += movement.y
                        ice.x += movement.x
                        ice.y += movement.y

                    ice.x += movement.x
                    ice.y += movement.y

                    if ice.collidelist(st.level.holes) != -1:
                        st.level.player.x -= movement.x
                        st.level.player.y -= movement.y
                    else:
                        # compensating for last move
                        ice.x -= movement.x
                        ice.y -= movement.y
                        st.level.player.x -= movement.x
                        st.level.player.y -= movement.y

            for hole in st.level.holes:
                # if the player collides any holes it doesnt move
                if st.level.player.colliderect(hole):
                    # return False
                    st.level.player.x -= movement.x
                    st.level.player.y -= movement.y

            del_holes = st.level.holes
            del_boxes = st.level.boxes
            del_ice = st.level.iceBoxes

            for i in del_holes:
                for k in del_boxes:
                    if i.colliderect(k):
                        st.level.boxes.remove(k)
                        st.level.holes.remove(i)
                for j in del_ice:
                    if i.colliderect(j):
                        st.level.iceBoxes.remove(j)
                        st.level.holes.remove(i)

            # winning mechanism
            if st.level.player.colliderect(st.level.finish):
                if args.mode == "human":
                    print(st.moves)
                    run2 = False
                    run = False
                #elif args.mode == "ai" and (args.algorithm == "qlearning" or args.algorithm == "sarsa"):
                    #print("Found solution !")
                else:
                    run = False
                    solution = st

            return True


def drawGameState(level):

    # draws floor
    for tile in level.floor:
        pygame.draw.rect(screen, pygame.Color('pink'), tile)

    # draws arena
    for wall in level.arena:
        pygame.draw.rect(screen, (0, 255, 0),
                         (wall.x, wall.y, wall.width, wall.height))
    
    

    # draws finish
    pygame.draw.rect(screen, pygame.Color('blue'), level.finish)

    # draws player
    pygame.draw.rect(screen, pygame.Color('red'), level.player)

    # draws box
    for box in level.boxes:
        pygame.draw.rect(screen, pygame.Color('yellow'), box)

    # #draws holes
    for hole in level.holes:
        pygame.draw.rect(screen, pygame.Color('grey'), hole)
    # draws ice
    for ice in level.iceBoxes:
        pygame.draw.rect(screen, pygame.Color(0, 255, 255), ice)


# ============================================== BREADTH-FIRST-SEARCH ==============================================
def compareStatesBFS(possibleMoves):

    for st1 in possibleMoves:
        flag = True
        for st2 in visited:
            if st1.level == st2.level:
                flag = False
        if flag:
            queue.append(st1)


# ============================================== DEPTH-FIRST-SEARCH ==============================================
def compareStatesDFS(possibleMoves):
    for st1 in possibleMoves:
        flag = True
        for st2 in visited:
            if st1.level == st2.level:
                flag = False
        if flag:
            queue.insert(1, st1)


# ============================================== ITERATIVE DEPTH-FIRST-SEARCH ==============================================
def compareStatesIDFS(possibleMoves):

    global max_depth

    for st1 in possibleMoves:
        if len(st1.moves) > max_depth:
            continue
        flag = True
        for st2 in visited:
            if st1.level == st2.level:
                flag = False
        if flag:
            queue.insert(1, st1)


# ============================================== GREEDY ==============================================
def exitDistance(s):
    return math.sqrt(math.pow(s.level.player.x - s.level.finish.x, 2) + math.pow(s.level.player.y - s.level.finish.y, 2))


def compareStatesGreedy(possibleMoves):
    for st1 in possibleMoves:
        flag = True
        for st2 in visited:
            if st1.level == st2.level:
                flag = False
        if flag:
            queue.put(st1)


# ============================================== A - STAR ==============================================
def compareStatesAstar(possibleMoves):

    temporary = []

    for st1 in possibleMoves:
        flag = True
        for st2 in visited:
            if st1.level == st2.level:
                flag = False
        if flag:
            temporary.append(st1)

    if len(temporary) == 0:
        run = False
    else:
        for s in temporary:
            queue.put(s)


def calculateMinimumSolution():

    lowest_value_index = 0

    for j in range(len(solutions)):

        if len(solutions[j].moves) < len(solutions[lowest_value_index].moves):
            lowest_value_index = j

    return solutions[lowest_value_index].moves

# ============================================== A.I. FUNCTIONS ==============================================


def nextMove(algorithm, state):
    possibleMoves = []

    # creates all tmp variables
    tmp1 = deepcopy(state)

    tmp2 = deepcopy(state)

    tmp3 = deepcopy(state)

    tmp4 = deepcopy(state)

    pM = []

    # is it left?
    movement1 = pygame.Vector2(-25, 0)
    if calculateGameState(movement1, tmp1):
        if tmp1.level.player.x != state.level.player.x or tmp1.level.player.y != state.level.player.y:
            tmp1.addMove("left")
            possibleMoves.append(tmp1)
            pM.append("left")

    # is it right?
    movement2 = pygame.Vector2(25, 0)
    if calculateGameState(movement2, tmp2):
        #if not tmp2 == state:
        if tmp2.level.player.x != state.level.player.x or tmp2.level.player.y != state.level.player.y:
            tmp2.addMove("right")
            possibleMoves.append(tmp2)
            pM.append("right")

    # is it up?
    movement3 = pygame.Vector2(0, -25)
    if calculateGameState(movement3, tmp3):
        #if not tmp3 == state:
        if tmp3.level.player.x != state.level.player.x or tmp3.level.player.y != state.level.player.y:
            tmp3.addMove("up")
            possibleMoves.append(tmp3)
            pM.append("up")

    # is it down?
    movement4 = pygame.Vector2(0, 25)
    if calculateGameState(movement4, tmp4):
        #if not tmp4 == state:
        if tmp4.level.player.x != state.level.player.x or tmp4.level.player.y != state.level.player.y:
            tmp4.addMove("down")
            possibleMoves.append(tmp4)
            pM.append("down")

    # puts moves on queue based on algorithm
    if algorithm == "bfs":  # breadth-first
        compareStatesBFS(possibleMoves)
    elif algorithm == "dfs":  # depth-first search
        possibleMoves.reverse()
        compareStatesDFS(possibleMoves)
    elif algorithm == "greedy":  # greedy
        compareStatesGreedy(possibleMoves)
    elif algorithm == "idfs":      # iterative depth search
        possibleMoves.reverse()
        compareStatesIDFS(possibleMoves)
    elif algorithm == "astar":  # astar
        compareStatesGreedy(possibleMoves)
    elif algorithm == "qlearning":  #qlearning
        return pM


def findSolution(state, algorithm):

    global max_depth
    global queue
    global visited
    global run2

    if args.v:
        # inits game
        pygame.get_init()

        # sets window caption
        pygame.display.set_caption("Box World 2")


    while run2:

        if algorithm == "idfs" and len(queue) == 0:
            queue = [State(Level(l), algorithm)]
            visited = []
            max_depth = max_depth + 10
            print("\n Retrying idfs with new depth limit: ",  max_depth, "\n")

        if algorithm == "greedy" or algorithm == "astar":
            state = queue.get()
        else:
            state = queue[0]

        # add node to already visited
        if algorithm == "greedy" or algorithm == "astar":
            visited.append(state)
        else:
            visited.append(queue[0])

        if args.v:
            # draws game state
        
            drawGameState(state.level)

            # Update the full Surface to the screen
            pygame.display.flip()

            screen.fill((0, 0, 0))

        # calculates next move
        nextMove(algorithm, state)

        # remove the first queue element
        if algorithm != "greedy" and algorithm != "astar":
            queue.remove(queue[0])

        # break condition
        if not run:
            print(solution.moves)
            break


def usage():
    print("""
Invalid arguments!

    Usage if you wish to play a level:
    > python3 game.py human <level>
    (where:
        <level> is a integer from 0 to 5)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% PROJECT 1 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%     
        
    Usage if you wish the AI to solve a level:
        > python3 game.py ai <level> -al <algorithm> -v <bool>
        (where:
            <level> a integer from 0 to 5
            <algorithm> is one of the folowing algorithms:
                - "bfs" -> breadth.first search
                - "dfs" -> depth-first search
                - "idfs" -> iterative depth-first search
                - "greedy" -> greedy algorithm
                - "astar" -> A* algorithm
            <bool> is a boolean (1, true, 0, false,)
                    this shows in which node the algorithm is
                    in real time but it is very costly performance wise.
                    Use it only in the lower levels that are quick to solve)



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% PROJECT 2 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    Usage if you wish the AI to solve a level with reinforcement learning:
        > python3 game.py ai <level> -alg <algorithm> -v <bool>
        (where:
            <level> a integer from 0 to 5
            <algorithm> is one of the folowing algorithms:
                - "qlearning"
                - "sarsa" 
            <bool> is a boolean (1, true, 0, false,)
                    this shows agent training in real time
                    but it is very costly performance-wise.
                    Use it only in the lower levels that are quick to solve)
        
        If you leave the command as showed above, the default values will be:
            alpha = 1
            epsilon = 0.3
            number of episodes = 500
            max steps per episode = 30

        If you wish to change this values you can use these optional flags
            "-alpha <float>" -> change alpha
            "-e <float>"     -> change epsilon
            "-ep <int>"      -> change nr episodes
            "-steps <int>"   -> change nr of steps per episode
        
        Example:
        >python3 game.py ai 0 -alg qlearning -v true -alpha 1 -e 0.2 -ep 250 -steps 25



            """

          )


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

# # ============================================== MAIN SCRIPT ==============================================


# initializes the screen 500x500
screen = pygame.display.set_mode((500, 500))

# Creates a clock object to keep track of time
clock = pygame.time.Clock()

# gets the level
parser = argparse.ArgumentParser(usage=usage())
parser.add_argument('mode', type=str, help='human/player')
parser.add_argument('level', type=int, help='Game level')
parser.add_argument('-algorithm', type=str,
                    help='Game algorithm', required=False)
parser.add_argument('-v', type=str2bool, required=False)
parser.add_argument('-alpha', type=float,help='alpha value 0..1', required=False)
parser.add_argument('-e', type=float, help='epsilon value 0..1', required=False)
parser.add_argument('-ep', type=int, help='Nr episodes', required=False)
parser.add_argument('-steps', type=int, help='Nr episodes', required=False)

args = parser.parse_args()





l = args.level

# specifies the level
level = Level(l)

# game states the player has already been in
visited = []

# current game state
state = State(level, args.algorithm)

alpha = 1
epsilon = 0.3
num_episodes = 500
max_steps_per_episode = 30

# queue with nodes
if args.algorithm == "greedy" or args.algorithm == "astar":
    
    queue = Q.PriorityQueue()
    queue.put(state)
else:
    queue = [state]

# initial state added to the queue

# creates movement
movement = pygame.Vector2(0, 0)

if args.mode == "human":

    # inits game
    pygame.get_init()

    # sets window caption
    pygame.display.set_caption("Box World 2")

    # Creates a clock object to keep track of time
    clock = pygame.time.Clock()

    state.level = Level(l)

    while True:

        # adds key functionality
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_r]:
            level = Level(l)

        if keys[pygame.K_ESCAPE]:
            run = False

        # creates movement vector that is later used for checking arena boundaries
        movement_player = pygame.Vector2(0, 0)

        if keys[pygame.K_LEFT]:
            movement_player = move(movement_player, "left")

        if keys[pygame.K_RIGHT]:
            movement_player = move(movement_player, "right")

        if keys[pygame.K_UP]:
            movement_player = move(movement_player, "up")

        if keys[pygame.K_DOWN]:
            movement_player = move(movement_player, "down")

        if keys[pygame.K_r]:
            state = State(Level(l))

        if keys[pygame.K_h]:
            state = State(Level(l))

            findSolution(state, "idfs")
            state = State(Level(l))

        # calculates next move
        calculateGameState(movement_player, state)

        pygame.time.delay(85)

        # draws game state
        drawGameState(state.level)

        # Update the full Surface to the screen
        pygame.display.flip()

        # Run the program at 60 frames per second
        clock.tick(60)

        screen.fill((0, 0, 0))

        # break condition
        if not run:
            break

# while loop
else:
    print("Solving this level using ", args.algorithm,
          "algorithm...\nThis shouldn't take long :)\nYou can also put \"-v true\" in the comand arguments to see the search in real time at cost of some performance...\n")
    start = time.time()

    if args.algorithm == "qlearning" or args.algorithm == "sarsa":
        
        if args.alpha:
            alpha = args.alpha
        
        if args.e:
            epsilon = args.e
            
        if args.ep:
            num_episodes = args.ep

        if args.steps:
            max_steps_per_episode = args.steps

        print("Please wait, I'm training ... ")

        graph1_x = []
        graph1_y = []

        graph2_x = []
        graph2_y = []
    

        state = State(Level(l), args.algorithm)
        qlearn = Qlearn()

        num_steps = 0

        for episode in range(num_episodes):
            # resets level 
            # might need to change later
            state = State(Level(l), args.algorithm)

            t = 1

            graph2_x.append(episode)



            for steps in range(max_steps_per_episode):

                graph1_x.append(episode)

                qlearn.addState(state)

                if args.v:
                    pygame.time.delay(0)

                    # draws game state
                    drawGameState(state.level)

                    # Update the full Surface to the screen
                    pygame.display.flip()

                    # Run the program at 60 frames per second
                    clock.tick(60)

                    screen.fill((0, 0, 0))
                
                # sees possible moves
                possibleMoves = nextMove("qlearning", state)

                # will get the max Qvalue to calculate the next position
                maxQvalue = [0, ""]

                # exploration vs exploitation
                if random.uniform(0, 1) < epsilon:
                    intMove = random.randint(0, 3)
                    if intMove == 0:
                        tmp = deepcopy(state)
                        tmp_movement = pygame.Vector2(-25, 0)
                        calculateGameState(tmp_movement, tmp)
                        qlearn.addState(tmp)
                        maxQvalue = [0, "left"]
                    elif intMove == 1:
                        tmp = deepcopy(state)
                        tmp_movement = pygame.Vector2(25, 0)
                        calculateGameState(tmp_movement, tmp)
                        qlearn.addState(tmp)
                        maxQvalue = [0, "right"]
                    elif intMove == 2:
                        tmp = deepcopy(state)
                        tmp_movement = pygame.Vector2(0, -25)
                        calculateGameState(tmp_movement, tmp)
                        qlearn.addState(tmp)
                        maxQvalue = [0, "up"]
                    elif intMove == 3:
                        tmp = deepcopy(state)
                        tmp_movement = pygame.Vector2(0, 25)
                        calculateGameState(tmp_movement, tmp)
                        qlearn.addState(tmp)
                        maxQvalue = [0, "down"]
                else:
                    
                    qValues = []
                    
                    # gets Q-Table values
                    for move in possibleMoves:
                        if move == "left":
                            tmp = deepcopy(state)
                            tmp_movement = pygame.Vector2(-25, 0)
                            calculateGameState(tmp_movement, tmp)
                            qlearn.addState(tmp)
                        elif move == "right":
                            tmp = deepcopy(state)
                            tmp_movement = pygame.Vector2(25, 0)
                            calculateGameState(tmp_movement, tmp)
                            qlearn.addState(tmp)
                        elif move == "up":
                            tmp = deepcopy(state)
                            tmp_movement = pygame.Vector2(0, -25)
                            calculateGameState(tmp_movement, tmp)
                            qlearn.addState(tmp)
                        elif move == "down":
                            tmp = deepcopy(state)
                            tmp_movement = pygame.Vector2(0, 25)
                            calculateGameState(tmp_movement, tmp)
                            qlearn.addState(tmp)
                        
                        qValues.append([qlearn.findQvalue(state, move), move])

                    # finds best move
                    maxiMax = -10000
                    for value in qValues:
                        if maxiMax < value[0]:
                            maxiMax = value[0]
                            maxQvalue = deepcopy(value)
                        if maxiMax == value[0]:
                            intMove = random.randint(0, 1)
                            if intMove == 0:
                                maxiMax = value[0]
                                maxQvalue = deepcopy(value)


                # calculates reward
                if maxQvalue[1] == "left":
                    if state.level.finish.collidelist(state.level.boxes) != -1:
                        reward = -20
                    elif (state.level.player.x - 25) == state.level.finish.x and state.level.player.y == state.level.finish.y :
                        reward = 10
                    else:
                        reward = -0.1

                    
                    

                elif maxQvalue[1] == "right":
                    if state.level.finish.collidelist(state.level.boxes) != -1:
                        reward = -20
                    elif (state.level.player.x + 25) == state.level.finish.x and state.level.player.y == state.level.finish.y :
                        reward = 10
                    else:
                        reward = -0.1

                    

                elif maxQvalue[1] == "up":
                    if state.level.finish.collidelist(state.level.boxes) != -1:
                        reward = -20
                    elif state.level.player.x == state.level.finish.x and (state.level.player.y - 25) == state.level.finish.y :
                        reward = 10
                    else:
                        reward = -0.1

                    

                elif maxQvalue[1] == "down":
                    if state.level.finish.collidelist(state.level.boxes) != -1:
                        reward = -20
                    elif state.level.player.x == state.level.finish.x and (state.level.player.y + 25) == state.level.finish.y :
                        reward = 10
                    else:
                        reward = -0.1

                    


                # test
                nextStates = []
                stateCmp1 = deepcopy(state)
                calculateGameState(pygame.Vector2(-25, 0), stateCmp1)
                nextStates.append(stateCmp1)
                stateCmp2 = deepcopy(state)
                calculateGameState(pygame.Vector2(25, 0), stateCmp2)
                nextStates.append(stateCmp2)
                stateCmp3 = deepcopy(state)
                calculateGameState(pygame.Vector2(0, -25), stateCmp3)
                nextStates.append(stateCmp3)
                stateCmp4 = deepcopy(state)
                calculateGameState(pygame.Vector2(0, 25), stateCmp4)
                nextStates.append(stateCmp4)


                # updates Q-Table
                qlearn.updateQtable(state, maxQvalue[1], reward, alpha, args.algorithm, epsilon, nextStates)
                buff = qlearn.getQentry(state)


                movement_player = pygame.Vector2(0, 0)
                if maxQvalue[1] == "left":
                    movement_player.x -= 25
                    graph1_y.append(buff[1])
                if maxQvalue[1] == "right":
                    movement_player.x += 25
                    graph1_y.append(buff[2])
                if maxQvalue[1] == "up":
                    movement_player.y -= 25
                    graph1_y.append(buff[3])
                if maxQvalue[1] == "down":
                    movement_player.y += 25
                    graph1_y.append(buff[4])

                # updates player position
                calculateGameState(movement_player, state)

                # if it reaches the exit resets level
                if state.level.player.colliderect(state.level.finish):
                    num_steps = steps
                    break

                if state.level.finish.collidelist(state.level.boxes) != -1:
                    num_steps = steps
                    break

                if steps == max_steps_per_episode - 1:
                    num_steps = steps

                
                



                t += 1.0

                alpha = pow(t, -0.1)

            
            graph2_y.append(num_steps)

                    

        #prints q_table
        for st1 in qlearn.q_table:
            print(st1[0].level.player.x, ",", st1[0].level.player.y, "\t", round(st1[1], 2), "\t", round(st1[2], 2), "\t", round(st1[3], 2), "\t", round(st1[4], 2))

        # ------------------------------------------------ from here we print the solution --------------------------------
        
        state = State(Level(l), "qlearning")


        limit = 25

        for step in range(limit):

            
            pygame.time.delay(300)

            # draws game state
            drawGameState(state.level)

            # Update the full Surface to the screen
            pygame.display.flip()

            # Run the program at 60 frames per second
            clock.tick(60)

            screen.fill((0, 0, 0))
            
            # sees possible moves
            possibleMoves = nextMove("qlearning", state)
            
            
            maxQvalue = [0, ""]
            qValues = []

            

            # gets Q-Table values
            for move in possibleMoves:
                qValues.append([qlearn.findQvalue(state, move), move])

            # finds best move
            maxi = -10000
            
            for value in qValues:
                if maxi < value[0]:
                    maxi = value[0]
                    maxQvalue = deepcopy(value)
                elif maxi == value[0]:
                    intMove = random.randint(0, 1)
                    if intMove == 0:
                        maxi = value[0]
                        maxQvalue = deepcopy(value)

            print("[", round(maxQvalue[0], 2), ", ", maxQvalue[1], "]")

            
            movement_player = pygame.Vector2(0, 0)
            if maxQvalue[1] == "left":
                movement_player.x -= 25
            if maxQvalue[1] == "right":
                movement_player.x += 25
            if maxQvalue[1] == "up":
                movement_player.y -= 25
            if maxQvalue[1] == "down":
                movement_player.y += 25

            # updates player position
            calculateGameState(movement_player, state)

            # if it reaches the exit resets level
            if state.level.player.colliderect(state.level.finish):
                break

        i = 0
        new_graph_x = []
        for x in graph1_x:
            i += 1
            new_graph_x.append(i)
        

        # draws graphs
        plt.plot(new_graph_x, graph1_y)
        #plt.plot(graph2_x, graph2_y)
        plt.show()


        #plot rewards
            # ------------------------------------------------ to here --------------------------------


    
    else:
        findSolution(state, args.algorithm)
        end = time.time()
        print("""
                Solution found!
                Showing solution on screen!""")

        print("\nA solution was found in ", round(end - start, 4), " s.")
        print("I looked through", len(visited), "nodes.")
        print("The solution has a cost of", len(solution.moves), "(moves).")

        #--------------------- Printing Solution --------------------#

        if not args.v:
            # inits game
            pygame.get_init()

            # sets window caption
            pygame.display.set_caption("Box World 2")

            # Creates a clock object to keep track of time
            clock = pygame.time.Clock()

        state.level = Level(l)

        state.moves = solution.moves

        while True:
            nextPlay = pygame.Vector2(0, 0)

            currentMove = state.moves[0]
            nextPlay = move(nextPlay, currentMove)
            calculateGameState(nextPlay, state)

            pygame.time.delay(500)

            # draws game state
            drawGameState(state.level)

            # Update the full Surface to the screen
            pygame.display.flip()

            # Run the program at 60 frames per second
            clock.tick(60)

            screen.fill((0, 0, 0))

            state.moves.pop(0)

            if not state.moves:
                break


pygame.quit()
