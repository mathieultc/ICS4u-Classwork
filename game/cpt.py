import arcade

WIDTH = 800
HEIGHT = 600


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

        self.sprite1 = arcade.Sprite(center_x=100, center_y=200)
        self.sprite1.change_x = 10
        self.sprite1.texture = arcade.make_soft_square_texture(50,
                                                               arcade.color.BLACK,
                                                               outer_alpha=255)

        self.sprite2 = arcade.Sprite(center_x=WIDTH-100, center_y=200)
        self.sprite2.texture = arcade.make_soft_square_texture(50,
                                                               arcade.color.BLUE,
                                                               outer_alpha=255)
        
        self.sprite3 = arcade.Sprite(center_x=90, center_y=200)
        self.sprite3.texture = arcade.make_soft_square_texture(50, arcade.color.GREEN, outer_alpha=255)

        self.sprite4 = arcade.Sprite(center_x=WIDTH-100, center_y=300)
        self.sprite4.change_y = -10
        self.sprite4.texture = arcade.make_soft_square_texture(50, arcade.color.YELLOW, outer_alpha=255)

        self.sprite5 = arcade.Sprite(center_x=WIDTH-100, center_y=HEIGHT+50)
        self.sprite5.texture = arcade.make_soft_square_texture(50, arcade.color.WHITE, outer_alpha=255)

    def on_draw(self):
        arcade.start_render()  # keep as first line

        # Draw everything below here.
        self.sprite1.draw()
        self.sprite2.draw()
        self.sprite3.draw()
        self.sprite4.draw()
        self.sprite5.draw()

    def update(self, delta_time):
        self.sprite1.update()
        self.sprite2.update()
        self.sprite3.update()
        self.sprite4.update()
        self.sprite5.update()

        if self.sprite1.collides_with_sprite(self.sprite2):
            self.sprite1.change_x = -10

        elif self.sprite1.collides_with_sprite(self.sprite3):
            self.sprite1.change_x = 10

        elif self.sprite4.collides_with_sprite(self.sprite2):
            self.sprite4.change_y = 10

        elif self.sprite4.collides_with_sprite(self.sprite5):
            self.sprite4.change_y = -10


def main():
    game = MyGame(WIDTH, HEIGHT, "My Game")
    arcade.run()


if __name__ == "__main__":
    main()