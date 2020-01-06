import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Shape List Demo Person"


def make_character(head_radius,
                chest_height,
                chest_width,
                leg_width,
                leg_height,
                arm_width,
                arm_length,
                arm_gap,
                shoulder_height):

    shape_list = arcade.ShapeElementList()

    # Head
    shape = arcade.create_ellipse_filled(0, chest_height / 2 + head_radius, head_radius, head_radius,
                                         arcade.color.WHITE)
    shape_list.append(shape)

    # Chest
    shape = arcade.create_rectangle_filled(0, 0, chest_width, chest_height, arcade.color.BLACK)
    shape_list.append(shape)

    # Left leg
    shape = arcade.create_rectangle_filled(-(chest_width / 2) + leg_width / 2, -(chest_height / 2) - leg_height / 2,
                                           leg_width, leg_height, arcade.color.RED)
    shape_list.append(shape)

    # Right leg
    shape = arcade.create_rectangle_filled((chest_width / 2) - leg_width / 2, -(chest_height / 2) - leg_height / 2,
                                           leg_width, leg_height, arcade.color.RED)
    shape_list.append(shape)

    # Left arm
    shape = arcade.create_rectangle_filled(-(chest_width / 2) - arm_width / 2 - arm_gap,
                                           (chest_height / 2) - arm_length / 2 - shoulder_height, arm_width, arm_length,
                                           arcade.color.BLUE)
    shape_list.append(shape)

    # Left shoulder
    shape = arcade.create_rectangle_filled(-(chest_width / 2) - (arm_gap + arm_width) / 2,
                                           (chest_height / 2) - shoulder_height / 2, arm_gap + arm_width,
                                           shoulder_height, arcade.color.BLUE_BELL)
    shape_list.append(shape)

    # Right arm
    shape = arcade.create_rectangle_filled((chest_width / 2) + arm_width / 2 + arm_gap,
                                           (chest_height / 2) - arm_length / 2 - shoulder_height, arm_width, arm_length,
                                           arcade.color.BLUE)
    shape_list.append(shape)

    # Right shoulder
    shape = arcade.create_rectangle_filled((chest_width / 2) + (arm_gap + arm_width) / 2,
                                           (chest_height / 2) - shoulder_height / 2, arm_gap + arm_width,
                                           shoulder_height, arcade.color.BLUE_BELL)
    shape_list.append(shape)

    return shape_list


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        head_radius = 10
        chest_height = 50
        chest_width = 30
        leg_width = 20
        leg_height = 20
        arm_width = 5
        arm_length = 20
        arm_gap = 5
        shoulder_height = 5

        self.shape_list = make_character(head_radius,
                                      chest_height,
                                      chest_width,
                                      leg_width,
                                      leg_height,
                                      arm_width,
                                      arm_length,
                                      arm_gap,
                                      shoulder_height)

        arcade.set_background_color(arcade.color.AMAZON)

        self.shape_list.center_x , self.shape_list.center_y = SCREEN_WIDTH//2, SCREEN_HEIGHT//2


    def setup(self):

        """ Set up the game and initialize the variables. """

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        self.shape_list.draw()

    def on_update(self, delta_time):
        pass
   

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.D:
            self.shape_list.change_x += 5

        elif key == arcade.key.W:
            self.shape_list.change_y += 5
      


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()