import pygame

class Level:

    def __init__(self, i):

        # ======================================= LEVEL 0 =======================================
        
        # level 0
        if(i == 0):
            self.player = pygame.Rect(100, 100, 25, 25)

            self.boxes = []

            self.iceBoxes = []

            self.floor = [
                [pygame.Rect(100, 100, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(100, 125, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(100, 150, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(100, 175, 25, 25), 0.0, 0.0, 0.0, 0.0],

                [pygame.Rect(125, 100, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(125, 125, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(125, 150, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(125, 175, 25, 25), 0.0, 0.0, 0.0, 0.0],

                [pygame.Rect(150, 100, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(150, 125, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(150, 150, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(150, 175, 25, 25), 0.0, 0.0, 0.0, 0.0],

                [pygame.Rect(175, 100, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(175, 125, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(175, 150, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(175, 175, 25, 25), 0.0, 0.0, 0.0, 0.0],

            ]

            self.arena = [
                pygame.Rect(75, 75, 150, 25),
                pygame.Rect(75, 75, 25, 150),
                pygame.Rect(75, 200, 150, 25),
                pygame.Rect(200, 75, 25, 150),

                pygame.Rect(150, 125, 25, 25),
                pygame.Rect(100, 125, 25, 25),
                pygame.Rect(100, 150, 25, 25),
                pygame.Rect(175, 175, 25, 25),
            ]

            self.holes = [
                
            ]

            self.finish = pygame.Rect(100, 175, 25, 25)

        # ======================================= LEVEL 0 =======================================

        #level 1
        elif(i == 1):
            self.player = pygame.Rect(300, 175, 25, 25)

            self.boxes = [
                #pygame.Rect(175, 150, 25, 25),
                #pygame.Rect(200, 175, 25, 25),
                #pygame.Rect(225, 200, 25, 25),
                #pygame.Rect(125, 150, 25, 25),
                #pygame.Rect(150, 175, 25, 25),
                #pygame.Rect(175, 200, 25, 25),
            ]

            self.iceBoxes = []

            self.floor = [
                #pygame.Rect(125, 200, 225, 25),
                #pygame.Rect(125, 150, 225, 25),
                #pygame.Rect(125, 175, 225, 25),
                
                [pygame.Rect(125, 200, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(150, 200, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(175, 200, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(200, 200, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(225, 200, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(250, 200, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(275, 200, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(300, 200, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(325, 200, 25, 25), 0.0, 0.0, 0.0, 0.0],

                [pygame.Rect(125, 175, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(150, 175, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(175, 175, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(200, 175, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(225, 175, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(250, 175, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(275, 175, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(300, 175, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(325, 175, 25, 25), 0.0, 0.0, 0.0, 0.0],

                [pygame.Rect(125, 150, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(150, 150, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(175, 150, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(200, 150, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(225, 150, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(250, 150, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(275, 150, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(300, 150, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(325, 150, 25, 25), 0.0, 0.0, 0.0, 0.0],

                [pygame.Rect(100, 150, 25, 25), 0.0, 0.0, 0.0, 0.0],
                [pygame.Rect(100, 200, 25, 25), 0.0, 0.0, 0.0, 0.0],

            ]

            self.arena = [
                pygame.Rect(75, 125, 300, 25),
                pygame.Rect(75, 125, 25, 125),
                pygame.Rect(350, 125, 25, 125),
                pygame.Rect(100, 225, 250, 25),
                #pygame.Rect(100, 150, 25, 25),
                #pygame.Rect(100, 200, 25, 25)
            ]

            self.holes = []

            self.finish = pygame.Rect(100, 175, 25, 25)

        # ======================================= LEVEL 2 =======================================

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

        # ======================================= LEVEL 3 =======================================
        
        #level 3
        if(i == 3):
            self.player = pygame.Rect(200, 300, 25, 25)

            self.boxes = [
                pygame.Rect(200, 275, 25, 25),
                pygame.Rect(175, 250, 25, 25),
                pygame.Rect(225, 250, 25, 25),
                pygame.Rect(175, 225, 25, 25),
                pygame.Rect(200, 200, 25, 25),
                pygame.Rect(250, 200, 25, 25),
                pygame.Rect(225, 175, 25, 25),
            ]

            self.iceBoxes = []

            self.floor = [
                pygame.Rect(175, 150, 25, 200),
                pygame.Rect(200, 150, 25, 200),
                pygame.Rect(225, 150, 25, 200),
                pygame.Rect(250, 150, 25, 200),
            ]

            self.arena = [
                pygame.Rect(150, 325, 150, 25),
                pygame.Rect(150, 150, 25, 175),
                pygame.Rect(150, 150, 75, 25),
                pygame.Rect(250, 150, 50, 25),
                pygame.Rect(275, 150, 25, 200),
            ]

            self.holes = [
                pygame.Rect(200, 250, 25, 25),
                pygame.Rect(200, 225, 25, 25),
                pygame.Rect(225, 225, 25, 25),
                pygame.Rect(225, 200, 25, 25),
            ]

            self.finish = pygame.Rect(225, 150, 25, 25)

        # ======================================= LEVEL 4 =======================================

        #level 4
        if(i == 4):
            self.player = pygame.Rect(250, 100, 25, 25)

            self.boxes = [
                pygame.Rect(225, 125, 25, 25),
                pygame.Rect(275, 125, 25, 25),
                pygame.Rect(250, 150, 25, 25),
                pygame.Rect(225, 175, 25, 25),
                pygame.Rect(275, 175, 25, 25),
                pygame.Rect(250, 200, 25, 25),

                pygame.Rect(225, 275, 25, 25),
                pygame.Rect(250, 275, 25, 25),
                pygame.Rect(275, 275, 25, 25),
            ]

            self.iceBoxes = []

            self.floor = [
                pygame.Rect(200, 75, 25, 275),
                pygame.Rect(225, 75, 25, 275), 
                pygame.Rect(250, 75, 25, 275),
                pygame.Rect(275, 75, 25, 275),
                pygame.Rect(300, 75, 25, 275),
            ]

            self.arena = [
                pygame.Rect(175, 75, 175, 25), #h t
                pygame.Rect(175, 75, 25, 275), #v l
                pygame.Rect(325, 75, 25, 275), #v r
                pygame.Rect(175, 325, 75, 25), #h b 1
                pygame.Rect(275, 325, 75, 25), #h b 2
            ]

            self.holes = [
                pygame.Rect(225, 150, 25, 25),
                pygame.Rect(275, 150, 25, 25),

                pygame.Rect(200, 175, 25, 25),
                pygame.Rect(250, 175, 25, 25),
                pygame.Rect(300, 175, 25, 25),

                pygame.Rect(200, 200, 25, 25),
                pygame.Rect(225, 200, 25, 25),
                pygame.Rect(275, 200, 25, 25),
                pygame.Rect(300, 200, 25, 25),

                pygame.Rect(200, 225, 25, 25),
                pygame.Rect(225, 225, 25, 25),
                pygame.Rect(250, 225, 25, 25),
                pygame.Rect(275, 225, 25, 25),
                pygame.Rect(300, 225, 25, 25),

                pygame.Rect(200, 250, 25, 25),
                pygame.Rect(225, 250, 25, 25),
                pygame.Rect(250, 250, 25, 25),
                pygame.Rect(275, 250, 25, 25),
                pygame.Rect(300, 250, 25, 25),

                pygame.Rect(200, 275, 25, 25),
                pygame.Rect(300, 275, 25, 25),

                pygame.Rect(200, 300, 25, 25),
                pygame.Rect(300, 300, 25, 25),
            ]

            self.finish = pygame.Rect(250, 325, 25, 25)
        

        # ======================================= LEVEL 5 =======================================
        
        #level 5
        if(i == 5):
            self.player = pygame.Rect(200, 250, 25, 25)

            self.boxes = [
                pygame.Rect(275, 250, 25, 25),
                pygame.Rect(275, 325, 25, 25),
                pygame.Rect(350, 250, 25, 25),
            ]

            self.iceBoxes = []

            self.floor = [
                pygame.Rect(200, 150, 25, 200),
                pygame.Rect(225, 150, 25, 200),
                pygame.Rect(250, 150, 25, 225),
                pygame.Rect(275, 150, 25, 225),
                pygame.Rect(300, 150, 25, 225),
                pygame.Rect(325, 150, 25, 225),
                pygame.Rect(350, 150, 25, 175),
                pygame.Rect(375, 150, 25, 175),
            ]

            self.arena = [
                pygame.Rect(175, 150, 25, 200), #v l
                pygame.Rect(175, 150, 225, 25), #h t
                
                pygame.Rect(175, 350, 75, 25),
                pygame.Rect(225, 375, 125, 25), #h b
                pygame.Rect(325, 325, 25, 75),

                pygame.Rect(400, 150, 25, 25), #v r
                pygame.Rect(400, 200, 25, 125), #v r
                pygame.Rect(375, 200, 25, 25), #v r
                pygame.Rect(375, 225, 25, 25), #v r
                
                pygame.Rect(300, 300, 125, 25),
                pygame.Rect(300, 275, 25, 50),

                #middle
                pygame.Rect(225, 200, 25, 125), 
                pygame.Rect(225, 200, 100, 25),
                pygame.Rect(225, 300, 50, 25),
                pygame.Rect(300, 225, 50, 25),   

                #block exit
                pygame.Rect(425, 150, 25, 75),
            ]

            self.holes = [
                pygame.Rect(350, 200, 25, 25),
                pygame.Rect(350, 175, 25, 25),
                pygame.Rect(375, 175, 25, 25),
            ]

            self.finish = pygame.Rect(400, 175, 25, 25)


        # ======================================= LEVEL 5 =======================================

        #level 6
        if(i == 6):
            
            self.player = pygame.Rect(150, 200, 25, 25)

            self.boxes = [
                pygame.Rect(325, 175, 25, 25),
            ]

            self.iceBoxes = [
                pygame.Rect(225, 200, 25, 25),
                pygame.Rect(225, 250, 25, 25),
                pygame.Rect(275, 200, 25, 25),
                pygame.Rect(275, 250, 25, 25),
            ]

            self.floor = [
                pygame.Rect(150, 150, 25, 100),
                pygame.Rect(175, 150, 25, 200),
                pygame.Rect(200, 150, 25, 200),
                pygame.Rect(225, 150, 25, 200),
                pygame.Rect(250, 150, 25, 200),
                pygame.Rect(275, 150, 25, 200),
                pygame.Rect(300, 150, 25, 200),
                pygame.Rect(325, 150, 25, 200),
            ]

            self.arena = [
                pygame.Rect(175, 200, 25, 25),
                pygame.Rect(175, 225, 25, 25),
                pygame.Rect(150, 225, 25, 25),
                pygame.Rect(125, 150, 25, 100),
                pygame.Rect(150, 150, 225, 25),
                pygame.Rect(350, 150, 25, 200),
                pygame.Rect(325, 325, 25, 25),
                pygame.Rect(175, 325, 125, 25),
                pygame.Rect(250, 175, 25, 25),
                pygame.Rect(275, 350, 75, 25),

                pygame.Rect(175, 250, 25, 75),
            ]

            self.holes = [
                pygame.Rect(200, 275, 25, 25),
                pygame.Rect(225, 275, 25, 25),
                pygame.Rect(250, 275, 25, 25),
                pygame.Rect(275, 275, 25, 25),
                pygame.Rect(300, 275, 25, 25),
                pygame.Rect(325, 275, 25, 25),

                pygame.Rect(200, 300, 25, 25),
                pygame.Rect(225, 300, 25, 25),
                pygame.Rect(250, 300, 25, 25),
                pygame.Rect(275, 300, 25, 25),
                pygame.Rect(300, 300, 25, 25),
            ]

            self.finish = pygame.Rect(300, 325, 25, 25)

       

    
    def __eq__(self, other):

        return self.player == other.player and self.boxes == other.boxes and self.iceBoxes == other.iceBoxes and self.holes == other.holes

    def __nq__(self, other):

        return self.player == other.player and self.boxes == other.boxes and self.iceBoxes == other.iceBoxes and self.holes == other.holes



