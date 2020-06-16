import arcade
from gun import Gun
from player import Player


class Game(arcade.Window):
    def __init__(self):
        super().__init__(title="Game", width=15 * 64, height=9 * 64, fullscreen=False)
        
        # Load background image
        self.background_sprite = arcade.Sprite("assets/background.png", center_x=self.width / 2, center_y=self.height / 2)
        self.static_sprites = arcade.SpriteList(is_static=True)
        self.static_sprites.append(self.background_sprite)

        # Create game objects
        self.test_gun = Gun(300, 200)
        self.bullets = []
        self.player = Player(50, 50)

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

    def on_draw(self):
        arcade.start_render()
        # Draw backgroud and all non-moving sprites
        self.static_sprites.draw()

        # Draw game objects
        self.player.draw()
        self.test_gun.draw()
        for bullet in self.bullets:
            bullet.draw()

    def on_update(self, deltatime):
        # Update game objects
        for bullet in self.bullets:
            bullet.update()
        self.test_gun.update(deltatime)
        self.player.update()


Game()
arcade.run()
