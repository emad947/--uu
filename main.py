def on_button_pressed_a():
 rain= game.create_sprite(randint(9, -1),0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
   a=2000
   b=1000
   if a> b:
       basic.show_string("a is greater than b")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_ab():
   game.create_sprite(2, 3)
input.on_button_pressed(Button.AB, on_button_pressed_ab)