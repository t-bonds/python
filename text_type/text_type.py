import keyboard as keyboard
from pynput.mouse import Button, Controller
import time
import sys
from argparse import ArgumentParser


def parse():
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest='filename', help="Name of text file to parse. Defaults to printing one word at a time.")
    parser.add_argument("-a", "--all", dest="full_file", action="store_true", default=False, help="When given, will print entire text file at once.")
    parser.add_argument("-t", "--text", dest='text', help="String to print. Will print entire string.")
    parser.add_argument("-w", "--wait", dest='wait_len', help="Wait time in seconds between writes.")
    parser.add_argument("-l", "--length", dest='length', help="Number of prints before exiting.")
    args = parser.parse_args()
    return args


def mouse_click():
    mouse = Controller()
    mouse.press(Button.left)
    mouse.release(Button.left)


def file_and_text_print(file_name, text, wait_len, frequency, full_file):

    if frequency is not None:
        count = 0
        with open(file_name, "r", encoding='utf-8', errors='ignore') as f:
            file = f.read()
            if not full_file:
                file = file.split()
            if full_file:
                while True:
                    keyboard.write(text + ' ' + file)
                    keyboard.press_and_release("Space")
                    keyboard.press_and_release("Enter")
                    if frequency is not None:
                        count += 1
                        if count == frequency:
                            sys.exit()
                    if wait_len is not None:
                        time.sleep(wait_len)
            else:
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
            if not full_file:
                file = file.split()
            if full_file:
                keyboard.write(text + ' ' + file)
                keyboard.press_and_release("Space")
                keyboard.press_and_release("Enter")
                if wait_len is not None:
                    time.sleep(wait_len)
            else:
                for e in text:
                    keyboard.write(text + ' ' + e)
                    keyboard.press_and_release("Space")
                    keyboard.press_and_release("Enter")
                    if wait_len is not None:
                        time.sleep(wait_len)


def file_print(file_name, wait_len, frequency, full_file):
    count = 0
    with open(file_name, "r", encoding='utf-8', errors='ignore') as f:
        file = f.read()
        if not full_file:
            file = file.split()
        if full_file:
            if frequency is not None:
                while True:
                    keyboard.write(file)
                    keyboard.press_and_release("Space")
                    keyboard.press_and_release("Enter")
                    count += 1
                    if count == frequency:
                        sys.exit()
                if wait_len is not None:
                    time.sleep(wait_len)
            else:
                keyboard.write(file)
                keyboard.press_and_release("Space")
                keyboard.press_and_release("Enter")
        else:
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
            mouse_click()
            keyboard.write(text)
            keyboard.press_and_release("Space")
            keyboard.press_and_release("Enter")
            if wait_len is not None:
                time.sleep(wait_len)


def main():
    args = parse()
    file_name = args.filename
    text = args.text
    full_file = args.full_file
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
        file_and_text_print(file_name, text, wait_len, frequency, full_file)
    elif file_name is not None:
        file_print(file_name, wait_len, frequency, full_file)
    elif text is not None:
        text_print(text, wait_len, frequency)


if __name__ == "__main__":
    main()
