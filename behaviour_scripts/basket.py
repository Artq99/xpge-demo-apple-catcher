import pygame

from xpgext.sprite import SpriteBehaviour


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
