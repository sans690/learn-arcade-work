import arcade
from pyglet.math import Vec2

# --Constants--
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_MOVEMENT_SPEED = 1.8
MAP_SCALING = 1.8
PLAYER_SCALING = .05
CAMERA_SPEED = 1
# how many pixels to keep between the character and screen edge
VIEWPORT_MARGIN = 250


# Player class inherits arcade's Sprite class
class Player(arcade.Sprite):
    """Initializer"""

    def __init__(self, filename, scale):
        super(Player, self).__init__(filename, scale)
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


class Monster(arcade.Sprite):
    """Initializer"""

    def __init__(self, filename, scale):
        super(Monster, self).__init__(filename, scale)
        self.center_x = 0
        self.center_y = 0
        self.change_x = 0
        self.change_y = 0

    # method of Monster class that tells the class how to move when called
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
        self.tile_map = None
        self.player_sprite = None
        self.npc_sprite = None
        self.monster_sprite = None
        # creates camera for player
        self.camera_sprite = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.physics_engine = None
        self.current_room = 0

        # lists
        self.player_sprite_list = arcade.SpriteList()
        self.npc_sprite_list = arcade.SpriteList()
        self.monster_sprite_list = arcade.SpriteList()
        self.room_list = []

    def load_level_kitchen(self):
        # tells attribute to equal arcade's library to do load_tilemap function
        resource = "Inside Resources/KitchenTilemap.tmj"
        objects = "Objects"
        self.tile_map = arcade.load_tilemap(f"{resource}", MAP_SCALING)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.tile_map.sprite_lists[f"{objects}"])

    def load_level_bedroom(self):
        # tells attribute to equal arcade's library to do load_tilemap function
        resource = "Inside Resources/BedroomTilemap.tmj"
        objects = "Objects"
        self.tile_map = arcade.load_tilemap(f"{resource}", MAP_SCALING)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.tile_map.sprite_lists[f"{objects}"])

    # sets up the game, defines the values for objects and anything else in the game
    def setup(self):
        self.player_sprite = Player("output2.png", PLAYER_SCALING)
        self.player_sprite.center_x = 0
        self.player_sprite.center_y = 0
        # condition
        # if the current room is 0, then do this code
        if self.current_room == 0:
            self.load_level_bedroom()
            self.player_sprite.center_x = 200
            self.player_sprite.center_y = 20
            self.player_sprite_list.append(self.player_sprite)
            # condition
            # if the current room is 1, then do this code
        if self.current_room == 1:
            self.load_level_kitchen()
            self.player_sprite.center_x = 480
            self.player_sprite.center_y = 15
            # player_sprite_list adds sprite give by self.player_sprite
            self.player_sprite_list.append(self.player_sprite)

    def update(self, delta_time: float):
        self.player_sprite_list.update()
        # scrolls screen to player
        self.scroll_to_player()
        self.physics_engine.update()
        # condition
        # if the current room is 0, then do this code
        if self.current_room == 0:
            if self.player_sprite.center_x > 280:
                self.player_sprite.center_x = 280
            elif self.player_sprite.center_x < 10:
                self.player_sprite.center_x = 10
            elif self.player_sprite.center_y > 280:
                self.player_sprite.center_y = 275
                while self.player_sprite.center_y >= 275 and self.player_sprite.center_x >= 230 and self.current_room == 0:
                    self.current_room = 1
                    self.load_level_kitchen()
                    self.player_sprite.center_x = 480
                    self.player_sprite.center_y = 15
            elif self.player_sprite.center_y < 10:
                self.player_sprite.center_y = 20
                self.player_sprite_list.update()
        # condition
        # if the current room is 1, then do this code
        # if player tries to move outside boundary, they are stopped
        if self.current_room == 1:
            if self.player_sprite.center_x > 560:
                self.player_sprite.center_x = 560
            elif self.player_sprite.center_x < 10:
                self.player_sprite.center_x = 10
            elif self.player_sprite.center_y > 265:
                self.player_sprite.center_y = 265
            elif self.player_sprite.center_y < 10:
                self.player_sprite.center_y = 20
                self.player_sprite_list.update()

    # when the key is pressed the player is moved
    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.W:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED

    # when the player releases the key
    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0

    def scroll_to_player(self):
        # based on where the player is, the camera will position to be centered on player
        # so window width is 800, player is at 100, 800/2 = 400, 100 - 400 = -300, so camera will start at -300
        position = Vec2(self.player_sprite.center_x - self.width / 2, self.player_sprite.center_y - self.height / 2)
        # camera will move to position at set speed
        self.camera_sprite.move_to(position, CAMERA_SPEED)

    def on_resize(self, width: float, height: float):
        # resizes the window when player hits edge
        self.camera_sprite.resize(int(width), int(height))

    def on_draw(self):
        arcade.start_render()
        # selects the camera to use for player sprite
        self.camera_sprite.use()
        arcade.set_background_color((20, 20, 30))
        if self.current_room == 0:
            self.tile_map.sprite_lists["Tile Layer 1"].draw()
            self.tile_map.sprite_lists["Carpets"].draw()
            self.tile_map.sprite_lists["Objects"].draw()

        if self.current_room == 1:
            self.tile_map.sprite_lists["Tile Layer 1"].draw()
            self.tile_map.sprite_lists["Carpets"].draw()
            self.tile_map.sprite_lists["Objects"].draw()
        self.player_sprite_list.draw()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()

