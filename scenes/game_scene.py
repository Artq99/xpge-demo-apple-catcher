import pygame

from xpgext.scene import SimpleScene
from xpgext.sprite import XPGESprite

from behaviour_scripts.basket import BasketController, AppleSpawner


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
        basket.components.append(AppleSpawner(basket))

        self.sprites.append(basket)
