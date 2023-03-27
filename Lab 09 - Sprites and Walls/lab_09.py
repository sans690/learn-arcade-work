import arcade

# --Constants--
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 3

SPRITE_BOX_SCALING = 0.5
SPRITE_PLAYER_SCALING = 0.5
SPRITE_COIN_SCALING = 0.5

class Fence(arcade.Sprite):
    def __init__(self, filename, SPRITE_BOX_SCALING):
        super(Fence, self).__init__(filename, SPRITE_BOX_SCALING)
        # attributes of the Fence class, the fence
        self.left_fence_corner_sprite = None
        self.middle_fence_sprite = None
        self.right_fence_corner = None
        self.opening_for_fence_sprite = None
        self.middle_upward_fence_sprite = None

        # attributes of the Fence class, position of the fence image
        self.center_x = 0
        self.center_y = 0
        self.change_x = 0
        self.change_y = 0
    # method that updates the fence sprite
    def update(self):
        # current x position = current x position plus the change
        self.center_x += self.change_x
        # current y position = current y position plus the change
        self.center_y += self.change_y

class Coin(arcade.Sprite):
    def __init__(self, filename, SPRITE_COIN_SCALING):
        super(Coin, self).__init__(filename, SPRITE_COIN_SCALING)
        # attribute of the Coin class, the coin image
        self.coin = None
        # attribute of the Coin class, position on the coins
        self.center_x = 0
        self.center_y = 0
        self.change_x = 0
        self.change_y = 0
    # method that updates the coin sprite
    def update(self):
        # current x position = current x position plus the change
        self.center_x += self.change_x
        # current y position = current y position plus the change
        self.center_y += self.change_y

class Player(arcade.Sprite):
    def __init__(self, filename, SPRITE_PLAYER_SCALING):
        super(Player, self).__init__(filename, SPRITE_PLAYER_SCALING)

        # attributes of the Player class, player image
        self.player = None

        # attributes of the Player class, position of the player
        self.center_x = 0
        self.center_y = 0
        self.change_x = 0
        self.change_y = 0
    # method that updates the position of the player
    def update(self):
        # current x position = current x position plus the change
        self.center_x += self.change_x
        # current y position = current y position plus the change
        self.center_y += self.change_y

class MyGame(arcade.Window):
    """Initializer"""
    def __init__(self):
        # calls the parent class
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "SPRITES AND WALLS")

        self.fence_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.player_list =arcade.SpriteList()
    def setup(self):
        arcade.set_background_color(arcade.color.WHITE)
        # variable that defines the image of the coin
        coin_sprite = Coin("coinGold_ul copy.png", SPRITE_COIN_SCALING)
        # coin_lists adds the coin_sprite to the coin_list
        self.coin_list.append(coin_sprite)



    def update(self, delta_time: float):

    def on_draw(self):
        arcade.start_render()

def main():
    window = MyGame
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()


