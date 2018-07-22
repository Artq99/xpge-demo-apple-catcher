import pygame

from xpgext.sprite import SpriteBehaviour


class AppleController(SpriteBehaviour):

    def __init__(self, sprite):
        super().__init__(sprite)

        # TODO this should be added to XPGE
        self.screen_rect = pygame.Rect(0, 0, 800, 600)
        self.basket = None

    def on_update(self):
        self.basket = self.sprite.scene_manager.get_by_name("basket")
        x, y = self.sprite.position
        self.sprite.position = (x, y + 5)

        if not self.screen_rect.colliderect(self.sprite.rect):
            # TODO this should be added to XPGE
            self.sprite.scene_manager._sprites.remove(self.sprite)
            self.sprite.scene_manager.static["apples_number"] -= 1

        if self.sprite.rect.colliderect(self.basket.rect):
            self.sprite.scene_manager.static["points"] += 1
            self.sprite.scene_manager._sprites.remove(self.sprite)
            self.sprite.scene_manager.static["apples_number"] -= 1
            print("Current points: {}".format(self.sprite.scene_manager.static["points"]))
