#!/usr/bin/env python3

# auto_prompt.py
#
# Wednesday December 27, 2023
# Waheed Brown
#
# This Python script builds prompts for generative AI applications. The goal is to make
# prompt engineering easier, by using autocomplete when typing prompts. The autocomplete
# training text can be defined by the user
#
# References:
# https://pypi.org/project/autocomplete/
# https://docs.python.org/3/howto/curses.html

import autocomplete
import curses

class AutoPrompt:
    stdscr = 0
    predictions = {}

    def __init__(self, stdscr):
        self.stdscr = stdscr

    def get_predictions(self, current_row):
        while True:
            self._display_predictions(current_row)
            key = self.stdscr.getch()

            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(["Option 1", "Option 2", "Option 3", "Option 4"]) - 1:
                current_row += 1
            elif key == 10:  # Enter key pressed
                break  # Exit the loop

    def _display_predictions(self, current_row):
        h, w = self.stdscr.getmaxyx()

        menu_items = ["Option 1", "Option 2", "Option 3", "Option 4"]
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        selected_text = curses.color_pair(1)
        
        self.stdscr.clear()

        for i, item in enumerate(menu_items):
            x = w//2 - len(item)//2
            y = h//2 - len(menu_items)//2 + i
            if i == current_row:
                self.stdscr.attron(selected_text)
                self.stdscr.addstr(y, x, item)
                self.stdscr.attroff(selected_text)
            else:
                self.stdscr.addstr(y, x, item)

        self.stdscr.refresh()

        # This raises ZeroDivisionError when i == 10.
        # for i in range(0, 11):
        #     v = i-10
        #     self.stdscr.addstr(i, 0, '10 plus {} is {}'.format(v, 10+v))

        # self.stdscr.refresh()
        # self.stdscr.getkey()

def main(stdscr):
    # Train the model
    autocomplete.load()

    # Initialize UI
    curses.curs_set(0)  # Hide the cursor
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    stdscr.keypad(1)  # Enable special keys (e.g., arrows)

    # Start auto prompt
    auto_prompt = AutoPrompt(stdscr)
    current_row = 0
    auto_prompt.get_predictions(current_row)


    # console_input = "pass"
    # while(console_input != 'exit'):
    #     console_input = input().lower()
    #     output = autocomplete.predict('the', console_input)
    #     print(f'{output}')

curses.wrapper(main)