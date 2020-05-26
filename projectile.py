from arcade import Sprite, draw_rectangle_filled, color
from math import sin, cos, radians


class Projectile(Sprite):
    def __init__(self, image_filename, direction, speed):
        super().__init__(filename=image_filename, scale=4)
        self.angle = direction
        self.change_x = speed * cos(radians(direction))
        self.change_y = speed * sin(radians(direction))



class SmallBullet(Projectile):
    def __init__(self, gun_x, gun_y, direction, speed):
        super().__init__("assets/bullets/bulletDark2.png", direction, speed)
        self.center_x = gun_x
        self.center_y = gun_y
        self.width = self.width / 2
        self.height = self.height / 2
        self.angle = -90
