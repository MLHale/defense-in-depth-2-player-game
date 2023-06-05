def on_received_number(receivedNumber):
    if receivedNumber == 1:
        led.plot(0, 0)
    elif receivedNumber == 2:
        led.plot(1, 0)
    elif receivedNumber == 3:
        led.plot(2, 0)
    elif receivedNumber == 4:
        led.plot(3, 0)
    elif receivedNumber == 5:
        led.plot(4, 0)
    elif receivedNumber == 6:
        led.plot(0, 1)
    elif receivedNumber == 7:
        led.plot(1, 1)
    elif receivedNumber == 8:
        led.plot(2, 1)
    elif receivedNumber == 9:
        led.plot(3, 1)
    elif receivedNumber == 10:
        led.plot(4, 1)
    elif receivedNumber == 11:
        led.plot(0, 2)
    elif receivedNumber == 12:
        led.plot(1, 2)
    elif receivedNumber == 13:
        led.plot(2, 2)
    elif receivedNumber == 14:
        led.plot(3, 2)
    elif receivedNumber == 15:
        led.plot(4, 2)
    elif receivedNumber == 16:
        led.plot(0, 3)
    elif receivedNumber == 17:
        led.plot(1, 3)
    elif receivedNumber == 18:
        led.plot(2, 3)
    elif receivedNumber == 19:
        led.plot(3, 3)
    elif receivedNumber == 20:
        led.plot(4, 3)
    elif receivedNumber == 21:
        led.plot(0, 4)
    elif receivedNumber == 22:
        led.plot(1, 4)
    elif receivedNumber == 23:
        led.plot(2, 4)
    elif receivedNumber == 24:
        led.plot(3, 4)
    elif receivedNumber == 25:
        led.plot(4, 4)
    else:
        basic.show_string("Err")
radio.on_received_number(on_received_number)

def on_logo_long_pressed():
    basic.pause(200)
    # Send a number 16-20 for layer 4
    radio.send_number(16)
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def on_button_pressed_a():
    basic.pause(200)
    # Send a number 1-5 for layer 1
    radio.send_number(2)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    if receivedString == "blocked":
        basic.show_icon(IconNames.NO)
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    basic.pause(200)
    # Send a number 6-10 for layer 2
    radio.send_number(6)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.pause(200)
    # Send a number 21-25 for layer 5
    radio.send_number(21)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    basic.pause(200)
    # Send a number 11-15 for layer 3
    radio.send_number(11)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

# Set this to be the same as your groupmate
radio.set_group(1)
# Set this to be the same as your groupmate
radio.set_frequency_band(1)