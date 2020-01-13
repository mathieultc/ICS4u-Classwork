"""
Move with a Sprite Animation

Simple program to show basic sprite usage.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_animation
"""
import arcade
import random
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Move with a Sprite Animation Example"

CHARACTER_SCALING = 0.5

MOVEMENT_SPEED = 5
UPDATES_PER_FRAME = 7

# Constants used to track if the player is facing left or right
RIGHT_FACING = 0
LEFT_FACING = 1


def load_texture_pair(filename):
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [
        arcade.load_texture(filename, scale=CHARACTER_SCALING),
        arcade.load_texture(filename, scale=CHARACTER_SCALING, mirrored=True)
    ]


class PlayerCharacter(arcade.Sprite):
    def __init__(self):

        # Set up parent class
        super().__init__()

        # Default to face-right
        self.character_face_direction = RIGHT_FACING

        # Used for flipping between image sequences
        self.cur_texture = 0

        # Track out state
     

        # Adjust the collision box. Default includes too much empty space
        # side-to-side. Box is centered at sprite center, (0, 0)

        # --- Load Textures ---

        # Images from Kenney.nl's Asset Pack 3
        main_path = ":resources:images/animated_characters/male_person/malePerson"
        # main_path = ":resources:images/animated_characters/female_person/femalePerson"
        # main_path = ":resources:images/animated_characters/male_person/malePerson"
        # main_path = ":resources:images/animated_characters/male_adventurer/maleAdventurer"
        # main_path = ":resources:images/animated_characters/zombie/zombie"
        # main_path = ":resources:images/animated_characters/robot/robot"

        # Load textures for idle standing
        self.idle_texture_pair = load_texture_pair(f"{main_path}_idle.png")

        # Load textures for walking
        self.walk_textures = []
        for i in range(8):
            texture = load_texture_pair(f"{main_path}_walk{i}.png")
            self.walk_textures.append(texture)

        self.jump_texture = load_texture_pair(f"{main_path}_jump.png")

    def update_animation(self, delta_time: float = 1/60):

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING
    
            
        # Idle animation
        if self.change_x == 0 and self.change_y == 0:
        # Walking animation
            self.cur_texture += 1
            if self.cur_texture > 7 * UPDATES_PER_FRAME:
                self.cur_texture = 0
            self.texture = self.walk_textures[self.cur_texture // UPDATES_PER_FRAME][self.character_face_direction]


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = None

        # Set up the player
        self.score = 0
        self.player = None

        self.sprite1 = arcade.Sprite(center_x=SCREEN_WIDTH//2, center_y=SCREEN_HEIGHT//2-100)
        self.sprite1.texture = arcade.make_soft_square_texture(50, arcade.color.BLACK, outer_alpha=255)
        self.sprite1.width = 200
        self.sprite1.height = 10

    def setup(self):
        self.player_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.player = PlayerCharacter()

        self.player.center_x = SCREEN_WIDTH//2
        self.player.center_y = SCREEN_HEIGHT // 2
        self.player.scale = 0.8

        self.player_list.append(self.player)

        # Set the background color
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        self.sprite1.draw()

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        if key == arcade.key.SPACE:
            self.player.change_y = 2
            self.player.texture = self.player.jump_texture[0]

            
    def on_key_release(self, key, modifiers):
        """
        Called when the user releases a key.
        """
  
        self.key_press = []
        if key == arcade.key.SPACE:
            self.player.change_y = -2

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.sprite1.update()
        self.player_list.update()
        self.player_list.update_animation()

        if self.player.collides_with_sprite(self.sprite1):
            self.player.change_x = 0
            self.player.change_y = 0

        # Generate a list of all sprites that collided with the player.

        # Loop through each colliding sprite, remove it, and add to the score.
     

def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()