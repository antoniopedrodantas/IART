'''
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
'''
    
                
class Qlearn:



    def __init__(self):

        self.q_table = []
        self.states = []

    
    def addState(self, state):
        
        for st in self.states:
            if st.level == state.level:
                return -1

        self.states.append(state)
        self.q_table.append([state, 0.0, 0.0, 0.0, 0.0])

        return 0

    
    def findQvalue(self, state, move):
    
        if move == "left":
            for q_instance in self.q_table:
                #if state.level.player.x == q_instance[0].level.player.x and state.level.player.y == q_instance[0].level.player.y:
                if state.level == q_instance[0].level:

                    return q_instance[1]

        elif move == "right":
            for q_instance in self.q_table:
                if state.level == q_instance[0].level:
                    return q_instance[2]

        elif move == "up":
            for q_instance in self.q_table:
                if state.level == q_instance[0].level:
                    return q_instance[3]

        if move == "down":
            for q_instance in self.q_table:
                if state.level == q_instance[0].level:
                    return q_instance[4]

    
    
    
    def updateQtable(self, state, move, reward, alpha):

        gamma = 0.9
        
        if move == "left":
            for q_instance in self.q_table:
                if state.level == q_instance[0].level and state.level == q_instance[0].level:

                    # calculates future reward
                    futureRewards = []
                    for next_state in self.q_table:
                        if (state.level.player.x - 25) == next_state[0].level.player.x and state.level.player.y == next_state[0].level.player.y:
                            futureRewards.append(next_state[1])
                            futureRewards.append(next_state[2])
                            futureRewards.append(next_state[3])
                            futureRewards.append(next_state[4])
                            break

                    maxi = -10000
                    for value in futureRewards:
                        if maxi < value:
                            maxi = value

                    
                    q_instance[1] = q_instance[1] + alpha * (reward + gamma * maxi - q_instance[1])


        elif move == "right":
            for q_instance in self.q_table:
                if state.level == q_instance[0].level and state.level == q_instance[0].level:
                    # calculates future reward
                    futureRewards = []
                    for next_state in self.q_table:
                        if (state.level.player.x + 25) == next_state[0].level.player.x and state.level.player.y == next_state[0].level.player.y:
                            futureRewards.append(next_state[1])
                            futureRewards.append(next_state[2])
                            futureRewards.append(next_state[3])
                            futureRewards.append(next_state[4])
                            break

                    maxi = -10000
                    for value in futureRewards:
                        if maxi < value:
                            maxi = value

                    q_instance[2] = q_instance[2] + alpha * (reward + gamma * maxi - q_instance[2])
                    

        elif move == "up":
            for q_instance in self.q_table:
                if state.level == q_instance[0].level and state.level == q_instance[0].level:
                    # calculates future reward
                    futureRewards = []
                    for next_state in self.q_table:
                        if state.level.player.x == next_state[0].level.player.x and (state.level.player.y - 25) == next_state[0].level.player.y:
                            futureRewards.append(next_state[1])
                            futureRewards.append(next_state[2])
                            futureRewards.append(next_state[3])
                            futureRewards.append(next_state[4])
                            break

                    maxi = -10000
                    for value in futureRewards:
                        if maxi < value:
                            maxi = value

                    q_instance[3] = q_instance[3] + alpha * (reward + gamma * maxi - q_instance[3])
                    

        elif move == "down":
            for q_instance in self.q_table:
                if state.level == q_instance[0].level and state.level == q_instance[0].level:

                    # calculates future reward
                    futureRewards = []
                    for next_state in self.q_table:
                        if state.level.player.x == next_state[0].level.player.x and (state.level.player.y + 25) == next_state[0].level.player.y:
                            futureRewards.append(next_state[1])
                            futureRewards.append(next_state[2])
                            futureRewards.append(next_state[3])
                            futureRewards.append(next_state[4])
                            break

                    maxi = -10000
                    for value in futureRewards:
                        if maxi < value:
                            maxi = value

                    q_instance[4] = q_instance[4] + alpha * (reward + gamma * maxi - q_instance[4])


        

    
