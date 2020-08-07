import pygame
from Game.Scenes import Scene
from Game.Shared import *

class PlayingGameScene(Scene):

    def __init__(self, game):
        super(PlayingGameScene, self).__init__(game)

    def render(self):
        super(PlayingGameScene, self).render()

        game = self.getGame()

        if game.getLives() <= 0:
            game.changeScene(GameConstants.GAMEOVER_SCENE)

        bullets = game.getBullets()
        ship = game.getShip()

        #render balls
        for bullet in bullets:
           

            for brick in game.getLevel().getBricks():
                if not brick.isDestroyed() and bullet.intersects(brick):
                    brick.hit()
                    game.increaseScore(brick.getHitPoints())
                    #When bullet hits brick, bullet should reinitialize..reset to fire again
                    #bullet.setPosition(((pygame.mouse.get_pos()[0] - 10), ship.getPosition()[1]))
                    bullet.setMotion(0)
                    break

            if bullet.intersects(ship):
                bullet.changeDirection(ship)

            bullet.updatePosition()

            if bullet.isBulletDead():
                bullet.setMotion(0)
                game.reduceLives()

            #only draw bullet if in motion
            if bullet.isInMotion():
                game.screen.blit(bullet.getSprite(), bullet.getPosition())
        
        #render bricks
        for brick in game.getLevel().getBricks():
            if not brick.isDestroyed():
                game.screen.blit(brick.getSprite(), brick.getPosition())

        #render ship
        ship.setPosition((pygame.mouse.get_pos()[0], ship.getPosition()[1]))
        game.screen.blit(ship.getSprite(), ship.getPosition())


        #render hi score
        self.clearText()
        self.addText("Your Score: " + str(game.getScore()),
                     x = 0,
                     y = GameConstants.SCREEN_SIZE[1] - 60, 
                     size = 30)

        self.addText("Lives: " + str(game.getLives()),
                      x = 0,
                      y = GameConstants.SCREEN_SIZE[1] - 30, 
                      size = 30)

    def handleEvents(self, events):
        #pass event to base class
        super(PlayingGameScene, self).handleEvents(events)

        #specific scene event handling
        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for ball in self.getGame().getBullets():
                    ball.setMotion(1)