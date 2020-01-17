


import json


sorted_list = []
user = int(input("Enter a value: "))

def bubblesort(numbers):
    n = len(numbers)

    for i in range(n):
        for j in range(n - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    return numbers


with open("score.json", "r") as f:
    data = json.load(f)
    


data[f"user {len(data) + 1}"] = user

with open("score.json", 'w') as f:
    json.dump(data, f)


def score_board():
    with open("score.json", "r") as f:
        data = json.load(f)

    for values in data.values():
        sorted_list.append(values)
        bubblesort(sorted_list)
   

    for i in range(len(sorted_list)):
        print(f"{i}. {sorted_list[i]}")

        
    
        

result = score_board()




'''
display 10 best, remove the worst, if you get a new high score, use search to get the worst high score
when game is over self.score = self.highscor








import arcade
import random

screen_height = 800
screen_width = 600



class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

        self.sprites_list = arcade.SpriteList()


        for _ in range(3):
            self.sprite1 = arcade.Sprite()
            self.sprite1.texture = arcade.make_soft_square_texture(50, arcade.color.BLUE, outer_alpha=255)
            self.sprite1.center_x = 500
            self.sprite1.center_y = random.randrange(200, 600)
            self.sprites_list.append(self.sprite1)

            
    def draw_sprites(self, index):
        n = len(self.sprites_list)

        if index > n:
            return True

        elif index < n:
            self.sprites_list[index].change_x = -2
            self.sprites_list[index].draw()

            if self.sprites_list[index].center_x <= 10:
                return self.draw_sprites(index+1)

    def on_draw(self):
        arcade.start_render()
        self.draw_sprites(0)


    def on_update(self, dt):
        self.sprites_list.update()


def main():
    game = MyGame(screen_width, screen_height, ".")

    arcade.run()

if __name__ == "__main__":
    main()
'''