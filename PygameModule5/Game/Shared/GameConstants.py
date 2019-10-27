import os

class GameConstants:
    BRICK_SIZE = [100, 30]
    SCREEN_SIZE = [800, 600]
    BALL_SIZE = [16, 16]
    PAD_SIZE = [139, 13]
    SPRITE_PAD = os.path.join("Game", "Assets", "pad.png")

    SPRITE_BALL = os.path.join("Game", "Assets", "ball.png")
    SPRITE_BRICK = os.path.join("Game", "Assets", "standard.png")
    SPRITE_SPEEDBRICK = os.path.join("Game", "Assets", "speed.png")
    SPRITE_LIFEBRICK = os.path.join("Game", "Assets", "life.png")