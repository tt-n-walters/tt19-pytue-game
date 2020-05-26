import monkeypatch
import arcade
from gun import Gun


class Game(arcade.Window):
    def __init__(self):
        super().__init__(title="Game", width=1200, height=400, fullscreen=False)
        arcade.set_background_color(arcade.color.WHITE)
        self.test_gun = Gun(300, 200)
        self.bullets = []

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()
        if symbol == arcade.key.SPACE:
            self.bullets.append(self.test_gun.fire())

    def on_draw(self):
        arcade.start_render()
        self.test_gun.draw()
        for bullet in self.bullets:
            bullet.draw()

    def on_update(self, deltatime):
        for bullet in self.bullets:
            bullet.update()
        self.test_gun.update(deltatime)


Game()
arcade.run()
