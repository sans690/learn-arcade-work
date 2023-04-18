import load_level_function


def update(self):
    self.player_sprite_list.update()
    # scrolls screen to player
    self.scroll_to_player()
    if self.current_room == 0 or self.current_room == 1:
        self.physics_engine.update()
        self.physics_engine001.update()

    if self.current_room == 2:
        self.physics_engine.update()
        self.physics_engine001.update()
        self.physics_engine002.update()
        self.physics_engine003.update()
        self.physics_engine004.update()
    if self.current_room == 3:

        self.physics_engine.update()
        self.physics_engine001.update()
        self.physics_engine002.update()
        self.physics_engine003.update()

    # condition
    # if the current room is 0, then do this code (movement between rooms)
    # if player tries to move outside boundary, they are stopped
    if self.current_room == 0:
        if self.player_sprite.center_x > 500:
            self.player_sprite.center_x = 500
        if self.player_sprite.center_x < 10:
            self.player_sprite.center_x = 10
        if self.player_sprite.center_y > 280:
            self.player_sprite.center_y = 280
            while self.player_sprite.center_y >= 275 and self.player_sprite.center_x >= 210 and self.current_room == 0 \
                    and self.player_sprite.center_x <= 280:
                self.current_room += 1
                self.load_level()
                self.player_sprite.center_x = 480
                self.player_sprite.center_y = 15
        elif self.player_sprite.center_y < 10:
            self.player_sprite.center_y = 15

    # condition
    # if the current room is 1, then do this code (movement between rooms)
    # if player tries to move outside boundary, they are stopped
    if self.current_room == 1:
        if self.player_sprite.center_x > 850:
            self.player_sprite.center_x = 850
        if self.player_sprite.center_x < 10:
            self.player_sprite.center_x = 10
        if self.player_sprite.center_y > 265:
            self.player_sprite.center_y = 265
        if self.player_sprite.center_y < 10:
            self.player_sprite.center_y = 15
            while self.player_sprite.center_y <= 20 and self.player_sprite.center_x >= 450 and \
                    self.current_room == 1 and self.player_sprite.center_x <= 515:
                self.current_room -= 1
                load_level_function.load_level(self)
                self.player_sprite.center_x = 230
                self.player_sprite.center_y = 278
            while self.player_sprite.center_y <= 20 and self.player_sprite.center_x >= 35 and self.current_room == 1\
                    and self.player_sprite.center_x <= 150:
                self.current_room += 1
                load_level_function.load_level(self)
                self.player_sprite.center_x = 1050
                self.player_sprite.center_y = 643

    # condition
    # if the current room is 2, then do this code (movement between rooms)
    # if player tries to move outside boundary, they are stopped
    if self.current_room == 2:
        if self.player_sprite.center_x > 1720:
            self.player_sprite.center_x = 1720
        if self.player_sprite.center_x < 10:
            self.player_sprite.center_x = 10
        if self.player_sprite.center_y < 10:
            self.player_sprite.center_y = 10
        if self.player_sprite.center_y > 860:
            self.player_sprite.center_y = 860
    while self.player_sprite.center_x <= 1065 and self.player_sprite.center_y >= 645 and self.player_sprite.center_x >= 1050 and self.current_room == 2:
        self.current_room -= 1
        load_level_function.load_level(self)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 25
