from arcade import Sprite, load_texture


class Player(Sprite):
    def __init__(self, center_x, center_y):
        super().__init__()
        self.texture = load_texture("assets/player/down.png")
        self.center_x = center_x
        self.center_y = center_y
