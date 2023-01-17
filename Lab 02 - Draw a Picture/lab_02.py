# Open the "arcade" library
import arcade

# Open up a window
# From the "arcade" library. use function called "open_window"
# Window title set to "Drawing Example"
# Window dimensions set to (width 800 and height 600)
arcade.open_window(800, 600, "Drawing Example")


# Set background color from library
arcade.set_background_color(arcade.color.BLUE)

# Ready to draw
arcade.start_render()

# Grass
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.GO_GREEN)

# House base
arcade.draw_lrtb_rectangle_filled(30, 300, 200, 150, arcade.color.FAWN)

# House base second color
arcade.draw_lrtb_rectangle_filled(30, 300, 300, 170, arcade.color.BONE)
# House door
arcade.draw_lrtb_rectangle_filled(140, 180, 220, 150, arcade.color.BURNT_UMBER)

# House window left
arcade.draw_lrtb_rectangle_filled(70, 100, 230, 200, arcade.color.BROWN)
# House window right
arcade.draw_lrtb_rectangle_filled(220, 255, 230, 200, arcade.color.BROWN)

# Roof from triangle with 3 points


arcade.finish_render()








# Keep window open
arcade.run()
