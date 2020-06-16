from arcade import load_textures
from character import Character


up = load_textures("assets/player/up.png", [[0, 0, 50, 50],
                                            [50, 0, 50, 50],
                                            [100, 0, 50, 50]])
down = load_textures("assets/player/down.png", [[0, 0, 50, 50],
                                                [50, 0, 50, 50],
                                                [100, 0, 50, 50]])
left = load_textures("assets/player/left.png", [[0, 0, 50, 50],
                                                [50, 0, 50, 50],
                                                [100, 0, 50, 50]])
right = load_textures("assets/player/right.png", [[0, 0, 50, 50],
                                                  [50, 0, 50, 50],
                                                  [100, 0, 50, 50]])


class Player(Character):
    def __init__(self, center_x, center_y):
        super().__init__(scale=2)
