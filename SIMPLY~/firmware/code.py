import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

pins = [
    board.GP0, board.GP1, board.GP2, board.GP3,
    board.GP4, board.GP5, board.GP6, board.GP7
]

buttons = []
for pin in pins:
    button = digitalio.DigitalInOut(pin)
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP
    buttons.append(button)

keymap = [
    Keycode.ONE, Keycode.TWO, Keycode.THREE, Keycode.FOUR,
    Keycode.FIVE, Keycode.SIX, Keycode.SEVEN, Keycode.EIGHT
]

while True:
    for i in range(8):
        if not buttons[i].value:
            kbd.press(keymap[i])
        else:
            kbd.release(keymap[i])