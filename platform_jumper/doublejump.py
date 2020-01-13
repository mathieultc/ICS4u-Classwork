

#Import all the important libraries that will be used throughout the program
import arcade
import random
import os

class State():
    '''
    First class State() to create different game status of the player
    '''
    MAIN_MENU = 0
    PLAYING = 1
    GAME_OVER = 2




# Image of the base floor
ground = "Objects" + os.sep + "sprites" + os.sep + "base.png"
# List of different background images that are chosen randomly by the random function
background = ["Objects" + os.sep + "sprites" + os.sep + "officebackground2.jpg"
               ,"Objects" + os.sep + "sprites" + os.sep + "cloudsky.jpg"]
platform = "Objects" + os.sep + "sprites" + os.sep + "platform2.png"

player = "Objects" + os.sep + "sprites" + os.sep + "officeguy.png"

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
    '9': 'Objects' + os.sep + 'sprites' + os.sep + '9.png',}



# Strength of gravity
Gravity = 2

class Player (arcade.AnimatedTimeSprite):


    def __init__(self, center_x, center_y, death_height):
        super().__init__(center_x=center_x, center_y=center_y)
        self.score = 0
        self.textures = [arcade.load_texture(player, 0, 0, 0, 0, False, False, 0.05)]
        self.vel = 0
        self.death_height = death_height
        self.dead = False


    def update(self,dt=0):
      

        if self.vel > 0:
            self.center_y += 2
            # self.vel initially set to 0
            self.vel -= 2

    
        else:
            self.center_y -= Gravity

    # How many pixels per jump
    def jump(self):
        self.vel = 60

    def die(self):
        self.dead = True


class Platform(arcade.Sprite):

    def __init__(self, image):
       
        super().__init__(image)
        # speed
        self.horizontal_speed = -3
        self.scored = False

    @classmethod
    def random_platform_generator(cls, sprites, height):

        new_platform = cls(platform)
        new_platform.center_y = random.randrange(150, 300, 10)
        new_platform.left = 250
        new_platform.width = random.randrange(100, 300)
        new_platform.height = 25


        return new_platform

    def update(self):
        self.center_x += self.horizontal_speed

class Game(arcade.Window):

    def __init__(self, width, height):

        """
        Initializer for the game window, note that we need to call setup() on the game object.
        """
        super().__init__(width, height, title= "office guy")
        self.background = None
        self.player_list = None
        self.sprites = None
        self.platform_sprites = None
        self.player = None
        # Background texture

        # Score texture
        self.score_board = None
        #highscore
        self.highscore = None
        self.new_highscore = None
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

    def setup(self):
        self.highscore = None
        self.score = 0
        self.score_board = arcade.SpriteList()
        self.background = arcade.load_texture(random.choice(background))
        self.platform_sprites = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
    
        self.sprites = dict()
        self.sprites['background'] = self.background

        start_platform1 = Platform.random_platform_generator(self.sprites, self.height)
        self.platform_sprites.append(start_platform1)
        self.player = Player(55, 550, 200)

        self.player_list.append(self.player)


    def draw_background(self):

        #Function that loads the texture for the background

        arcade.draw_texture_rectangle(self.width // 2, self.height // 2, 500, 500,
                                      self.background, 0)

    def draw_score_board(self):

        #function that loads the texture to draw the score

        self.score_board.draw()

    def on_draw(self):
      

        # Start rendering and draw all the objects
        arcade.start_render()

        # draw background, then pipes on top, then base, then bird.
        self.draw_background()
        self.platform_sprites.draw()
        self.player_list.draw()


        #What to draw if the game state in on menu
        if self.state == State.MAIN_MENU:
            # Show the main menu
            texture = self.menus['start']
            arcade.draw_texture_rectangle(self.width//2, self.height//2 + 50, 250, 50, texture, 0)
            texture = self.menus['ready']
            arcade.draw_texture_rectangle(self.width//2,self.height//2 +100,250,200,texture,0)
     


        elif self.state == State.GAME_OVER:
            # Draw the game over menu if the player lost and the restart play button
            texture = self.menus['gameover']
            arcade.draw_texture_rectangle(self.width//2, self.height//2 + 50, 200, 100, texture, 0)
            texture = self.menus['play']
            arcade.draw_texture_rectangle(self.width//2, self.height//2 - 50, texture.width, texture.height,texture, 0)

            #If statement to compute if there is a new highscore
            if self.new_highscore == True:
                texture = self.menus['highscore']
                arcade.draw_texture_rectangle(self.width // 2, self.height // 2 - 50, 100, 200, texture, 0)

            self.draw_score_board()


    def on_key_press(self, key, modifiers):

        if key == arcade.key.SPACE and self.state == State.MAIN_MENU:
            # If game state is back to playing , just change the state and return
            self.state = State.PLAYING
            
        if key == arcade.key.SPACE and self.double_jump:
            #If Space bar is pressed, self.jump is set to true and will aloow the player to jump
            self.jump = True
           

    def on_mouse_press(self, x, y, button, modifiers):
        #Function for the restart button if game is gameover. If the coordinates of the mouse press are within the coordinates of the image it will update the game
        #state and call setup again which is going to draw all the images again.

        if self.state == State.GAME_OVER:
            texture = self.menus['play']
            x_position = self.width//2
            y_position = self.height//2 - 50
            if x_position - texture.width//2 <= x <= x_position + texture.width//2:
                if y_position - texture.height//2 <= y <= y_position + texture.height//2:
                    self.setup()
                    self.state = State.MAIN_MENU


    def scoreboard(self):
        '''
        Function created to calculate the score by using a for loop
        '''

        #This is the initial x coordinate of the score on the screen
        center = 230
        self.score_board = arcade.SpriteList()

        #Down below in the on_update function, the self.score is going to be updated.
        #By using a for each loop the value num is used an index to find the right score image from the list SCORE
        for num in str(self.score):
            self.score_board.append(arcade.Sprite(SCORE[num], 1, center_x= center , center_y=440))
            center += 24


    def on_update(self, delta_time):

        """
        This a function to update all the images on screen before being drawn, (angles, positions....etc)
        """

        self.player_list.update_animation()

        if self.state == State.PLAYING:

            if self.jump:
                self.player.jump()
                self.jump = False
            

            if self.player.center_y <= 0 :
                
                self.state = State.GAME_OVER

            if self.player.top > self.height:
                self.player.top = self.height

            new_platform = None

            for plat in self.platform_sprites:
                if plat.right <= 0:
                    plat.kill()
                elif len(self.platform_sprites) == 1 and plat.right <= random.randrange(self.width // 2, self.width // 2 + 15):
                    new_platform = Platform.random_platform_generator(self.sprites, self.height)
 
            if new_platform:
                self.platform_sprites.append(new_platform)


            if self.player.center_x >= self.platform_sprites[0].center_x and not self.platform_sprites[0].scored:
                self.score += 1
                self.platform_sprites[0].scored = True
                print(self.score)

            hit = arcade.check_for_collision_with_list(self.player, self.platform_sprites)
            if self.player.center_y - self.player.height//2 <= self.platform_sprites[0].center_y + self.platform_sprites[0].height//2  and self.player.center_y >= self.platform_sprites[0].center_y - self.platform_sprites[0].height//2  and self.player.center_x <= self.platform_sprites[0].center_x + self.platform_sprites[0].width//2  and self.player.center_x >= self.platform_sprites[0].center_x - self.platform_sprites[0].width//2:
                self.double_jump = True

            if self.player.center_y > self.platform_sprites[0].center_y + 128:
                self.double_jump = False
            

            if self.player.center_y - self.player.height//2 <= self.platform_sprites[0].center_y + self.platform_sprites[0].height//2  and self.player.center_y >= self.platform_sprites[0].center_y - self.platform_sprites[0].height//2  and self.player.center_x <= self.platform_sprites[0].center_x + self.platform_sprites[0].width//2  and self.player.center_x >= self.platform_sprites[0].center_x - self.platform_sprites[0].width//2 :
                self.player.center_y = self.platform_sprites[0].center_y + self.platform_sprites[0].height//2 + self.player.height//2
                self.player.angle = 0

            if self.player.center_y + self.player.height//2 >= self.platform_sprites[0].center_y - self.platform_sprites[0].height//2 and self.player.center_y <= self.platform_sprites[0].center_y and self.player.center_x > self.platform_sprites[0].center_x - self.platform_sprites[0].width//2 and self.player.center_x < self.platform_sprites[0].center_x + self.platform_sprites[0].width//2:
                self.state = State.GAME_OVER


            # This calls update() method on each object in the SpriteList
            self.player.update(delta_time)
            self.player_list.update()
            self.platform_sprites.update()


    
        if self.state == State.GAME_OVER:
            self.player.update()

            self.scoreboard()


       

       

def main():
    game = Game(500, 500)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

'''
sprites['base'].height + min_height, height - gap_size - min_height)
'''