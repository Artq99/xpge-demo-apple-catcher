import pygame

from xpgext.scene import SimpleScene
from xpgext.sprite import XPGESprite

from behaviour_scripts.basket import BasketController
from behaviour_scripts.apple import AppleController


class GameScene(SimpleScene):

    def __init__(self, scene_manager):
        super().__init__(scene_manager)

        basket_image = pygame.Surface((100, 25))
        basket_image.fill((255, 0, 0))

        basket = XPGESprite(self.scene_manager)
        basket.image = basket_image
        basket.position = (350, 575)
        basket.name = "basket"
        basket.components.append(BasketController(basket))

        self.sprites.append(basket)

        apple_image = pygame.Surface((25, 25))
        apple_image.fill((125, 125, 0))

        apple = XPGESprite(self.scene_manager)
        apple.image = apple_image
        apple.position = (0, 350)
        apple.components.append(AppleController(apple))

        self.sprites.append(apple)
