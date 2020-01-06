import random
from typing import List
import arcade


def bubbleSort(arr: List[int]) -> List[int]:
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

def make_character(head_radius,
                chest_height,
                chest_width,
                leg_width,
                leg_height,
                arm_width,
                arm_length,
                arm_gap,
                shoulder_height):

    shape_list = shape_list = arcade.ShapeElementList()

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

HEIGHT = 800
WIDTH = 600
GRAVITY = 5
BOUNCINESS = 0.000001


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

   
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

        self.shape_list.center_x , self.shape_list.center_y = WIDTH//2, HEIGHT//2
        self.shape_list.change_y -= GRAVITY 


        self.obstacles_list = []
        self.random_x = bubbleSort(random.sample(range(0, WIDTH, 75), 4))
        self.random_y = bubbleSort(random.sample(range(0, HEIGHT, 50), 6))
        
        for (i, j) in zip(self.random_x, self.random_y):
            self.obstacle = arcade.Sprite(center_x=i, center_y=j)
            self.obstacle.texture = arcade.make_soft_square_texture(50, arcade.color.BLUE, outer_alpha=255)

            self.obstacles_list.append(self.obstacle)
        
        

    def on_draw(self):
        arcade.start_render()

        for obs in self.obstacles_list:
            obs.draw()

        self.shape_list.draw()

    def on_update(self, delta_time):

        self.shape_list.center_y *= -GRAVITY
    
        

        #Hit the bottom
        if self.shape_list.center_y < 25:

            self.shape_list.center_y += BOUNCINESS

                    
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.D:
            self.shape_list.center_x += 3

        elif key == arcade.key.A:
            self.shape_list.center_x -= 3


def main():
    game = MyGame(WIDTH, HEIGHT, 'test')
    arcade.run()

if __name__ == "__main__":
    main()


