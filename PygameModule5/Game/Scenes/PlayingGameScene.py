import pygame
from Game.Scenes import Scene

class PlayingGameScene(Scene):

    def __init__(self, game):
        super(PlayingGameScene, self).__init__(game)

    def handleEvents(self, events):
        #pass event to base class
        super(PlayingGameScene, self).handleEvents(events)

        #specific scene event handling
        for event in events:
            if event.type == pygame.QUIT:
                exit()

    def render(self):
        super(PlayingGameScene, self).render()

        game = self.getGame()

        for ball in game.getBalls():
            
            for brick in game.getLevel().getBricks():
                if ball.intersects(brick):
                    brick.hit()
                    ball.changeDirection(brick)
                    break

            ball.updatePosition()
            game.screen.blit(ball.getSprite(), ball.getPosition())
            
        for brick in game.getLevel().getBricks():
            if not brick.isDestroyed():
                game.screen.blit(brick.getSprite(), brick.getPosition())

