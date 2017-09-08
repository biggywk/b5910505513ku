import arcade
from models import Ship
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class SpaceGameWindow(arcade.Window):


    def on_draw(self):
        arcade.start_render()
        
        self.ship.draw()
   
class Ship:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, delta):
        if self.y > 600:
            self.y = 0
        self.y += 5

if __name__=='__main__':
    window = SpaceGameWindow(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.run()
