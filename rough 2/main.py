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


HEIGHT = 500
WIDTH = 500
GRAVITY = 0.2
BOUNCINESS = 1

class MyGame(arcade.Window):
    def __init__(self, width: int, height: int, title: str) -> None:
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)


        self.obstacles_list = []
        self.random_x = random.sample(range(25, WIDTH, 75),3)
        self.random_y = bubbleSort(random.sample(range(25, HEIGHT), 9))

        self.sprite1 = arcade.Sprite(center_x=self.random_x[0], center_y=self.random_y[0] + 200)
        self.sprite1.texture = arcade.load_texture(file_name="images/officeguy.png", scale = 0.03)
        
        for (i, j) in zip(self.random_x, self.random_y):
            self.obstacle = arcade.Sprite(center_x=i, center_y=j)
            self.obstacle.texture = arcade.load_texture(file_name="images/platform2.png", scale=0.1)
            self.obstacles_list.append(self.obstacle)
        
    def on_draw(self):
        arcade.start_render()
        self.sprite1.draw()
    
        for obs in self.obstacles_list:
            obs.draw()

        if self.sprite1.center_y < 20:
            self.sprite1.center_y = 20
            self.sprite1.change_y = 0
            # Draw the game over menu if the player lost and the restart play button
            texture = arcade.load_texture(file_name = "images/gameover.png")
            arcade.draw_texture_rectangle(WIDTH//2, HEIGHT//2, 200, 100, texture, 0)
       
    def update(self, delta_time):
        global BOUNCINESS

        self.sprite1.update()

        self.sprite1.change_y -= GRAVITY 

        #Hit the bottom

        #if ball goes beyond width
        if self.sprite1.center_x > WIDTH + 25:
            self.sprite1.center_x = -25

        elif self.sprite1.center_x < -25:
            self.sprite1.center_x = WIDTH + 25

        #if ball hits obstacles
        for obs in self.obstacles_list:
            if self.sprite1.collides_with_sprite(obs):
                self.sprite1.change_y *= -BOUNCINESS // 4
                self.sprite1.change_x = 0
        
            
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.D:
            self.sprite1.change_x = 5

        elif key == arcade.key.A:
            self.sprite1.change_x = -5

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.D or key == arcade.key.A:
            self.sprite1.change_x = 0

def main():
    game = MyGame(WIDTH, HEIGHT, 'test')
    arcade.run()


if __name__ == "__main__":
    main()

