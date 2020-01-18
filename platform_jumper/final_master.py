import arcade
import random
import os
import json
from typing import List, Dict

# dimensions of the screen
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# variables for the character animation
CHARACTER_SCALING = 0.4
MOVEMENT_SPEED = 5
FRAME_RATE = 7

# Constants used to track if the player is facing left or right
RIGHT_FACING = 0
LEFT_FACING = 1
Gravity = 2


class State():
    '''
    First class State() to create different game status of the player
    '''
    MAIN_MENU = 0
    PLAYING = 1
    GAME_OVER = 2

# List of different background images that are chosen randomly by the random
# function

background = ["Objects" + os.sep + "sprites" + os.sep + "officebackground.jpg",
              "Objects" + os.sep + "sprites" + os.sep + "cloudsky.jpg"]

platform = "Objects" + os.sep + "sprites" + os.sep + "platform2.png"
player = "Objects" + os.sep + "sprites" + os.sep + "officeguy.png"
enemy = "Objects" + os.sep + "sprites" + os.sep + "obstacle.png"
# Start screen and game over images
play = "Objects" + os.sep + "sprites" + os.sep + "play.png"
ready = "Objects" + os.sep + "sprites" + os.sep + "presspace.png"
ready_message = "Objects" + os.sep + "sprites" + os.sep + "Readymessage.png"
volume = "Objects" + os.sep + "sprites" + os.sep + "soundup.png"
highscore = "Objects" + os.sep + "sprites" + os.sep + "highscore.png"
gameover = "Objects" + os.sep + "sprites" + os.sep + "gameover2.png"

# Images for the different numbers used in scoring
SCORE = {
    '0': 'Objects' + os.sep + 'sprites' + os.sep + '0.png',
    '1': 'Objects' + os.sep + 'sprites' + os.sep + '1.png',
    '2': 'Objects' + os.sep + 'sprites' + os.sep + '2.png',
    '3': 'Objects' + os.sep + 'sprites' + os.sep + '3.png',
    '4': 'Objects' + os.sep + 'sprites' + os.sep + '4.png',
    '5': 'Objects' + os.sep + 'sprites' + os.sep + '5.png',
    '6': 'Objects' + os.sep + 'sprites' + os.sep + '6.png',
    '7': 'Objects' + os.sep + 'sprites' + os.sep + '7.png',
    '8': 'Objects' + os.sep + 'sprites' + os.sep + '8.png',
    '9': 'Objects' + os.sep + 'sprites' + os.sep + '9.png', }


def bubblesort(numbers: List[int]) -> List[int]:
    n = len(numbers)

    for i in range(n):
        for j in range(n - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    return numbers


def load_texture_pair(filename: str) -> "SpriteList":
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [
        arcade.load_texture(filename, scale=CHARACTER_SCALING),
        arcade.load_texture(filename, scale=CHARACTER_SCALING, mirrored=True)]


class PlayerCharacter(arcade.Sprite):
    """ Class PlayerCharacter

        Attrs:
            character_face_directio (int): face direction of the character 
            defaulted to right facing
            vel (int): The player's velocity
            dead (bool): Boolean statement used to track the player's state
            gravity_on (bool): Boolean statement to activate gravity
            walk_textures (List[sprites]): List of different walking textures 
            for animations
            jump_texture (sprite): Player character jumping texture
    """

    def __init__(self) -> None:
        """Creates a player character object"""

        # Set up parent class
        super().__init__()

        # Default to face-right
        self.character_face_direction = RIGHT_FACING

        # Used for flipping between image sequences
        self.cur_texture = 0
        self.vel = 0
        self.dead = False
        self.gravity_on = False

        # Track out state
        main_path = ":resources:images/animated_characters/male_person/malePerson"
        # Load textures for idle standing
        self.idle_texture_pair = load_texture_pair(f"{main_path}_idle.png")

        # Load textures for walking
        self.walk_textures = []
        for i in range(8):
            texture = load_texture_pair(f"{main_path}_walk{i}.png")
            self.walk_textures.append(texture)

        self.jump_texture = load_texture_pair(f"{main_path}_jump.png")

    def update_animation(self, delta_time: float = 1/60) -> None:
        """Updates the animation of the player
        Args: 
            delta_time (float): speed of the animation
        """

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        if self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING
            
        # walking animation
        if self.change_x == 0 and self.change_y == 0:
            self.cur_texture += 1
            if self.cur_texture > 7 * FRAME_RATE:
                self.cur_texture = 0
            self.texture = self.walk_textures[self.cur_texture // FRAME_RATE][self.character_face_direction]

        if self.dead:
            self.angle = 90
            if self.center_y > self.death_height + self.height//2:
                self.center_y -= 4
            return

        if self.vel > 0:
            self.center_y += 2
            self.vel -= 2
            self.texture = self.jump_texture[0]

        if self.vel == 0 and self.gravity_on is True:
            self.center_y -= 2

    # How many pixels per jump
    def jump(self) -> None:
        """class method to make the player jump"""
        self.vel = 60

    def die(self) -> None:
        """class method to make the player die"""
        self.dead = True


class Platform(arcade.Sprite):
    """class platform
    Attrs:
        horizontal_speed(int): speed of the platform
        scored(bool): To track whether if the player gained a point
        """    

    def __init__(self, image: "sprite") -> None:
        """creates a platform object

        Args:
            image(sprite): The texture for the platform sprite
        """
        super().__init__(image)
        self.horizontal_speed = -4
        self.scored = False

    @classmethod
    def random_platform_generator(cls) -> "sprites":
        """class method to generate random platform

        Args:
            sprites(sprite): The texture for the platform sprite

        Returns:
            returns a sprite image
        """

        new_platform = cls(platform)
        new_platform.center_y = random.randrange(150, SCREEN_HEIGHT//2, 10)
        new_platform.left = 250
        new_platform.width = random.randrange(180, 250)
        new_platform.height = 25
        return new_platform

    def update(self) -> None:
        """ Update method to update the x position of the platform"""
        self.center_x += self.horizontal_speed


# Main Game class
class Game(arcade.Window):
    """ Main class for the game

    Attrs:
        background: texture for the background image. Defaults to None.
        player_list (List[sprites]): list to store sprites for the player 
        character. Defaults to None.
        platform_sprites (List[sprites]): list to store the platform sprites. 
        Defaults to None.
        enemy_sprites (List[sprites]): list to store sprites for the enemy 
        image. Defauls to None.
        player: variable to store the call to the Player class. 
        Defaults to None.
        score_board (List[sprites]): list to store the sprites to display 
        scores. 
        Defaults to None.
        jump (bool): a boolean to check if the user pressed space bar.
        score (int): a variable to store the score. Defaults to None.
        state: variable used to track the state of the player. Defaults to main 
        menu.
        menus (Dict): dictionary to store different texture for the menu 
        screen.
        double_jump (bool): a boolean statement to check whether the player
        used double jump. Defaults to False.
        sorted_list (List[int]): list to store a sorted list of scores from 
        highest to lowest. Defaults to empty list
        stored_score (bool): boolean statement to check if we stored the score. 
        Defaults to False.
        sorted_score (bool): boolean statement to check if we sorted the list 
        already. Defaults to False.
    """

    def __init__(self, width: int, height: int) -> None:
        """
        Initializer for the game window, note that we need to call setup() on 
        the game object.

        Args: 
            width(int): the width of the screen
            height(int): the height of the screen
            title(str): the title of the screen
        """
        super().__init__(width, height, title="office guy")
        self.background = None
        self.player_list = None
        self.platform_sprites = None
        self.enemy_sprites = arcade.SpriteList()
        self.player = None
        # Score texture
        self.score_board = None
        self.score_list = None
        # A boolean to check if the user pressed space bar
        self.jump = False
        # initial score
        self.score = None
        # Initial state of the game
        self.state = State.MAIN_MENU
        # The texture for the start and game over screens.
        self.menus = {'start': arcade.load_texture(ready),
                      'ready': arcade.load_texture(ready_message),
                      'gameover': arcade.load_texture(gameover),
                      'play': arcade.load_texture(play),
                      'highscore': arcade.load_texture(highscore)}
        self.double_jump = False
        self.sorted_list = []
        self.stored_score = False
        self.sorted_score = False
        self.user_name = None
        self.change_user_name = None

        # for loop to generate 100 enemy sprites
        for _ in range(100):
            self.sprite1 = arcade.Sprite()
            self.sprite1.texture = arcade.load_texture(file_name=enemy, scale=0.2)
            self.sprite1.left = 400
            self.sprite1.center_y = random.randrange(200, SCREEN_HEIGHT//2+20)
            self.enemy_sprites.append(self.sprite1)

    def setup(self) -> None:
        """Sets up sprites for the game"""

        self.score = 0
        self.score_board = arcade.SpriteList()
        self.score_list = arcade.SpriteList()
        self.background = arcade.load_texture(random.choice(background))
        self.platform_sprites = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.five_best = []

        start_platform1 = Platform.random_platform_generator()
        self.platform_sprites.append(start_platform1)
        self.player = PlayerCharacter()
        self.player.center_x = 55
        self.player.center_y = SCREEN_HEIGHT//2 + 250
        self.player.scale = 0.8
        self.player_list.append(self.player)

    def draw_enemy_sprites(self, index: int) -> "sprite":
        """recursive function to draw sprites from the enemy sprites list"""

        n = len(self.enemy_sprites)

        if index > n:  # base case
            return True

        elif index < n:
            self.enemy_sprites[index].change_x = -4
            self.enemy_sprites[index].draw()

            if self.enemy_sprites[index].center_x <= 10:
                return self.draw_enemy_sprites(index+1)  # recursive step

    def draw_background(self) -> None:
        """draws the background"""

        # Function that loads the texture for the background
        arcade.draw_texture_rectangle(self.width // 2, self.height // 2, 500,
                                      500, self.background, 0)

    def draw_score_board(self) -> None:
        # function that loads the texture to draw the score
        self.score_board.draw()
        self.score_list.draw()

    def on_draw(self) -> None:
        """draw function to draw all necessary sprites on the screen"""
        # Start rendering and draw all the objects
        arcade.start_render()
        # draw background, then pipes on top, then base, then bird.
        self.draw_background()
        self.platform_sprites.draw()
        self.player_list.draw()
        # calling recursive function 
        self.draw_enemy_sprites(0)

        # What to draw if the game state in on menu
        if self.state == State.MAIN_MENU:
            # Show the main menu
            texture = self.menus['start']
            arcade.draw_texture_rectangle(self.width//2, self.height//2 + 50, 
                                          250, 50, texture, 0)
            texture = self.menus['ready']
            arcade.draw_texture_rectangle(self.width//2, self.height//2 + 100,
                                          250, 200, texture, 0)
        elif self.state == State.GAME_OVER:
            # Draw the game over menu if the player lost and the restart play 
            # button
            texture = self.menus['gameover']
            arcade.draw_texture_rectangle(self.width//2, self.height//2 + 50, 
                                          200, 100, texture, 0)
            texture = self.menus['play']
            arcade.draw_texture_rectangle(self.width//2, self.height//2 - 50, 
                                          texture.width, texture.height, 
                                          texture, 0)

            # If statement to compute if there is a new highscore
            self.draw_score_board()

    def on_key_press(self, key, key_modifiers) -> None:
        if key == arcade.key.SPACE and self.state == State.MAIN_MENU:
            # If game state is back to playing , just change the state and 
            # return
            self.state = State.PLAYING
        if key == arcade.key.SPACE and self.double_jump:
            # If Space bar is pressed, self.jump is set to true and will allow 
            # the player to jump
            self.jump = True

    def on_mouse_press(self, x, y, button, modifiers) -> None:
        # if statement to check whether the user clicks in the required box to 
        # restart game
        if self.state == State.GAME_OVER:
            texture = self.menus['play']
            x_position = self.width//2
            y_position = self.height//2 - 50
            if x_position - texture.width//2 <= x <= x_position + texture.width//2:
                if y_position - texture.height//2 <= y <= y_position + texture.height//2:
                    self.setup()
                    self.state = State.MAIN_MENU
                    self.stored_score = False
                    self.sorted_list = []

    def scoreboard(self) -> None:
        '''
        Function created to calculate the score by using a for loop
        '''
        center = 230

        self.score_board = arcade.SpriteList()

        for num in str(self.score):
            self.score_board.append(arcade.Sprite(SCORE[num], 1, 
                                                  center_x=center,
                                                  center_y=440))
            center += 24

    def store_score(self, score: int) -> None:
        """stores the score when game is over

        Args:
            score(int): the player's score
        """
        with open("score.json", "r") as f:
            data = json.load(f)
        data[f"user {len(data) + 1}"] = score
        with open("score.json", "w") as f:
            json.dump(data, f)
        self.stored_score = True

    def display_score(self) -> None:
        """displays all the score from highest to lowest"""

        self.score_list = arcade.SpriteList()
        x_position = 100
        y_position = 450
        self.five_best = []

        with open("score.json", "r") as f:
            data = json.load(f)

        for values in data.values():
            self.sorted_list.append(values)
            bubblesort(self.sorted_list)

        if len(self.sorted_list) < 6:
            self.five_best = self.sorted_list
        else:
            self.five_best = self.sorted_list[:5]

        for score in self.five_best:
            if len(str(score)) == 1:
                for num in str(score):
                    self.score_list.append(arcade.Sprite(SCORE[num], 1,
                                           center_x=x_position,
                                           center_y=y_position))
                    y_position -= 50

            if len(str(score)) == 2:
                for num in str(score):
                    self.score_list.append(arcade.Sprite(SCORE[num], 1, 
                                           center_x=x_position, 
                                           center_y=y_position))
                    x_position += 24
                y_position -= 50
                x_position = 100

    def generate_platform(self) -> None:
        """generate random platform"""

        new_platform = None

        for plat in self.platform_sprites:
            if plat.right <= 0:
                plat.kill()
            elif len(self.platform_sprites) == 1 and plat.right <= random.randrange(self.width // 2, self.width // 2 + 15):
                new_platform = Platform.random_platform_generator()

        if new_platform:
            self.platform_sprites.append(new_platform)

    def on_update(self, delta_time: float) -> None:
        """
        This a function to update all the images on screen before being drawn
        """
        self.player_list.update_animation()

        if self.state == State.PLAYING:
            self.generate_platform()
            self.player.gravity_on = True

            if self.jump:
                self.player.jump()
                self.jump = False
                self.player.center_y -= 2
               
            if self.player.center_y <= 0:
                self.state = State.GAME_OVER
                
            if self.player.top > self.height:
                self.player.top = self.height

            if self.player.center_x >= self.platform_sprites[0].center_x and not self.platform_sprites[0].scored:
                self.score += 1
                self.platform_sprites[0].scored = True

            hit = arcade.check_for_collision_with_list(self.player, 
                                                       self.enemy_sprites)
            if any(hit):
                self.state = State.GAME_OVER

            # checking when double jump is used up
            if self.player.center_y - self.player.height//2 <= self.platform_sprites[0].center_y + self.platform_sprites[0].height//2 and self.player.center_y >= self.platform_sprites[0].center_y - self.platform_sprites[0].height//2 and self.player.center_x <= self.platform_sprites[0].center_x + self.platform_sprites[0].width//2 and self.player.center_x >= self.platform_sprites[0].center_x - self.platform_sprites[0].width//2:
                self.double_jump = True
            if self.player.center_y > self.platform_sprites[0].center_y + 120:
                self.double_jump = False
            if self.player.center_y < self.platform_sprites[0].center_y - 100:
                self.double_jump = False
            # check if the player collides with platform
            if self.player.center_y - self.player.height//2 <= self.platform_sprites[0].center_y + self.platform_sprites[0].height//2 and self.player.center_y >= self.platform_sprites[0].center_y - self.platform_sprites[0].height//2 and self.player.center_x <= self.platform_sprites[0].center_x + self.platform_sprites[0].width//2 and self.player.center_x >= self.platform_sprites[0].center_x - self.platform_sprites[0].width//2:
                self.player.center_y = self.platform_sprites[0].center_y + self.platform_sprites[0].height//2 + self.player.height//2
                self.player.angle = 0
            # check if the player hits the platform from under
            if self.player.center_y + self.player.height//2 >= self.platform_sprites[0].center_y - self.platform_sprites[0].height//2 and self.player.center_y <= self.platform_sprites[0].center_y and self.player.center_x > self.platform_sprites[0].center_x - self.platform_sprites[0].width//2 and self.player.center_x < self.platform_sprites[0].center_x + self.platform_sprites[0].width//2:
                self.state = State.GAME_OVER
            # This calls update() method on each object in the SpriteList
            self.player_list.update()
            self.player_list.update_animation()
            self.platform_sprites.update()
            self.enemy_sprites.update()

        if self.state == State.GAME_OVER:
            self.player.update()
            self.player.gravity_on = False
            self.scoreboard()
            
            if self.stored_score is False:
                self.store_score(self.score)
                self.display_score()
                
                
def main():
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()