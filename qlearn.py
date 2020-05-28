import random
    
                
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

    
    def getState(self, state):

        for st in self.q_table:
            if st[0].level == state.level:
                return st[0]

        return null


    
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

    
    
    
    def updateQtable(self, state, move, reward, alpha, algorithm, epsilon, nextStates):

        gamma = 0.9
        
        
        if move == "left":
            for q_instance in self.q_table:
                if state.level == q_instance[0].level and state.level == q_instance[0].level:

                    # calculates future reward
                    futureRewards = []
                    '''
                    for next_state in self.q_table:
                        if (state.level.player.x - 25) == next_state[0].level.player.x and state.level.player.y == next_state[0].level.player.y:
                            futureRewards.append(next_state[1])
                            futureRewards.append(next_state[2])
                            futureRewards.append(next_state[3])
                            futureRewards.append(next_state[4])
                            break
                    '''
                    for next_state in self.q_table:
                        tmp = self.getState(nextStates[0])
                        if tmp.level == next_state[0].level:
                            futureRewards.append(next_state[1])
                            futureRewards.append(next_state[2])
                            futureRewards.append(next_state[3])
                            futureRewards.append(next_state[4])
                            break

                    maxi = -10000
                    for value in futureRewards:
                        if maxi < value:
                            maxi = value
                        if maxi == value:
                            intMove = random.randint(0, 1)
                            if intMove == 0:
                                maxi = value
                    
                    if len(futureRewards) == 0:
                        maxi = 0

                    
                    if algorithm == "sarsa":
                        if len(futureRewards) > 0:
                            mean = (futureRewards[0] + futureRewards[1] + futureRewards[2] + futureRewards[3]) / 4
                            maxi = (epsilon * mean) + ((1 - epsilon) * maxi)
                        else:
                            mean = 0
                            maxi = (epsilon * mean) + ((1 - epsilon) * maxi)

                    
                    q_instance[1] = q_instance[1] + alpha * (reward + gamma * maxi - q_instance[1])


        elif move == "right":
            for q_instance in self.q_table:
                if state.level == q_instance[0].level and state.level == q_instance[0].level:
                    # calculates future reward
                    futureRewards = []
                    '''
                    for next_state in self.q_table:
                        if (state.level.player.x + 25) == next_state[0].level.player.x and state.level.player.y == next_state[0].level.player.y:
                            futureRewards.append(next_state[1])
                            futureRewards.append(next_state[2])
                            futureRewards.append(next_state[3])
                            futureRewards.append(next_state[4])
                            break
                    '''
                    for next_state in self.q_table:
                        tmp = self.getState(nextStates[1])
                        if tmp.level == next_state[0].level:
                            futureRewards.append(next_state[1])
                            futureRewards.append(next_state[2])
                            futureRewards.append(next_state[3])
                            futureRewards.append(next_state[4])
                            break

                    maxi = -10000
                    for value in futureRewards:
                        if maxi < value:
                            maxi = value
                        if maxi == value:
                            intMove = random.randint(0, 1)
                            if intMove == 0:
                                maxi = value

                    if len(futureRewards) == 0:
                        maxi = 0

                    
                    if algorithm == "sarsa":
                        if len(futureRewards) > 0:
                            mean = (futureRewards[0] + futureRewards[1] + futureRewards[2] + futureRewards[3]) / 4
                            maxi = (epsilon * mean) + ((1 - epsilon) * maxi)
                        else:
                            mean = 0
                            maxi = (epsilon * mean) + ((1 - epsilon) * maxi)

                    q_instance[2] = q_instance[2] + alpha * (reward + gamma * maxi - q_instance[2])
                    

        elif move == "up":
            for q_instance in self.q_table:
                if state.level == q_instance[0].level and state.level == q_instance[0].level:
                    # calculates future reward
                    futureRewards = []
                    '''
                    for next_state in self.q_table:
                        if state.level.player.x == next_state[0].level.player.x and (state.level.player.y - 25) == next_state[0].level.player.y:
                            futureRewards.append(next_state[1])
                            futureRewards.append(next_state[2])
                            futureRewards.append(next_state[3])
                            futureRewards.append(next_state[4])
                            break
                    '''
                    for next_state in self.q_table:
                        tmp = self.getState(nextStates[2])
                        if tmp.level == next_state[0].level:
                            futureRewards.append(next_state[1])
                            futureRewards.append(next_state[2])
                            futureRewards.append(next_state[3])
                            futureRewards.append(next_state[4])
                            break
                    
                    maxi = -10000
                    for value in futureRewards:
                        if maxi < value:
                            maxi = value
                        if maxi == value:
                            intMove = random.randint(0, 1)
                            if intMove == 0:
                                maxi = value

                    if len(futureRewards) == 0:
                        maxi = 0

                    
                    if algorithm == "sarsa":
                        if len(futureRewards) > 0:
                            mean = (futureRewards[0] + futureRewards[1] + futureRewards[2] + futureRewards[3]) / 4
                            maxi = (epsilon * mean) + ((1 - epsilon) * maxi)
                        else:
                            mean = 0
                            maxi = (epsilon * mean) + ((1 - epsilon) * maxi)


                    q_instance[3] = q_instance[3] + alpha * (reward + gamma * maxi - q_instance[3])
                    

        elif move == "down":
            for q_instance in self.q_table:
                if state.level == q_instance[0].level and state.level == q_instance[0].level:

                    # calculates future reward
                    futureRewards = []
                    '''
                    for next_state in self.q_table:
                        if state.level.player.x == next_state[0].level.player.x and (state.level.player.y + 25) == next_state[0].level.player.y:
                            futureRewards.append(next_state[1])
                            futureRewards.append(next_state[2])
                            futureRewards.append(next_state[3])
                            futureRewards.append(next_state[4])
                            break
                    '''
                    for next_state in self.q_table:
                        tmp = self.getState(nextStates[3])
                        if tmp.level == next_state[0].level:
                            futureRewards.append(next_state[1])
                            futureRewards.append(next_state[2])
                            futureRewards.append(next_state[3])
                            futureRewards.append(next_state[4])
                            break

                    maxi = -10000
                    for value in futureRewards:
                        if maxi < value:
                            maxi = value
                        if maxi == value:
                            intMove = random.randint(0, 1)
                            if intMove == 0:
                                maxi = value

                    if len(futureRewards) == 0:
                        maxi = 0

                    
                    if algorithm == "sarsa":
                        if len(futureRewards) > 0:
                            mean = (futureRewards[0] + futureRewards[1] + futureRewards[2] + futureRewards[3]) / 4
                            maxi = (epsilon * mean) + ((1 - epsilon) * maxi)
                        else:
                            mean = 0
                        maxi = (epsilon * mean) + ((1 - epsilon) * maxi)

                    q_instance[4] = q_instance[4] + alpha * (reward + gamma * maxi - q_instance[4])


        

    
