import pygame

class State:
    
    def __init__(self, level):

        self.level = level

        self.moves = []

    
    def addMove(self, move):

        self.moves.append(move)
