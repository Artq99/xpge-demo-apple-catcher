from xpgext.application import XPGApplication
from xpgext.scene_manager import SimpleSceneManager


class SceneManager(SimpleSceneManager):

    def __init__(self):
        super().__init__()

        self.static = {"points": 0}


class AppleCatcher(XPGApplication):

    def __init__(self):
        super().__init__(SceneManager(), (800, 600))


if __name__ == "__main__":
    game = AppleCatcher()
    game.run_main_loop()
