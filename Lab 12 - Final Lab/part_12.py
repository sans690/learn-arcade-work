import arcade

# --Constants--
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PlAYER_MOVEMENT_SPEED = 3


# Player class inherits arcade's Sprite class
class Player(arcade.Sprite):
    """Initializer"""

    def __init__(self, filename, scale):
        super(Player, self).__init__(filename, scale)
        self.filename = None
        self.scale = None
        self.center_x = 0
        self.center_y = 0
        self.change_x = 0
        self.change_y = 0

    # method of Player class that tells the class how to move when called
    def update(self):
        # current x position = current x position plus the change to x
        self.center_x += self.change_x
        # current y position = current y position plus the change to y
        self.center_y += self.change_y


class NPC(arcade.Sprite):
    """Initializer"""

    def __init__(self, filename, scale):
        super(NPC, self).__init__(filename, scale)
        self.filename = None
        self.scale = None
        self.center_x = 0
        self.center_y = 0
        self.change_x = 0
        self.change_y = 0

    # method of NPC class that tells the class how to move when called
    def update(self):
        # current x position = current x position plus the change to x
        self.center_x += self.change_x
        # current y position = current y position plus the change to y
        self.center_y += self.change_y


class Mon(arcade.Sprite):
    """Initializer"""

    def __init__(self, filename, scale):
        super(Mon, self).__init__(filename, scale)
        self.filename = None
        self.scale = None
        self.center_x = 0
        self.center_y = 0
        self.change_x = 0
        self.change_y = 0

    # method of Mon class that tells the class how to move when called
    def update(self):
        # current x position = current x position plus the change to x
        self.center_x += self.change_x
        # current y position = current y position plus the change to y
        self.center_y += self.change_y


class MyGame(arcade.Window):
    """Initializer"""

    def __init__(self):
        # calls that parent class arcade.Window and inherits the methods/attributes/functions of that class
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Test")
        # sets attributes to the class
        # empty variables is set
        self.scene = None
        self.tile_map = None
        self.player_sprite = None
        self.npc_sprite = None
        self.mon_sprite = None

        # lists
        self.player_sprite_list = arcade.SpriteList()
        self.npc_sprite_list = arcade.SpriteList()
        self.mon_sprite_list = arcade.SpriteList()

    # sets up the game, defines the values for objects and anything else in the game
    def setup(self):
        # tells attribute to equal arcade's library to do load_tilemap function
        self.tile_map = arcade.load_tilemap("Inside Resources/KitchenTilemao.tmj", 1)
        # tells attribute to equal arcade's library Scene class and do the from_tilemap function
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

    def setup2(self):
        # tells attribute to equal arcade's library to do load_tilemap function
        self.tile_map = arcade.load_tilemap("Inside Resources/BedroomTilemao.tmj", 1)
        # tells attribute to equal arcade's library Scene class and do the from_tilemap function
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

    #  def on_update(self, delta_time: float):

    def on_draw(self):
        self.scene.draw()

    # when the key is pressed the player is moved
    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.W:
            self.player_sprite.change_y = PlAYER_MOVEMENT_SPEED
        elif key == arcade.key.A:
            self.player_sprite.change_x = -PlAYER_MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player_sprite.change_y = - PlAYER_MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player_sprite.change_x = PlAYER_MOVEMENT_SPEED

    # when the player releases the key
    def on_key_release(self, key: int, modifiers: int):
        if arcade.key.A or arcade.key.D:
            self.player_sprite.change_x = 0
        elif arcade.key.W or arcade.key.S:
            self.player_sprite.change_y = 0


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()
