import monkeypatch
import arcade
from gun import Gun
from player import Player


class Game(arcade.Window):
    def __init__(self):
        super().__init__(title="Game", width=1200, height=800, fullscreen=False)
        arcade.set_background_color(arcade.color.WHITE)
        self.test_gun = Gun(300, 200)
        self.bullets = []
        self.player = Player(50, 50, scale=2)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()
        if symbol == arcade.key.SPACE:
            self.bullets.append(self.test_gun.fire())
        
        if symbol == arcade.key.W:
            self.player.move_up(4)
        if symbol == arcade.key.A:
            self.player.move_left(4)
        if symbol == arcade.key.S:
            self.player.move_down(4)
        if symbol == arcade.key.D:
            self.player.move_right(4)
    
    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.W and self.player.direction == "up":
            self.player.stop()
        if symbol == arcade.key.A and self.player.direction == "left":
            self.player.stop()
        if symbol == arcade.key.S and self.player.direction == "down":
            self.player.stop()
        if symbol == arcade.key.D and self.player.direction == "right":
            self.player.stop()


    def on_draw(self):
        arcade.start_render()
        self.test_gun.draw()
        for bullet in self.bullets:
            bullet.draw()
        self.player.draw()

    def on_update(self, deltatime):
        for bullet in self.bullets:
            bullet.update()
        self.test_gun.update(deltatime)

        self.player.update()
        self.player.update_animation(deltatime)


# Open the correct folder, so Python knows where to loads images from
import os
correct_location = os.path.dirname(__file__)
os.chdir(correct_location)

Game()
arcade.run()
