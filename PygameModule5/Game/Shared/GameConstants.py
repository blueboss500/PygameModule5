import os

class GameConstants:
    BRICK_SIZE = [100, 30]
    SCREEN_SIZE = [800, 600]
    BALL_SIZE = [16, 16]
    #BALL_SIZE = [32, 32]
    SHIP_SIZE = [32, 30]
    SPRITE_SHIP = os.path.join("Game", "Assets", "GalagaShip32.png")

    SPRITE_BALL = os.path.join("Game", "Assets", "ball.png")
    #SPRITE_BALL = os.path.join("Game", "Assets", "GalagaShip32.png")
    SPRITE_BRICK = os.path.join("Game", "Assets", "standard.png")
    SPRITE_SPEEDBRICK = os.path.join("Game", "Assets", "speed.png")
    SPRITE_LIFEBRICK = os.path.join("Game", "Assets", "life.png")   
    SPRITE_HIGHSCORE = os.path.join("Game", "Assets", "highscore.png") 
    
    PLAYING_SCENE = 0
    GAMEOVER_SCENE = 1
    HIGHSCORE_SCENE = 2
    MENU_SCENE = 3