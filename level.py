import pygame

class Level:

    def __init__(self, i):
        
        #level 1
        if(i == 1):
            self.player = pygame.Rect(325, 175, 25, 25)

            self.boxes = [
                pygame.Rect(175, 150, 25, 25),
                pygame.Rect(200, 175, 25, 25),
                pygame.Rect(225, 200, 25, 25),
                pygame.Rect(125, 150, 25, 25),
                pygame.Rect(150, 175, 25, 25),
                pygame.Rect(175, 200, 25, 25),
            ]

            self.iceBoxes = []

            self.floor = [
                pygame.Rect(125, 200, 225, 25),
                pygame.Rect(125, 150, 225, 25),
                pygame.Rect(125, 175, 225, 25),
            ]

            self.arena = [
                pygame.Rect(75, 125, 300, 25),
                pygame.Rect(75, 125, 25, 125),
                pygame.Rect(350, 125, 25, 125),
                pygame.Rect(100, 225, 250, 25),
                pygame.Rect(100, 150, 25, 25),
                pygame.Rect(100, 200, 25, 25)
            ]

            self.holes = []

            self.finish = pygame.Rect(100, 175, 25, 25)

        #level 2
        elif(i == 2):
            self.player = pygame.Rect(75, 175, 25, 25)

            self.boxes = [
                pygame.Rect(125, 125, 25, 25),
                pygame.Rect(150, 125, 25, 25),
                pygame.Rect(175, 125, 25, 25),
                pygame.Rect(200, 125, 25, 25),
                pygame.Rect(150, 150, 25, 25),
                pygame.Rect(200, 150, 25, 25),
                pygame.Rect(125, 175, 25, 25),
            ]

            self.iceBoxes = [
                pygame.Rect(150, 75, 25, 25),
                pygame.Rect(225, 75, 25, 25),
            ]

            self.floor = [
                pygame.Rect(75, 75, 200, 25),
                pygame.Rect(100, 100, 150, 25),
                pygame.Rect(125, 125, 100, 25),
                pygame.Rect(100, 150, 150, 25),
                pygame.Rect(75, 175, 200, 25),
            ]

            self.arena = [
                pygame.Rect(50, 50, 250, 25),
                pygame.Rect(50, 75, 25, 25),
                pygame.Rect(275, 75, 25, 25),
                pygame.Rect(50, 100, 50, 25),
                pygame.Rect(250, 100, 50, 25),
                pygame.Rect(50, 125, 75, 25),
                pygame.Rect(225, 125, 75, 25),
                pygame.Rect(50, 150, 50, 25),
                pygame.Rect(250, 150, 50, 25),
                pygame.Rect(275, 175, 25, 25),
                pygame.Rect(50, 175, 25, 25),
                pygame.Rect(50, 200, 250, 25),
            ]

            self.holes = [
                pygame.Rect(100, 75 ,25 ,25),
                pygame.Rect(250, 75 ,25 ,25),
                pygame.Rect(125, 150, 25, 25),
            ]

            self.finish = pygame.Rect(75, 75, 25, 25)



