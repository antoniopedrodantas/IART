import pygame
import math
import argparse

def manhattanDistance(s, start, finish):
    return (abs(start.x - finish.x) + abs(start.y - finish.y))
    
    
def getClosestBox(s):

    if len(s.level.boxes) == 0:
        return manhattanDistance(s, s.level.player, s.level.finish)

    lowest_value_index = 0

    for j in range(len(s.level.boxes)):
        if manhattanDistance(s, s.level.player, s.level.boxes[j]) < manhattanDistance(s, s.level.player, s.level.boxes[lowest_value_index]):
            lowest_value_index = j 


    return manhattanDistance(s, s.level.boxes[lowest_value_index], s.level.finish)

class State:
    
    
    def __init__(self, level, arg):

        self.level = level

        self.moves = []

        self.arg = arg



    
    def addMove(self, move):

        self.moves.append(move)


    def __lt__(self, other):
        if self.arg == "greedy":
            return math.sqrt(math.pow(self.level.player.x - self.level.finish.x, 2) + math.pow(self.level.player.y - self.level.finish.y, 2)) < math.sqrt(math.pow(other.level.player.x - other.level.finish.x, 2) + math.pow(other.level.player.y - other.level.finish.y, 2))
        elif self.arg == "astar":
            return getClosestBox(self) < getClosestBox(other)

