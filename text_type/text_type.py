import keyboard as keyboard
from pynput.mouse import Button, Controller
import time
import sys
from argparse import ArgumentParser


def parse():
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest='filename')
    parser.add_argument("-t", "--text", dest='text')
    parser.add_argument("-w", "--wait", dest='wait_len')
    parser.add_argument("-l", "--length", dest='length')
    args = parser.parse_args()
    return args


def mouse_click():
    mouse = Controller()
    mouse.press(Button.left)
    mouse.release(Button.left)


def file_and_text_print(file_name, text, wait_len, frequency):

    if frequency is not None:
        count = 0
        with open(file_name, "r", encoding='utf-8', errors='ignore') as f:
            file = f.read()
            file = file.split()
        for e in file:
            keyboard.write(text + ' ' + e)
            keyboard.press_and_release("Space")
            keyboard.press_and_release("Enter")
            if frequency is not None:
                count += 1
                if count == frequency:
                    break
            if wait_len is not None:
                time.sleep(wait_len)

    else:
        with open(file_name, "r", encoding='utf-8', errors='ignore') as f:
            file = f.read()
            file = file.split()
        for e in file:
            keyboard.write(text + ' ' + e)
            keyboard.press_and_release("Space")
            keyboard.press_and_release("Enter")
            if wait_len is not None:
                time.sleep(wait_len)


def file_print(file_name, wait_len, frequency):
    count = 0
    with open(file_name, "r", encoding='utf-8', errors='ignore') as f:
        text = f.read()
        text = text.split()
    for e in text:
        keyboard.write(e)
        keyboard.press_and_release("Space")
        keyboard.press_and_release("Enter")
        if frequency is not None:
            count += 1
            if count == frequency:
                sys.exit()
        if wait_len is not None:
            time.sleep(wait_len)


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
            keyboard.write(text)
            keyboard.press_and_release("Space")
            keyboard.press_and_release("Enter")
            if wait_len is not None:
                time.sleep(wait_len)


def main():
    args = parse()
    file_name = args.filename
    text = args.text
    if args.wait_len is not None:
        wait_len = float(args.wait_len)
    else:
        wait_len = args.wait_len
    if args.length is not None:
        frequency = int(args.length)
    else:
        frequency = args.length
    mouse_click()

    if file_name is not None and text is not None:
        file_and_text_print(file_name, text, wait_len, frequency)
    elif file_name is not None:
        file_print(file_name, wait_len, frequency)
    elif text is not None:
        text_print(text, wait_len, frequency)


if __name__ == "__main__":
    main()
