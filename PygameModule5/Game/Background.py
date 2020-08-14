import pygame
import random

from Game.Shared import *

class Background(GameObject):
    def __init__(self, position, sprite, game):
        self.__game = game
        self._position = 0
        self.__sprite = sprite
        self._random = random.seed(100)
        super(Background, self).__init__(position, (GameConstants.BACKGROUND_SIZE), sprite)

    def getGame(self):
        return self.__game

    def updatePosition(self):
        newPosition = (random.randrange(GameConstants.SCREEN_SIZE[0]), random.randrange(GameConstants.SCREEN_SIZE[1]))
        self.setPosition(newPosition)

    def getSprite(self):
        return self.__sprite
