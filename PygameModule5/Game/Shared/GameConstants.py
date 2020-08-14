import os

class GameConstants:
    BRICK_SIZE = [100, 30]
    SCREEN_SIZE = [800, 600]
    BALL_SIZE = [16, 16]
    BULLET_SIZE = [14, 16]
    #BALL_SIZE = [32, 32]
    SHIP_SIZE = [32, 30]
    BACKGROUND_SIZE = [5, 5]
    SPRITE_SHIP = os.path.join("Game", "Assets", "GalagaShip32.png")

    SPRITE_BALL = os.path.join("Game", "Assets", "ball.png")
    SPRITE_BULLET = os.path.join("Game", "Assets", "bullet.png")
    #SPRITE_BALL = os.path.join("Game", "Assets", "GalagaShip32.png")
    SPRITE_BRICK = os.path.join("Game", "Assets", "alien_pink.png")
    SPRITE_SPEEDBRICK = os.path.join("Game", "Assets", "alien_green.png")
    SPRITE_LIFEBRICK = os.path.join("Game", "Assets", "life.png")   
    SPRITE_HIGHSCORE = os.path.join("Game", "Assets", "highscore.png") 
    SPRITE_BACKGROUND_1 = os.path.join("Game", "Assets", "background_pixel_blue.png") 
    SPRITE_BACKGROUND_2 = os.path.join("Game", "Assets", "background_pixel_green.png") 
    SPRITE_BACKGROUND_3 = os.path.join("Game", "Assets", "background_pixel_red.png") 



    
    PLAYING_SCENE = 0
    GAMEOVER_SCENE = 1
    HIGHSCORE_SCENE = 2
    MENU_SCENE = 3