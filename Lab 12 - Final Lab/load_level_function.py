import arcade

# --Constant--
MAP_SCALING = 1.8


def load_level(self):
    # Bedroom
    if self.current_room == 0:
        resource = "Inside Resources/Gen4Bedroom.tmj"
        objects = "Objects"
        tables = "Tables"
        # tells attribute to equal arcade's library to do load_tilemap function
        self.tile_map = arcade.load_tilemap(f"{resource}", MAP_SCALING)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.tile_map.sprite_lists[f"{objects}"])
        self.physics_engine001 = arcade.PhysicsEngineSimple(self.player_sprite,
                                                            self.tile_map.sprite_lists[f"{tables}"])
    # Downstairs
    elif self.current_room == 1:
        resource = "Inside Resources/Gen4Kitchen.tmj"
        objects = "Objects"
        tables = "Tables"
        # tells attribute to equal arcade's library to do load_tilemap function
        self.tile_map = arcade.load_tilemap(f"{resource}", MAP_SCALING)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.tile_map.sprite_lists[f"{objects}"])
        self.physics_engine001 = arcade.PhysicsEngineSimple(self.player_sprite,
                                                            self.tile_map.sprite_lists[f"{tables}"])
    # Outside
    elif self.current_room == 2:
        resource = "Outside Resources/Version 3/OutsideTilemap.tmj"
        fences = "Fence"
        trees01 = "Trees(with collision)"
        buildings = "Buildings"
        trees00 = "Trees"
        objects = "Objects"

        # tells attribute to equal arcade's library to do load_tilemap function
        self.tile_map = arcade.load_tilemap(f"{resource}", MAP_SCALING)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.tile_map.sprite_lists[f"{fences}"])
        self.physics_engine001 = arcade.PhysicsEngineSimple(self.player_sprite,
                                                            self.tile_map.sprite_lists[f"{trees01}"])
        self.physics_engine002 = arcade.PhysicsEngineSimple(self.player_sprite,
                                                            self.tile_map.sprite_lists[f"{buildings}"])
        self.physics_engine003 = arcade.PhysicsEngineSimple(self.player_sprite,
                                                            self.tile_map.sprite_lists[f"{trees00}"])
        self.physics_engine004 = arcade.PhysicsEngineSimple(self.player_sprite,
                                                            self.tile_map.sprite_lists[f"{objects}"])

        # Wild
    elif self.current_room == 3:
        resource = "Outside Resources/Version 2/WildGen4Tilemap.tmj"
        fences = "Fence"
        trees01 = "Trees(with collision)"
        trees00 = "Trees"
        objects = "Objects"

        # tells attribute to equal arcade's library to do load_tilemap function
        self.tile_map = arcade.load_tilemap(f"{resource}", MAP_SCALING)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.tile_map.sprite_lists[f"{fences}"])
        self.physics_engine001 = arcade.PhysicsEngineSimple(self.player_sprite,
                                                            self.tile_map.sprite_lists[f"{trees01}"])
        self.physics_engine002 = arcade.PhysicsEngineSimple(self.player_sprite,
                                                            self.tile_map.sprite_lists[f"{trees00}"])
        self.physics_engine003 = arcade.PhysicsEngineSimple(self.player_sprite,
                                                            self.tile_map.sprite_lists[f"{objects}"])
