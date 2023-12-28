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
    console_input = 'bo' # TODO: Initialize to null
    stdscr = 0
    predictions = {}

    def __init__(self, stdscr):
        self.stdscr = stdscr

    def get_predictions(self, current_row):
        self.predictions = autocomplete.predict('the', self.console_input)

        while True:
            self._display_predictions(current_row)
            key = self.stdscr.getch()

            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(self.predictions) - 1:
                current_row += 1
            elif key == curses.KEY_UP or key == curses.KEY_DOWN or key == curses.KEY_LEFT or key == curses.KEY_RIGHT:
                pass
            elif key == curses.KEY_DC or key == 8 or key == 127:
                self.console_input = self.console_input[:-1]
            elif key == 10:  # Enter key pressed
                break  # Exit the loop
            else:
                self.console_input += chr(key)
                self.predictions = autocomplete.predict('the', self.console_input)

    def _display_predictions(self, current_row):
        h, w = self.stdscr.getmaxyx()
        menu_items = self.predictions
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        selected_text = curses.color_pair(1)
        
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, self.console_input)

        for i, item in enumerate(menu_items):
            x = w//2 - len(item[0])//2
            y = h//2 - len(menu_items)//2 + i
            if i == current_row:
                self.stdscr.attron(selected_text)
                self.stdscr.addstr(y, x, item[0])
                self.stdscr.attroff(selected_text)
            else:
                self.stdscr.addstr(y, x, item[0])

        self.stdscr.refresh()

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

curses.wrapper(main)