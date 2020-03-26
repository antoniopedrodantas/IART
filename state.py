import pygame
import math

class State:
    
    def __init__(self, level):

        self.level = level

        self.moves = []

    
    def addMove(self, move):

        self.moves.append(move)

    def __lt__(self, other):

        return math.sqrt(math.pow(self.level.player.x - self.level.finish.x, 2) + math.pow(self.level.player.y - self.level.finish.y, 2)) < math.sqrt(math.pow(other.level.player.x - other.level.finish.x, 2) + math.pow(other.level.player.y - other.level.finish.y, 2))
