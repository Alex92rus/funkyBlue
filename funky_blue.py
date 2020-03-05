import arcade
from arcade import Sprite, Texture, SpriteList

from bounce_dot_sprite import BounceDotSprite

SCREEN_WIDTH = 600
DOT_SIDE_LENGTH = 20
SCREEN_HEIGHT = 600
SPRITE_SCALING_FUNKY = 0.9
MOVEMENT_SPEED = 5

class MyGame(arcade.Window):

    def __init__(self, width, height, name):
        super().__init__(width, height, name)

    def setup(self):
        self.the_funky_blue = arcade.SpriteList()

        for i in range(1, 11):
            funky_blue = arcade.Sprite("assets/funky_blue_colour_{}.jpg".format(i), SPRITE_SCALING_FUNKY)
            self.the_funky_blue.append(funky_blue)

        self.add_lifes()

        self.current_Funky = self.the_funky_blue[-1]
        placeSprite(self.current_Funky, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        self.dots = []
        spriteDot = BounceDotSprite(DOT_SIDE_LENGTH, DOT_SIDE_LENGTH, "#0000ff", self)
        placeSprite(spriteDot, SCREEN_WIDTH // 2, SCREEN_HEIGHT - DOT_SIDE_LENGTH)
        spriteDot.rand_velocity(5, [-1, 1], [-1, 0])
        self.dots.append(spriteDot)

        spriteDot = BounceDotSprite(DOT_SIDE_LENGTH, DOT_SIDE_LENGTH, "#ff0000", self)
        placeSprite(spriteDot, SCREEN_WIDTH // 2, DOT_SIDE_LENGTH)
        spriteDot.rand_velocity(5, [-1, 1], [0, 1])
        self.dots.append(spriteDot)


        self.physics_engine = arcade.PhysicsEngineSimple(self.current_Funky, arcade.SpriteList())

        self.score = 0
        self.level = 1
        self.next_score = 10

    def add_lifes(self):
        offset = 10
        self.life_icons = arcade.SpriteList()
        for i in range(0, 3):
            heart = arcade.Sprite("assets/heart_life.png", 0.05)
            placeSprite(heart, 40 + (offset + heart.width) * i, SCREEN_HEIGHT - heart.height * 2.5)
            self.life_icons.append(heart)
        self.lives = 3

    def on_draw(self):

        arcade.start_render()

        if self.lives <= 0:
            output = f"GAME OVER SCORE: {self.score}"
            arcade.draw_text(output, (self.width // 2) - 150, self.height // 2, arcade.color.GREEN, 30, bold=True)
        else:
            self.current_Funky.draw()
            for sprite in self.dots:
                sprite.draw()

            output = f"Score: {self.score}"
            arcade.draw_text(output, self.width - 100, self.height - 40, arcade.color.AIR_FORCE_BLUE, 20, bold=True)
            self.life_icons.draw()

    def update(self, delta_time: float):
        if self.lives > 0:
            self.physics_engine.update()
            if self.current_Funky.left < 1 or self.current_Funky.right >= self.width:
                self.current_Funky.change_x = 0


            for sprite in self.dots:
               sprite.update()
               if self.current_Funky.left - sprite.width <= sprite.left <= self.current_Funky.right:
                   if sprite.change_y < 0 and abs(sprite.bottom - self.current_Funky.top) <= 2:
                      sprite.change_x = - sprite.change_x
                      sprite.change_y = - sprite.change_y
                      self.score += 1
                   elif sprite.change_y > 0 and abs(sprite.top - self.current_Funky.bottom) <= 2:
                       sprite.change_x = - sprite.change_x
                       sprite.change_y = - sprite.change_y
                       self.score += 1
               if self.current_Funky.bottom <= sprite.center_y <= self.current_Funky.top:
                   if abs(sprite.right - self.current_Funky.left) <= 2:
                       sprite.change_x = - sprite.change_x
                   elif abs(sprite.left - self.current_Funky.right) <= 2:
                       sprite.change_x = - sprite.change_x

            self.dots = [self._swap_color(s) for s in self.dots]

            if self.score >= self.next_score and self.level < len(self.the_funky_blue):
                self.level += 1
                self.next_score += 1
                smallerFunky = self.the_funky_blue[- self.level]
                placeSprite(smallerFunky, self.current_Funky.center_x, self.current_Funky.center_y)
                self.current_Funky = smallerFunky
                self.physics_engine = arcade.PhysicsEngineSimple(self.current_Funky, arcade.SpriteList())

    def on_key_press(self, symbol: int, modifiers: int):

        if symbol == arcade.key.LEFT and self.current_Funky.left > 0:
            self.current_Funky.change_x = -MOVEMENT_SPEED if self.current_Funky.left > MOVEMENT_SPEED else - self.current_Funky.left
        elif symbol == arcade.key.RIGHT and self.current_Funky.right < self.width:
            self.current_Funky.change_x = MOVEMENT_SPEED if self.current_Funky.right + MOVEMENT_SPEED <= self.width else self.width - self.current_Funky.right


    def on_key_release(self, symbol: int, modifiers: int):

        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.current_Funky.change_x = 0

    def _swap_color(self, bounceDotSprite: BounceDotSprite):
        if bounceDotSprite.center_y > bounceDotSprite.window.height / 2 and bounceDotSprite.solidColor != "#0000ff":
            #self.lives -= 1
            #self.life_icons.pop()
            return bounceDotSprite.change_solid_color("#0000ff")
        elif bounceDotSprite.center_y < bounceDotSprite.window.height / 2 and bounceDotSprite.solidColor != "#ff0000":
            #self.lives -= 1
           # self.life_icons.pop()
            return bounceDotSprite.change_solid_color("#ff0000")
        return bounceDotSprite

def placeSprite(sprite: Sprite, center_x: float, center_y: float):
    sprite.center_x = center_x
    sprite.center_y = center_y

def placeSpriteList(spriteList: SpriteList, centersList):
    for i in range(len(spriteList)):
        placeSprite(spriteList[i], centersList[i][0], centersList[i][1])

def init():
    return MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Funky Blue")


def render():
    arcade.start_render()
    arcade.set_background_color(arcade.color.WARM_BLACK)
    arcade.draw_circle_filled(200, 300, 50, arcade.color.AERO_BLUE)
    arcade.finish_render()

def run():
    arcade.run()


def main():
    funky_blue = init()
    funky_blue.setup()
    arcade.run()


if __name__ == '__main__':
    main()