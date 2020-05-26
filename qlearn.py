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



def updateQtable(state, move, reward, alpha):

    gamma = 0.9
    
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

                maxi = -10000
                for value in futureRewards:
                    if maxi < value:
                        maxi = value

                tile[1] = tile[1] * (1 - alpha) + alpha * (reward + gamma * maxi)
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

                maxi = -10000
                for value in futureRewards:
                    if maxi < value:
                        maxi = value

                tile[2] = tile[2] * (1 - alpha) + alpha * (reward + gamma * maxi)
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

                maxi = -10000
                for value in futureRewards:
                    if maxi < value:
                        maxi = value

                tile[3] = tile[3] * (1 - alpha) + alpha * (reward + gamma * maxi)
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

                maxi = -10000
                for value in futureRewards:
                    if maxi < value:
                        maxi = value

                tile[4] = tile[4] * (1 - alpha) + alpha * (reward + gamma * maxi)
                return state

    
                
