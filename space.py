import arcade
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
from ship import Ship
class SpaceGameWindow(arcade.Window):
    def __init__(self,width,height):
        super().__init__(width,height)

        arcade.set_background_color(arcade.color.BLACK)
        
        self.ship = Ship(100,100)
        self.ship_sprite = arcade.Sprite('ship.png')


    def on_draw(self):
        arcade.start_render()
        
        self.ship_sprite.draw()

    def update(self, delta):
        ship = self.ship
        ship.update(delta)
        self.ship_sprite.set_position(ship.x, ship.y)
if __name__=='__main__':
    window = SpaceGameWindow(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.run()
