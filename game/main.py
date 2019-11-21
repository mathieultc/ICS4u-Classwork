import arcade

width = 500
height = 500

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        self.drawing = arcade.Sprite(filename = "images/sonic.jpg", center_x = 250, center_y = 250, scale = 0.2)

    def on_draw(self):
        arcade.start_render()
        self.drawing.draw()

    def update(self, delta_time):
        self.drawing.update()
        self.drawing.change_x *= 0.98
        self.drawing.change_y *= 0.98

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.drawing.change_y = 1
        if key == arcade.key.S:
            self.drawing.change_y = -1
        if key == arcade.key.D:
            self.drawing.change_x = 1
        if key == arcade.key.A:
            self.drawing.change_x = -1

    def check_boundaries(self):
        if self.drawing.center_x > 500:
            self.drawing.center_x = 500


def main():
    game = MyGame(width, height, "game")
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()