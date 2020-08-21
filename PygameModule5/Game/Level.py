import os
import fileinput
import pygame

from Game.Bricks import *
from Game.Shared import *

class Level:

    def __init__(self, game):
        #create and set private member vars
        self.__game = game
        self.__enemies = []
        self.__amountOfEnemiesLeft = 0
        self.__currentLevel = 0

        #methods
    def getEnemies(self):
        return self.__enemies

    def getAmountOfEnemiesLeft(self):
        return self.__amountOfEnemiesLeft

    def enemyHit(self):
        self.__amountOfEnemiesLeft -= 1

    def loadNextLevel(self):
        pass

    def load(self, level):
        self.__currentLevel = level
        self.__enemies = []

        x, y = 0, 0

        for line in fileinput.input(os.path.join("Game", "Assets", "Levels" , "level" + str(level) + ".dat")):
            for currentEnemy in line:
                if currentEnemy == "1":
                    enemy = Enemy([x, y], pygame.image.load(GameConstants.SPRITE_ENEMY), self.__game)
                    self.__enemies.append(enemy)
                    self.__amountOfEnemiesLeft += 1

                #elif currentEnemy == "2":
                #    enemy = SpeedBrick([x, y], pygame.image.load(GameConstants.SPRITE_SPEEDBRICK), self.__game)
                #    self.__enemies.append(enemy)
                #    self.__amountOfEnemiesLeft += 1

                #elif currentEnemy == "3":
                #    enemy = LifeBrick([x, y], pygame.image.load(GameConstants.SPRITE_LIFEBRICK), self.__game)
                #    self.__enemies.append(enemy)
                #    self.__amountOfEnemiesLeft += 1

                x += GameConstants.ENEMY_SIZE[0]
                
            x = 0
            y += GameConstants.ENEMY_SIZE[1]

