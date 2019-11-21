import arcade

WIDTH = 800
HEIGHT = 600


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
       self.player = arcade.Sprite(filename = "arcade_sprite/images/playerShip1_blue.png", scale = 0.5, center_x = 200, center_y = 200)
        
    def draw(self):
       arcade.start_render()
       self.player.draw()

    def update(self, delta_time):
        self.player.update()
        self.player.change_x *= 0.98

    def on_key_press(self, key, modifiers):
        if key == arcade.key.D:
            self.player.change_x = 1

def main():
    game = MyGame(WIDTH, HEIGHT, "my game")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
       