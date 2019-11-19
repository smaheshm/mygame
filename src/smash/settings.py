# settings for my game (smash.py)

# dimension of the game window
WIDTH = 1240
LENGTH = 860

# frames per second (how fast the game loop runs)
FPS = 60

# colors (RBG)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)
WHITE = (255, 255, 255)
LIGHTBLUE = (0, 155, 155)

# platform LENGTH
PLATFORM_LIST = [(WIDTH-200, 30, 100, LENGTH - 150),
                 (250, 25, 200, LENGTH-310),
                 (250, 25, WIDTH-450, LENGTH-310),
                  (125, 20, (WIDTH/2)-62.5, LENGTH-450)]

# for player movement
PLAYER_ACC = 1.0
PLAYER_FRICTION = -0.12
GRAVITY = 0.8
PLAYER_JUMP = 20

FONT_NAME = 'arial'