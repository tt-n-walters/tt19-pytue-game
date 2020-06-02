from arcade import Sprite, load_texture


class Player(Sprite):
    def __init__(self, center_x, center_y):
        super().__init__(scale=2)
        self.texture = load_texture("assets/player/down.png", width=42, height=50)
        self.center_x = center_x
        self.center_y = center_y
