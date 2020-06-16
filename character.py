import math

from arcade import Sprite


class Character(Sprite):
    def __init__(
        self,
        stationary_up, stationary_down, stationary_left, stationary_right,
        moving_up, moving_down, moving_left, moving_right,
        scale=1, texture_change_distance=15, center_x=0, center_y=0
    ):
        super().__init__(scale=scale)
        self.center_x = center_x
        self.center_y = center_y

        self.direction = "down"

        self.texture_change_distance = texture_change_distance * scale
        self.last_texture_x = 0
        self.last_texture_y = 0
        self.texture_index = 0

        self.stationary = {
            "up": stationary_up,
            "down": stationary_down,
            "left": stationary_left,
            "right": stationary_right,
        }
        self.moving = {
            "up": moving_up,
            "down": moving_down,
            "left": moving_left,
            "right": moving_right,
        }
        self.update_animation(0)

    def update_animation(self, delta_time):
        # Not moving
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.stationary[self.direction]
            return
            
        # Moving
        if self.change_y > 0:
            direction = "up"
        if self.change_y < 0:
            direction = "down"
        if self.change_x < 0:
            direction = "left"
        if self.change_x > 0:
            direction = "right"

        if self.direction != direction:
            self.texture_index = 0
            self.last_texture_x = self.center_x
            self.last_texture_y = self.center_y
            self.direction = direction

        distance = math.sqrt((self.center_x - self.last_texture_x)
                            ** 2 + (self.center_y - self.last_texture_y) ** 2)
        if distance > self.texture_change_distance:
            self.last_texture_x = self.center_x
            self.last_texture_y = self.center_y
            self.texture_index += 1
            if self.texture_index == len(self.moving[self.direction]):
                self.texture_index = 0
        self.texture = self.moving[self.direction][self.texture_index]

    def move_up(self, speed):
        self.velocity = [0, speed]

    def move_down(self, speed):
        self.velocity = [0, -speed]

    def move_left(self, speed):
        self.velocity = [-speed, 0]

    def move_right(self, speed):
        self.velocity = [speed, 0]

    def stop(self):
        self.velocity = [0, 0]
