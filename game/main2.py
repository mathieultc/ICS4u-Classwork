import arcade

WIDTH = 800
HEIGHT = 600


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        self.player = arcade.Sprite(filename="game/images/sonic.jpg",center_x= 200, center_y = 200, scale=0.5)

    def on_draw(self):
        arcade.start_render() 
        self.player.draw()

def main():
    game = MyGame(WIDTH, HEIGHT, "My Game")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()