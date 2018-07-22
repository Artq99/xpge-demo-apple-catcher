import pygame
import random

from xpgext.sprite import XPGESprite, SpriteBehaviour

from behaviour_scripts.apple import AppleController


class BasketController(SpriteBehaviour):

    def on_scene_loaded(self):
        pygame.mouse.set_pos(400, 300)
        pygame.event.get(pygame.MOUSEMOTION)

    def on_handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            x, y = self.sprite.position
            x += event.rel[0]
            x = max(min(700, x), 0)
            self.sprite.position = (x, y)

            pygame.mouse.set_pos(400, 300)
            pygame.event.get(pygame.MOUSEMOTION)


class AppleSpawner(SpriteBehaviour):

    def __init__(self, sprite):
        super().__init__(sprite)

        self.counter = 0

    def on_update(self):
        self.counter += 1

        if self.counter % 100 == 0:
            apple_image = pygame.Surface((25, 25))
            apple_image.fill((125, 125, 0))

            apple = XPGESprite(self.sprite.scene_manager)
            apple.image = apple_image
            apple.components.append(AppleController(apple))

            x = random.randint(0, 775)
            y = 0

            apple.position = (x, y)

            self.sprite.scene_manager._sprites.append(apple)
            self.sprite.scene_manager.static["apples_number"] += 1

        print("Number of apples: {}".format(self.sprite.scene_manager.static["apples_number"]))
