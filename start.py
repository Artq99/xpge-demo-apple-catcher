import pygame

from xpgext.application import XPGApplication
from xpgext.scene_manager import SimpleSceneManager

from scenes.game_scene import GameScene


class SceneManager(SimpleSceneManager):

    def __init__(self):
        super().__init__()

        self.static = {"points": 0}


class AppleCatcher(XPGApplication):

    def __init__(self):
        super().__init__(SceneManager(), (800, 600))

        pygame.mouse.set_visible(False)

        self.scene_manager.register_scene(GameScene, "game scene")
        self.scene_manager.load_scene("game scene")


if __name__ == "__main__":
    game = AppleCatcher()
    game.run_main_loop()
