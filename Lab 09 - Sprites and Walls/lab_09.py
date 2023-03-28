import arcade

# --Constants--
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Speed
MOVEMENT_SPEED = 3
# Scaling
SPRITE_FENCE_SCALING = 1
SPRITE_PLAYER_SCALING = 1.5
SPRITE_COIN_SCALING = 0.2

fence_list = [[510, 400], [520, 400], [530, 400], [540, 400], ]


# Fence class inherits functionality of arcade.Sprite
class Fence(arcade.Sprite):
    def __init__(self, filename, SPRITE_FENCE_SCALING):
        super(Fence, self).__init__(filename, SPRITE_FENCE_SCALING)
        # attributes of the Fence class, the fence
        self.left_fence_corner_sprite = None
        self.right_fence_corner = None
        self.opening_for_fence_sprite = None
        self.middle_upward_fence_sprite = None
        self.middle_connector_sprite = None
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


# Coin class inherits functionality of arcade.Sprite
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


# Player class inherits functionality of arcade.Sprite

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


# MyGame class inherits functionality of arcade.Window
class MyGame(arcade.Window):
    """Initializer"""

    def __init__(self):
        # calls the parent class
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "SPRITES AND WALLS")
        # gives the list the functions/methods/attributes of the class
        self.fence_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()

    def setup(self):
        arcade.set_background_color(arcade.color.WHITE)
        # variable that defines the image of the coin
        coin_sprite = Coin("coinGold_ul copy.png", SPRITE_COIN_SCALING)
        coin_sprite.center_x = 450
        coin_sprite.center_y = 300
        # coin_lists adds the coin_sprite to the coin_list
        self.coin_list.append(coin_sprite)

        """Box fence 1"""
        # variables that defines the image of the fence, creates an instances of the class
        left_fence_corner_sprite = Fence("kenney_tiny-town/Tiles/tile_0068.png", SPRITE_FENCE_SCALING)
        left_fence_corner_sprite.center_x = 390
        left_fence_corner_sprite.center_y = 400
        # fence_list adds sprite to the fence_list
        self.fence_list.append(left_fence_corner_sprite)
        left_fence_corner_sprite02 = Fence("kenney_tiny-town/Tiles/tile_0044.png", SPRITE_FENCE_SCALING)
        left_fence_corner_sprite02.center_x = 390
        left_fence_corner_sprite02.center_y = 500
        # fence_list adds sprite to the fence_list
        self.fence_list.append(left_fence_corner_sprite02)
        right_fence_corner_sprite = Fence("kenney_tiny-town/Tiles/tile_0070.png", SPRITE_FENCE_SCALING)
        right_fence_corner_sprite.center_x = 700
        right_fence_corner_sprite.center_y = 400
        # fence_list adds sprite to the fence_list
        self.fence_list.append(right_fence_corner_sprite)
        right_fence_corner_sprite02 = Fence("kenney_tiny-town/Tiles/tile_0046.png", SPRITE_FENCE_SCALING)
        right_fence_corner_sprite02.center_x = 700
        right_fence_corner_sprite02.center_y = 500
        # fence_list adds sprite to the fence_list
        self.fence_list.append(right_fence_corner_sprite02)
        opening_for_fence_sprite = Fence("kenney_tiny-town/Tiles/tile_0069.png", SPRITE_FENCE_SCALING)
        opening_for_fence_sprite.center_x = 0
        opening_for_fence_sprite.center_y = 0
        # fence_list adds sprite to the fence_list
        self.fence_list.append(opening_for_fence_sprite)
        for fence in range(400, 500, 10):
            middle_upward_fence_sprite = Fence("kenney_tiny-town/Tiles/tile_0071.png", SPRITE_FENCE_SCALING)
            middle_upward_fence_sprite.center_x = 390
            middle_upward_fence_sprite.center_y = fence
            self.fence_list.append(middle_upward_fence_sprite)
        for fence in range(410, 500, 10):
            middle_upward_fence_sprite = Fence("kenney_tiny-town/Tiles/tile_0071.png", SPRITE_FENCE_SCALING)
            middle_upward_fence_sprite.center_x = 700
            middle_upward_fence_sprite.center_y = fence
            self.fence_list.append(middle_upward_fence_sprite)
        for fence in range(400, 700, 15):
            middle_connector_sprite = Fence("kenney_tiny-town/Tiles/tile_0045.png", SPRITE_FENCE_SCALING)
            # give the center_x the value that fence has in the list, continues to change with each placement of fence
            middle_connector_sprite.center_x = fence
            middle_connector_sprite.center_y = 400
            self.fence_list.append(middle_connector_sprite)
        for fence in range(400, 700, 15):
            middle_connector_sprite = Fence("kenney_tiny-town/Tiles/tile_0045.png", SPRITE_FENCE_SCALING)
            # give the center_x the value that fence has in the list, continues to change with each placement of fence
            middle_connector_sprite.center_x = fence
            middle_connector_sprite.center_y = 500
            self.fence_list.append(middle_connector_sprite)

        """Box fence 2"""
        # variables that defines the image of the fence, creates an instances of the class
        left_fence_corner_sprite = Fence("kenney_tiny-town/Tiles/tile_0068.png", SPRITE_FENCE_SCALING)
        left_fence_corner_sprite.center_x = 390
        left_fence_corner_sprite.center_y = 250
        # fence_list adds sprite to the fence_list
        self.fence_list.append(left_fence_corner_sprite)
        left_fence_corner_sprite02 = Fence("kenney_tiny-town/Tiles/tile_0044.png", SPRITE_FENCE_SCALING)
        left_fence_corner_sprite02.center_x = 390
        left_fence_corner_sprite02.center_y = 350
        # fence_list adds sprite to the fence_list
        self.fence_list.append(left_fence_corner_sprite02)
        right_fence_corner_sprite = Fence("kenney_tiny-town/Tiles/tile_0070.png", SPRITE_FENCE_SCALING)
        right_fence_corner_sprite.center_x = 700
        right_fence_corner_sprite.center_y = 250
        # fence_list adds sprite to the fence_list
        self.fence_list.append(right_fence_corner_sprite)
        right_fence_corner_sprite02 = Fence("kenney_tiny-town/Tiles/tile_0046.png", SPRITE_FENCE_SCALING)
        right_fence_corner_sprite02.center_x = 700
        right_fence_corner_sprite02.center_y = 350
        self.fence_list.append(right_fence_corner_sprite02)
        opening_for_fence_sprite = Fence("kenney_tiny-town/Tiles/tile_0069.png", SPRITE_FENCE_SCALING)
        opening_for_fence_sprite.center_x = 0
        opening_for_fence_sprite.center_y = 0
        # fence_list adds sprite to the fence_list
        self.fence_list.append(opening_for_fence_sprite)
        for fence in range(400, 700, 15):
            middle_connector_sprite = Fence("kenney_tiny-town/Tiles/tile_0045.png", SPRITE_FENCE_SCALING)
            # give the center_x the value that fence has in the list, continues to change with each placement of fence
            middle_connector_sprite.center_x = fence
            middle_connector_sprite.center_y = 350
            self.fence_list.append(middle_connector_sprite)
        for fence in range(400, 700, 15):
            middle_connector_sprite = Fence("kenney_tiny-town/Tiles/tile_0045.png", SPRITE_FENCE_SCALING)
            # give the center_x the value that fence has in the list, continues to change with each placement of fence
            middle_connector_sprite.center_x = fence
            middle_connector_sprite.center_y = 250
            self.fence_list.append(middle_connector_sprite)
        for fence in range(260, 345, 10):
            middle_upward_fence_sprite = Fence("kenney_tiny-town/Tiles/tile_0071.png", SPRITE_FENCE_SCALING)
            middle_upward_fence_sprite.center_x = 390
            middle_upward_fence_sprite.center_y = fence
            self.fence_list.append(middle_upward_fence_sprite)
        for fence in range(260, 345, 10):
            middle_upward_fence_sprite = Fence("kenney_tiny-town/Tiles/tile_0071.png", SPRITE_FENCE_SCALING)
            middle_upward_fence_sprite.center_x = 700
            middle_upward_fence_sprite.center_y = fence
            self.fence_list.append(middle_upward_fence_sprite)

        # variable that defines the image of the player
        player_sprite = Player("kenney_tiny-dungeon/Tiles/tile_0085.png", SPRITE_PLAYER_SCALING)
        player_sprite.center_x = 300
        player_sprite.center_y = 300
        # player_list adds the player_sprite to the player_list
        self.player_list.append(player_sprite)

    # method in the MyGame class that will update lists
    def update(self, delta_time: float):
        self.coin_list.update()
        self.fence_list.update()
        self.player_list.update()

    # method that will draw what is defined in the list
    def on_draw(self):
        arcade.start_render()
        self.coin_list.draw()
        self.fence_list.draw()
        self.player_list.draw()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()
