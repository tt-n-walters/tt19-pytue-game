from arcade import Sprite
from projectile import SmallBullet


class Gun(Sprite):
    def __init__(self, x, y):
        super().__init__("assets/weapons/UK.png",
                         image_x=99,
                         image_y=2,
                         image_width=33,
                         image_height=13,
                         scale=8)
        self.center_x = x
        self.center_y = y

    def fire(self):
        self.angle = 30
        bullet = SmallBullet(self.right, self.center_y, 0, 50)
        return bullet

    def reload(self):
        pass

    def zoom(self):
        pass
    
    def update(self, delta):
        if self.angle > 0:
            self.angle = self.angle - 1
