import random

from PIL import Image
from arcade import SpriteSolidColor, Window, Texture


class BounceDotSprite(SpriteSolidColor):

    def __init__(self, width, height, color, window: Window):
        super().__init__(width, height, color)
        self.window = window
        self.solidColor = color

    def update(self):
        super().update()
        self.reflect()


    def reflect(self):
        if self.top >= self.window.height or self.bottom <= 0:
            self.change_y = - self.change_y
        if self.left <= 0 or self.right >= self.window.width:
            self.change_x = - self.change_x

    def change_solid_color(self, color):
        spriteDot = BounceDotSprite(self.width, self.height, color, self.window)
        spriteDot.center_x, spriteDot.center_y = self.center_x, self.center_y
        spriteDot.change_x, spriteDot.change_y = self.change_x, self.change_y
        return spriteDot

    def rand_velocity(self, multiplier, directionX, directionY):
        self.change_x = multiplier * random.uniform(directionX[0], directionX[1])
        self.change_y = multiplier * random.uniform(directionY[0], directionY[1])
