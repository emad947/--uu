input.onButtonPressed(Button.A, function on_button_pressed_a() {
    let rain = game.createSprite(randint(9, -1), 0)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    let a = 2000
    let b = 1000
    if (a > b) {
        basic.showString("a is greater than b")
    }
    
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    game.createSprite(2, 3)
})
