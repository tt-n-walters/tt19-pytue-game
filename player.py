from arcade import load_textures
from character import Character

up_textures = load_textures(
    "assets/player/up.png", [[0, 0, 50, 50], [50, 0, 50, 50], [100, 0, 50, 50]])
down_textures = load_textures(
    "assets/player/down.png", [[0, 0, 50, 50], [50, 0, 50, 50], [100, 0, 50, 50]])
left_textures = load_textures(
    "assets/player/left.png", [[0, 0, 50, 50], [50, 0, 50, 50], [100, 0, 50, 50]])
right_textures = load_textures(
    "assets/player/right.png", [[0, 0, 50, 50], [50, 0, 50, 50], [100, 0, 50, 50]])

stationary_textures_up = up_textures[0]
stationary_textures_down = down_textures[0]
stationary_textures_left = left_textures[0]
stationary_textures_right = right_textures[0]

moving_textures_up = [
    up_textures[0], up_textures[1], up_textures[0], up_textures[2]]
moving_textures_down = [
    down_textures[0], down_textures[1], down_textures[0], down_textures[2]]
moving_textures_left = [
    left_textures[0], left_textures[1], left_textures[0], left_textures[2]]
moving_textures_right = [
    right_textures[0], right_textures[1], right_textures[0], right_textures[2]]

class Player(Character):
    def __init__(self, center_x, center_y, scale=1):
        super().__init__(stationary_textures_up, stationary_textures_down, stationary_textures_left, stationary_textures_right, moving_textures_up, moving_textures_down, moving_textures_left, moving_textures_right, center_x=center_x, center_y=center_y, scale=scale)
