import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class SpaceGameWindow(arcade.Window):
    def __init__(self,width,height):
        super().__init__(width,height)

        arcade.set_background_color(arcade.color.BLACK)
        
        self.ship = arcade.Sprite('image/ship.png')
        self.ship.set_position(100,100)


    def on+fraw(self):
        arcade.start_render()
        
        self.ship.draw()

if __name__=='__main__':
    window = SpaceGameWindow(SCREEN_Width,SCREEN_HEIGHT)
    arcade.run()
