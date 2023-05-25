# from cgitb import text
from curses import wrapper
import curses
import re
import random
import sys
from hangman_pic import print_hang
import string

screen = curses.initscr()
curses.curs_set(0)
curses.echo()

menu = ["Play", "Instructions", "Credits", "exit"]
exit_selection = ["YES", "NO"]
message = "Are you sure you want to exit"



def start(stdscr):    
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    current_index = 0
    exit_index = 0
    main_menu(stdscr, current_index)
    while True:
        key = stdscr.getch()
        stdscr.clear()
        main_menu(stdscr, current_index)
        if key == curses.KEY_UP and current_index > 0:
            current_index -= 1
        elif key == curses.KEY_DOWN and current_index < 3:
            current_index += 1
        elif key == curses.KEY_ENTER or key in [10, 13] and current_index == 1:
            instructions(stdscr)
        elif key == curses.KEY_ENTER or key in [10, 13] and current_index == 2:
            credits(stdscr)
        elif key == curses.KEY_ENTER or key in [10, 13] and current_index == 0:
            play_game(stdscr)
        elif (
            key == curses.KEY_ENTER
            or key in [10, 13]
            and current_index == len(menu) - 1
        ):
            if ex_menu(stdscr, exit_index):
                break
            else:
                pass
        main_menu(stdscr, current_index)
        stdscr.refresh()


def main_menu(stdscr, current_row):
    stdscr.clear()
    for index, row in enumerate(menu):
        height, width = stdscr.getmaxyx()
        x = width // 2 - len(row) // 2
        y = height // 2 - len(menu) // 2 + index
        if index == current_row:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()


def print_ex_menu(stdscr, current_row):
    stdscr.clear()
    print_center(stdscr, "Are you sure you want to exit")
    for index, row in enumerate(exit_selection):
        height, width = stdscr.getmaxyx()
        x = width // 2 - len(exit_selection) // 2 + (index * 5)
        y = height // 2 - len(row) // 2 + 2
        if index == current_row:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
        stdscr.refresh()


def ex_menu(stdscr, exit_index):
    print_ex_menu(stdscr, exit_index)
    while True:
        key = stdscr.getch()
        if key == curses.KEY_LEFT and exit_index > 0:
            exit_index -= 1
        elif key == curses.KEY_RIGHT and exit_index < 1:
            exit_index += 1
        elif key == curses.KEY_ENTER or key in [10, 13] and exit_index == 1:
            return False
        elif key == curses.KEY_ENTER or key in [10, 13] and exit_index == 0:
            return True
        print_ex_menu(stdscr, exit_index)


def instructions(stdscr):
    text = [
        "Hangman is a paper-and-pencil guessing game",
        "played by two or more people.",
        "One player thinks of a word,",
        "and the other players have to try and guess it.",
        "They do so by calling letters ",
        "that they think are in the word.",
        "The word is shown as a row of dashes.",
    ]
    stdscr.clear()
    for i in range(len(text)):
        h, w = stdscr.getmaxyx()
        x = w // 2 - len(text[i]) // 2
        y = h // 2 - len(text) // 2
        stdscr.addstr(y + i * 2, x, text[i])
        stdscr.refresh()
    stdscr.getch()
    return


def credits(stdscr):
    text = [
        "Created from Charalampos Alexiadis",
        "for my final project",
        "on ",
        "CS50’s Introduction to Programming with Python!",
    ]
    stdscr.clear()
    for i in range(len(text)):
        h, w = stdscr.getmaxyx()
        x = w // 2 - len(text[i]) // 2
        y = h // 2 - len(text) // 2
        stdscr.addstr(y + i * 2, x, text[i])
        stdscr.refresh()
    stdscr.getch()
    return


def play_game(stdscr):
    alphabet = list(string.ascii_lowercase)
    pointer = 0
    hidden_word = random_word()
    stdscr.clear()
    quess_list = []
    tries = 1
    quess_word = list("_" * len(hidden_word))
    for i in range(len(hidden_word)):
        h, w = stdscr.getmaxyx()
        y = h // 2 - len(hidden_word)
        x = w // 2 - len(hidden_word) * 2
        stdscr.addstr(y + 4, x + 11 + i * 2, "_ ")
    print_hang(stdscr, tries, hidden_word)
    stdscr.refresh()
    while tries != 9:
        print_hang(stdscr, tries, hidden_word)
        if tries == 8:
            print_hang(stdscr, tries, hidden_word)
            break
        quess = stdscr.getkey()
        if quess not in alphabet:
            stdscr.addstr(y + 8, x, "Enter a letter     ")
            stdscr.refresh()
            continue
        stdscr.addstr(y + 8, x, f"You pressed:   {quess}")
        if quess in quess_list:
            stdscr.addstr(y + 8, x, f"Already typed: {quess}")
            stdscr.refresh()
            continue
        elif quess not in hidden_word and tries != 8:
            pointer += 1
            quess_list += quess
            stdscr.addstr(y + 6, x + 8 + pointer * 2, quess)
            tries += 1
            stdscr.refresh()
            continue
        else:
            pointer += 1
            for index, letter in enumerate(hidden_word):
                if quess == letter:
                    quess_word[index] = quess
                    h, w = stdscr.getmaxyx()
                    y = h // 2 - len(hidden_word)
                    x = w // 2 - len(hidden_word) * 2
                    stdscr.addstr(y + 3, x + 11 + index * 2, quess)
                    stdscr.refresh()
                    try:
                        word = "".join(quess_word)
                        if word == hidden_word:
                            tries = 9
                            print_hang(stdscr, tries, hidden_word)
                    except TypeError:
                        pass
                elif quess != letter:
                    continue
                quess_list += quess
                stdscr.addstr(y + 6, x + 10 + pointer * 2, quess)


def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w // 2 - len(text) // 2
    y = h // 2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def random_word():
    x = []
    new = []

    # Open file and save in lines
    try:
        with open("sample_text.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File doesn't exist")

    # Split and save in empty list
    for line in lines:
        line = re.sub(r"([!\"#$%&()*+,-./:;<=>?@\[\\\]^_`{|}~])\n?", "", line)
        x.extend(line.split(" "))

    # Clean the output
    for index, word in enumerate(x):
        if len(word) > 5 and not word[0].isupper() and word not in new:
            new.append(word)

        # Select a random word and create and empty list
    return new[random.randint(0, len(new) - 1)]


def add():
    return 3


def main():
    curses.wrapper(start)


if __name__ == "__main__":
    main()  
