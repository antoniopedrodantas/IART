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

    discount_rate = 0.3
    alpha = 1
    t = 1
    
    if move == "left":
        for tile in state.level.floor:
            if state.level.player.x == tile[0].x and state.level.player.y == tile[0].y:
                tile[1] = tile[1] + reward
                return state
                

    elif move == "right":
        for tile in state.level.floor:
            if state.level.player.x == tile[0].x and state.level.player.y == tile[0].y:
                tile[2] = tile[2] + reward
                return state
                

    elif move == "up":
        for tile in state.level.floor:
            if state.level.player.x == tile[0].x and state.level.player.y == tile[0].y:
                tile[3] = tile[3] + reward
                return state
                

    elif move == "down":
        for tile in state.level.floor:
            if state.level.player.x ==tile[0].x and state.level.player.y ==tile[0].y:
                tile[4] = tile[4] + reward
                return state

    
                
