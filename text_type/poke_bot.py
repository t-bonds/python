import keyboard as keyboard
from pynput.mouse import Button, Controller
import time
import sys
from argparse import ArgumentParser


def parse():
    parser = ArgumentParser()
    parser.add_argument("-pb", "--pokeball", dest='pokeball', action='store_true')
    parser.add_argument("-gb", "--greatball", dest='greatball', action='store_true')

    args = parser.parse_args()
    return args


def mouse_click():
    mouse = Controller()
    mouse.press(Button.left)
    mouse.release(Button.left)


def text_print(text, wait_len, frequency):
    if frequency is not None:
        for e in range(frequency):
            keyboard.write(text)
            keyboard.press_and_release("Space")
            keyboard.press_and_release("Enter")
            if wait_len is not None:
                time.sleep(wait_len)
    else:
        while True:
            mouse_click()
            keyboard.write(text)
            keyboard.press_and_release("Space")
            keyboard.press_and_release("Enter")
            if wait_len is not None:
                time.sleep(wait_len)

def pokeball():
    keyboard.write(';p')
    keyboard.press_and_release("Enter")
    time.sleep(1.5)
    keyboard.write('pb')
    keyboard.press_and_release("Enter")
    time.sleep(10)
    pokeball()

def greatball():
    keyboard.write(';p')
    keyboard.press_and_release("Enter")
    time.sleep(1.5)
    keyboard.write('gb')
    keyboard.press_and_release("Enter")
    time.sleep(10)
    pokeball()

def main():
    args = parse()
    mouse_click()
    if args.pokeball == True:
        pokeball()
    if args.greatball == True:
        greatball()




if __name__ == "__main__":
    main()
