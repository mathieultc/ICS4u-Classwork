import arcade

WIDTH = 800
HEIGHT = 600


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

        # If you have sprite lists, you should create them here,
        # and set them to None

        self.key_press = None

    def setup(self):
        self.player = arcade.Sprite(filename="images/playerShip1_blue.png",
                                    center_x=200,
                                    center_y=200,
                                    scale=0.5)

    def on_draw(self):
        arcade.start_render()  # keep as first line

        # Draw everything below here.
        self.player.draw()

    def update(self, delta_time):
        self.player.update()
        self.player.change_x *= 0.98
        self.player.change_y *= 0.98
 
    def on_key_press(self, key, key_modifiers):
        print(key, key_modifiers)
        
        if key == arcade.key.D:
            self.player.change_x = 1
            self.key_press = True
        if key == arcade.key.A:
            self.player.change_x = -1
        if key == arcade.key.W:
            self.player.change_y = 1
        if key == arcade.key.S:
            self.player.change_y = -1

    def on_key_release(self, key, key_modifiers):
        pass
    
  

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    game = MyGame(WIDTH, HEIGHT, "My Game")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()