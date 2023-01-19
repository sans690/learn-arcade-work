import arcade

Screen_Width = 1000
Screen_Height = 800


def snow_man(x, y):
    """Draw a snow man"""
    # Point for x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # snow
    arcade.draw_circle_filled(x + 20, 60 + y, 60, arcade.color.SNOW)
    arcade.draw_circle_filled(x + 20, 135 + y, 50, arcade.color.SNOW)
    arcade.draw_circle_filled(x + 20, 195 + y, 40, arcade.color.SNOW)

    # eyes
    arcade.draw_circle_filled(5 + x, 200 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(35 + x, 200 + y, 5, arcade.color.BLACK)


def grass():
    arcade.draw_lrtb_rectangle_filled(0, Screen_Width, Screen_Height / 3, 0, arcade.color.BONE)


def on_draw(delta_time):
    arcade.start_render()
    grass()
    snow_man(on_draw.snow_man1_x, 140)
    snow_man(450, 180)
    snow_man(600, 160)

    on_draw.snow_man1_x += 1


on_draw.snow_man1_x = 150


def main():
    arcade.open_window(Screen_Width, Screen_Height, "Drawing Example")
    arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

    # Finish and run program
    arcade.schedule(on_draw, 1 / 60)
    arcade.run()


main()
