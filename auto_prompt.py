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

import argparse
import bisect
import curses

class AutoPrompt:
    console_input = ''
    stdscr = 0
    corpus = []
    suggestions = []

    def __init__(self, stdscr):
        self.stdscr = stdscr

    def get_suggestions(self, current_row):
        while True:
            self._display_suggestions(current_row)
            key = self.stdscr.getch()

            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(self.suggestions) - 1:
                current_row += 1
            elif key == curses.KEY_DC or key == 8 or key == 127:
                self.console_input = self.console_input[:-1]
            elif key == 10:  # Enter key pressed
                break  # Exit the loop
            # TODO: Add support for all ASCII characters that a user could type in a gen AI prompt
            elif (key >= 65 and key <= 122) or (key >= 48 and key <= 57): # [a-z][A-Z][0-9]
                self.console_input += chr(key)
                self._complete()

    def _display_suggestions(self, current_row):
        h, w = self.stdscr.getmaxyx()
        menu_items = self.suggestions
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        selected_text = curses.color_pair(1)
        
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, self.console_input)

        for i, item in enumerate(menu_items):
            x = w//2 - len(item[0])//2
            y = h//2 - len(menu_items)//2 + i
            if i == current_row:
                self.stdscr.attron(selected_text)
                self.stdscr.addstr(y, x, item)
                self.stdscr.attroff(selected_text)
            else:
                self.stdscr.addstr(y, x, item)

        self.stdscr.refresh()

    def _complete(self):
        if self.console_input.lower():  # cache matches (entries that start with entered text)
            self.suggestions = [s for s in self.corpus 
                                if s and s.lower().startswith(self.console_input)]
        else:  # no text entered, all matches possible
            self.suggestions = self.corpus[:]

        # return match indexed by state
        try: 
            return self.suggestions
        except IndexError:
            return None

def main(stdscr):
    # Initialize UI
    curses.curs_set(0)  # Hide the cursor
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    stdscr.keypad(1)  # Enable special keys (e.g., arrows)

    auto_prompt = AutoPrompt(stdscr)

    with open(args.training_file, 'r') as training_file:
        for line in training_file:
            bisect.insort(auto_prompt.corpus, line.rstrip())
    
    auto_prompt.get_suggestions(current_row=0)

# Parse command line arguments
parser = argparse.ArgumentParser(description="auto_prompt.py command line arguments")
parser.add_argument('-t', '--training-file', type=str, required=True, help='path/to/training.txt file')
args = parser.parse_args()

curses.wrapper(main)