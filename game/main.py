import arcade

WIDTH = 800
HEIGHT = 600


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        self.player = arcade.Sprite(filename="game/images/sonic.jpg", center_x= 200, center_y = 200, scale=0.2)
        self.obs = arcade.draw_circle_filled(center_x = 500, center_y = 300, 20, arcade.color.BLUE)

    def on_draw(self):
        arcade.start_render()
        self.player.draw()

        for _  in range(10):
            self.obs.draw()

    def update(self, delta_time):
        self.player.update()
        self.player.change_y *= 0.98

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.player.change_y = 3
        if key == arcade.key.S:
            self.player.change_y = -3

    

def main():
    game = MyGame(WIDTH, HEIGHT, "my game")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

    