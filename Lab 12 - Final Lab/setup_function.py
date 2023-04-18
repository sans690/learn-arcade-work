from part_12 import Player, PLAYER_SCALING


def setup(self):
    self.player_sprite = Player("Player Resources/output2.png", PLAYER_SCALING)
    self.player_sprite.center_x = 0
    self.player_sprite.center_y = 0

    # condition
    # if the current room is 0, then do this code
    if self.current_room == 0:
        self.load_level()
        self.player_sprite.center_x = 300
        self.player_sprite.center_y = 150
        self.player_sprite_list.append(self.player_sprite)

    # condition
    # if the current room is 1, then do this code
    elif self.current_room == 1:
        self.load_level()
        self.player_sprite.center_x = 800
        self.player_sprite.center_y = 270
        # player_sprite_list adds sprite give by self.player_sprite
        self.player_sprite_list.append(self.player_sprite)

    # condition
    # if the current room is 2, then do this code
    elif self.current_room == 2:
        self.load_level()
        self.player_sprite.center_x = 1055
        self.player_sprite.center_y = 640
        # player_sprite_list adds sprite give by self.player_sprite
        self.player_sprite_list.append(self.player_sprite)

    # condition
    # if the current room is 2, then do this code
    elif self.current_room == 3:
        self.load_level()
        self.player_sprite.center_x = 1160
        self.player_sprite.center_y = 20
        # player_sprite_list adds sprite give by self.player_sprite
        self.player_sprite_list.append(self.player_sprite)
