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
try:
    import gnureadline as readline
except ImportError:
    import readline

class AutoPrompt:
    console_input = ''
    final_prompt = ''
    prompt_y = 0
    stdscr = 0
    corpus = []
    suggestions = []

    def __init__(self, stdscr):
        self.stdscr = stdscr

    def get_suggestions(self, current_row):
        self.stdscr.addstr(0, 0, '[Start typing a generative AI prompt, press ESC to quit]')

        while True:
            key = self.stdscr.getch()

            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(self.suggestions) - 1:
                current_row += 1
            elif key == curses.KEY_DC or key == 8 or key == 127:
                self.console_input = self.console_input[:-1]
            elif key == 9: # Tab key pressed
                self.console_input = self.suggestions[current_row]
            elif key == 27: # ESC key pressed
                break
            elif key == 10 or key == 13: # Enter key pressed
                if len(self.console_input) == 0:
                    continue
                self.final_prompt += f'{self.console_input}\n'
                self.console_input = ''
                self.suggestions.clear()
                self.prompt_y += 1
            elif key >= 32 and key <= 126:
                # ASCII codes for US English keyboard inputs
                self.console_input += chr(key)
                self._complete()

            self._display_suggestions(current_row)

    def _display_suggestions(self, current_row):
        h, w = self.stdscr.getmaxyx()
        menu_items = self.suggestions
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        selected_text = curses.color_pair(1)
        
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, self.final_prompt)
        self.stdscr.addstr(self.prompt_y, 0, self.console_input)

        for i, item in enumerate(menu_items):
            x = 0
            y = self.prompt_y + 1 + i

            try:
                if i == current_row:
                    self.stdscr.attron(selected_text)
                    self.stdscr.addstr(y, x, item)
                    self.stdscr.attroff(selected_text)
                else:
                    self.stdscr.addstr(y, x, item)
            except curses.error:
                # Handle cases where the text in an autocomplete menu item
                # wraps around the curses screen buffer
                pass

        self.stdscr.refresh()

    def _complete(self):
        if self.console_input:  # cache matches (entries that start with entered text)
            self.suggestions = [s for s in self.corpus 
                                if s and s.lower().startswith(self.console_input.lower())]
        else:  # no text entered, all matches possible
            self.suggestions = self.corpus[:]

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