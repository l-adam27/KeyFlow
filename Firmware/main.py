import time
import board
import digitalio
import rotaryio

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

# =====================
# HID Setup
# =====================
keyboard = Keyboard(board.USB_HID_DEVICES)
consumer = ConsumerControl(board.USB_HID_DEVICES)

# =====================
# Buttons (ajuste os pinos conforme seu PCB)
# =====================
buttons = [
    board.GP0,  # Key 1 - Screenshot
    board.GP1,  # Key 2 - Play / Pause
    board.GP2,  # Key 3 - Lock Screen
    board.GP3,  # Key 4 - Focus Mode
    board.GP5,  # Key 5 - Clean
    board.GP4,  # Key 6 - Mic Mute
]

keys = []

for pin in buttons:
    btn = digitalio.DigitalInOut(pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP
    keys.append(btn)

# =====================
# Rotary Encoder
# =====================
encoder = rotaryio.IncrementalEncoder(board.GP6, board.GP7)
encoder_button = digitalio.DigitalInOut(board.GP8)
encoder_button.direction = digitalio.Direction.INPUT
encoder_button.pull = digitalio.Pull.UP

last_position = encoder.position

# =====================
# Helper Functions
# =====================
def screenshot():
    keyboard.press(Keycode.CONTROL, Keycode.SHIFT, Keycode.S)
    keyboard.release_all()

def play_pause():
    consumer.send(ConsumerControlCode.PLAY_PAUSE)

def lock_screen():
    keyboard.press(Keycode.WINDOWS, Keycode.L)
    keyboard.release_all()

def focus_mode():
    # Clean desktop
    keyboard.press(Keycode.WINDOWS, Keycode.D)
    keyboard.release_all()
    time.sleep(0.4)

    # Open Start
    keyboard.press(Keycode.WINDOWS)
    keyboard.release_all()
    time.sleep(0.5)

    # Type "Clock"
    keyboard.send(Keycode.C, Keycode.L, Keycode.O, Keycode.C, Keycode.K)
    time.sleep(0.3)

    # Enter
    keyboard.send(Keycode.ENTER)

def clean_desktop():
    keyboard.press(Keycode.WINDOWS, Keycode.D)
    keyboard.release_all()

def mic_mute():
    keyboard.press(Keycode.CONTROL, Keycode.SHIFT, Keycode.M)
    keyboard.release_all()

# =====================
# Main Loop
# =====================
while True:
    # Buttons
    if not keys[0].value:
        screenshot()
        time.sleep(0.3)

    if not keys[1].value:
        play_pause()
        time.sleep(0.3)

    if not keys[2].value:
        lock_screen()
        time.sleep(0.3)

    if not keys[3].value:
        focus_mode()
        time.sleep(0.5)

    if not keys[4].value:
        clean_desktop()
        time.sleep(0.3)

    if not keys[5].value:
        mic_mute()
        time.sleep(0.3)

    # Encoder rotation
    position = encoder.position
    if position > last_position:
        consumer.send(ConsumerControlCode.VOLUME_INCREMENT)
    elif position < last_position:
        consumer.send(ConsumerControlCode.VOLUME_DECREMENT)

    last_position = position

    # Encoder click
    if not encoder_button.value:
        consumer.send(ConsumerControlCode.MUTE)
        time.sleep(0.3)

    time.sleep(0.01)
