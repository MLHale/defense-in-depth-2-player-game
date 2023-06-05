radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        led.plot(0, 0)
    } else if (receivedNumber == 2) {
        led.plot(1, 0)
    } else if (receivedNumber == 3) {
        led.plot(2, 0)
    } else if (receivedNumber == 4) {
        led.plot(3, 0)
    } else if (receivedNumber == 5) {
        led.plot(4, 0)
    } else if (receivedNumber == 6) {
        led.plot(0, 1)
    } else if (receivedNumber == 7) {
        led.plot(1, 1)
    } else if (receivedNumber == 8) {
        led.plot(2, 1)
    } else if (receivedNumber == 9) {
        led.plot(3, 1)
    } else if (receivedNumber == 10) {
        led.plot(4, 1)
    } else if (receivedNumber == 11) {
        led.plot(0, 2)
    } else if (receivedNumber == 12) {
        led.plot(1, 2)
    } else if (receivedNumber == 13) {
        led.plot(2, 2)
    } else if (receivedNumber == 14) {
        led.plot(3, 2)
    } else if (receivedNumber == 15) {
        led.plot(4, 2)
    } else if (receivedNumber == 16) {
        led.plot(0, 3)
    } else if (receivedNumber == 17) {
        led.plot(1, 3)
    } else if (receivedNumber == 18) {
        led.plot(2, 3)
    } else if (receivedNumber == 19) {
        led.plot(3, 3)
    } else if (receivedNumber == 20) {
        led.plot(4, 3)
    } else if (receivedNumber == 21) {
        led.plot(0, 4)
    } else if (receivedNumber == 22) {
        led.plot(1, 4)
    } else if (receivedNumber == 23) {
        led.plot(2, 4)
    } else if (receivedNumber == 24) {
        led.plot(3, 4)
    } else if (receivedNumber == 25) {
        led.plot(4, 4)
    } else {
        basic.showString("Err")
    }
})
input.onLogoEvent(TouchButtonEvent.LongPressed, function () {
    basic.pause(200)
    // Send a number 16-20 for layer 4
    radio.sendNumber(16)
})
input.onButtonPressed(Button.A, function () {
    basic.pause(200)
    // Send a number 1-5 for layer 1
    radio.sendNumber(2)
})
input.onButtonPressed(Button.AB, function () {
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
})
radio.onReceivedString(function (receivedString) {
    if (receivedString == "blocked") {
        basic.showIcon(IconNames.No)
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    }
})
input.onButtonPressed(Button.B, function () {
    basic.pause(200)
    // Send a number 6-10 for layer 2
    radio.sendNumber(6)
})
input.onGesture(Gesture.Shake, function () {
    basic.pause(200)
    // Send a number 21-25 for layer 5
    radio.sendNumber(21)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.pause(200)
    // Send a number 11-15 for layer 3
    radio.sendNumber(11)
})
// Set this to be the same as your groupmate
radio.setGroup(1)
// Set this to be the same as your groupmate
radio.setFrequencyBand(1)
