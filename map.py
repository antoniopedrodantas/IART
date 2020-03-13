# Allows the usage of the PyGame library
import pygame

# Initializes all PyGame modules
pygame.init()

# Barrier
minimum_x = 342

# Initializes the window's title, width, and height
pygame.display.set_caption("Farm Game")
screen = pygame.display.set_mode((720, 320))

fences = (
    pygame.Rect(255, 65, 20, 85),
    pygame.Rect(190, 65, 85, 20),
    pygame.Rect(290, 0, 20, 85),
    pygame.Rect(295, 0, 240, 20),
    pygame.Rect(415, 0, 20, 150),
    pygame.Rect(380, 130, 40, 20),
    pygame.Rect(255, 130, 80, 20)
)

# player coords
char = pygame.Rect(507, 60, 25, 40)

# Keeps the while loop running
done = False

# Boolean to identify whether the player has unlocked the currently locked area
unlocked = False

# Creates a clock object to keep track of time
clock = pygame.time.Clock()

# Keeps the program running
while not done:
    # Allows the user to exit by pressing the X button without throwing an error
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #       Logic Area

    # Assigns a list of the possible pressed keys to a variable
    pressed = pygame.key.get_pressed()

    speed = 3
    movement = pygame.Vector2(0, 0)
    # If the UP key is pressed, move the player upwards
    if pressed[pygame.K_UP] and not pressed[pygame.K_DOWN]:
        movement.y -= speed

    # If the DOWN key is pressed, move the player downwards
    if pressed[pygame.K_DOWN] and not pressed[pygame.K_UP]:
        movement.y += speed

    # If the LEFT key is pressed, move the player to the left
    if pressed[pygame.K_LEFT] and not pressed[pygame.K_RIGHT]:
        movement.x -= speed

    # If the RIGHT key is pressed, move the player to the right
    if pressed[pygame.K_RIGHT] and not pressed[pygame.K_LEFT]:
        movement.x += speed

    if movement.x != 0 or movement.y != 0:
        # Deflate. Where 3 pixels away from edge
        rect = screen.get_rect().inflate(-6, -6)
        moved = char.move(movement.x, movement.y)
        if moved.collidelist(fences) == -1 and rect.contains(moved):
            char = moved

    # Draw Area
    # Place the background image on the window
    screen.fill((0,0,0))

    # Puts the fences on the screen
    for fence in fences:
        pygame.draw.rect(screen, pygame.Color('red'), fence)

    pygame.draw.rect(screen, pygame.Color('red'), char)

    # Update the full Surface to the screen
    pygame.display.flip()

    # Run the program at 60 frames per second
    clock.tick(60)
