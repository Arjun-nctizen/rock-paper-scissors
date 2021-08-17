def on_button_pressed_a():
    basic.show_leds("""
        . . . . .
                . # # # .
                . # # # .
                . # # # .
                . . . . .
    """)
    basic.pause(500)
    basic.show_string("Rock")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_leds("""
        # # # # #
                # . . . #
                # . . . #
                # . . . #
                # # # # #
    """)
    basic.pause(500)
    basic.show_string("Paper")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_leds("""
        # # . . #
                # # . # .
                . . # . .
                # # . # .
                # # . . #
    """)
    basic.pause(500)
    basic.show_string("Scissors")
input.on_button_pressed(Button.B, on_button_pressed_b)
