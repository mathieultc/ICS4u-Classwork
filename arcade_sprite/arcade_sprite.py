import arcade

WIDTH = 800
HEIGHT = 600


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        self.player = arcade.Sprite(filename="arcade_sprite/images/playerShip1_blue.png",center_x=200,center_y=200,scale=0.5)

    def on_draw(self):
        arcade.start_render()  # keep as first line
        self.player.draw()

    def update(self, delta_time):
        self.player.update()
        self.player.change_x *= 0.98
 
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.D:
            self.player.change_x = 1
  
def main():
    game = MyGame(WIDTH, HEIGHT, "My Game")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()