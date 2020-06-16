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

stationary_up = up[0]
stationary_down = down[0]
stationary_left = left[0]
stationary_right = right[0]

moving_up = up
moving_down = down
moving_left = left
moving_right = right


class Player(Character):
    def __init__(self, center_x, center_y):
        super().__init__(
            stationary_up, stationary_down, stationary_left, stationary_right,
            moving_up, moving_down, moving_left, moving_right,
            scale=2, center_x=center_x, center_y=center_y)
