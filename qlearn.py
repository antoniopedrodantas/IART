def findQvalue(state, move):
    
    if move == "left":
        for tile in state.level.floor:
            if state.level.player.x == tile[0].x and state.level.player.y == tile[0].y:
                return tile[1]

    elif move == "right":
        for tile in state.level.floor:
            if state.level.player.x == tile[0].x and state.level.player.y == tile[0].y:
                return tile[2]

    elif move == "up":
        for tile in state.level.floor:
            if state.level.player.x == tile[0].x and state.level.player.y == tile[0].y:
                return tile[3]

    elif move == "down":
        for tile in state.level.floor:
            if state.level.player.x ==tile[0].x and state.level.player.y ==tile[0].y:
                return tile[4]



def updateQtable(state, move, reward):

    alpha = 0.8
    gamma = 0.3
    t = 1
    
    if move == "left":
        for tile in state.level.floor:
            if state.level.player.x == tile[0].x and state.level.player.y == tile[0].y:

                # calculates future reward
                futureRewards = []
                for next_tile in state.level.floor:
                    if (state.level.player.x - 25) == next_tile[0].x and state.level.player.y == next_tile[0].y:
                        futureRewards.append(next_tile[1])
                        futureRewards.append(next_tile[2])
                        futureRewards.append(next_tile[3])
                        futureRewards.append(next_tile[4])
                        break

                max = -10000
                for value in futureRewards:
                    if max < value:
                        max = value

                tile[1] = tile[1] + alpha * (reward + gamma * max - tile[1])
                #tile[1] = tile[1] + (reward + max)
                return state
                

    elif move == "right":
        for tile in state.level.floor:
            if state.level.player.x == tile[0].x and state.level.player.y == tile[0].y:

                # calculates future reward
                futureRewards = []
                for next_tile in state.level.floor:
                    if (state.level.player.x + 25) == next_tile[0].x and state.level.player.y == next_tile[0].y:
                        futureRewards.append(next_tile[1])
                        futureRewards.append(next_tile[2])
                        futureRewards.append(next_tile[3])
                        futureRewards.append(next_tile[4])
                        break

                max = -10000
                for value in futureRewards:
                    if max < value:
                        max = value

                tile[2] = tile[2] + alpha * (reward + gamma * max - tile[2])
                #tile[2] = tile[2] + (reward + max)
                return state
                

    elif move == "up":
        for tile in state.level.floor:
            if state.level.player.x == tile[0].x and state.level.player.y == tile[0].y:

                # calculates future reward
                futureRewards = []
                for next_tile in state.level.floor:
                    if state.level.player.x == next_tile[0].x and (state.level.player.y - 25) == next_tile[0].y:
                        futureRewards.append(next_tile[1])
                        futureRewards.append(next_tile[2])
                        futureRewards.append(next_tile[3])
                        futureRewards.append(next_tile[4])
                        break

                max = -10000
                for value in futureRewards:
                    if max < value:
                        max = value

                tile[3] = tile[3] + alpha * (reward + gamma * max - tile[3])
                #tile[3] = tile[3] + (reward + max)
                return state
                

    elif move == "down":
        for tile in state.level.floor:
            if state.level.player.x ==tile[0].x and state.level.player.y ==tile[0].y:

                # calculates future reward
                futureRewards = []
                for next_tile in state.level.floor:
                    if state.level.player.x == next_tile[0].x and (state.level.player.y + 25) == next_tile[0].y:
                        futureRewards.append(next_tile[1])
                        futureRewards.append(next_tile[2])
                        futureRewards.append(next_tile[3])
                        futureRewards.append(next_tile[4])
                        break

                max = -10000
                for value in futureRewards:
                    if max < value:
                        max = value

                tile[4] = tile[4] + alpha * (reward + gamma * max - tile[4])
                #tile[4] = tile[4] + (reward + max)
                return state

    
                
def showSolution(state):

    # ------------------------------------------------ from here --------------------------------

    while True:

        pygame.time.delay(100)

        # draws game state
        drawGameState(state.level)

        # Update the full Surface to the screen
        pygame.display.flip()

        # Run the program at 60 frames per second
        clock.tick(60)

        screen.fill((0, 0, 0))
        
        # sees possible moves
        possibleMoves = ["left", "right", "up", "down"]
        
        
        maxQvalue = [0, ""]
        qValues = []

        # gets Q-Table values
        for move in possibleMoves:
            qValues.append([qlearn.findQvalue(state, move), move])

        # finds best move
        max = -10000
        
        for value in qValues:
            if max < value[0]:
                max = value[0]
                maxQvalue = deepcopy(value)

        
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

        # ------------------------------------------------ to here --------------------------------
