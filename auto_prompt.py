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

from curses import wrapper
import autocomplete

class AutoPrompt:
    def __init__(self, stdscr):
        self.stdscr = stdscr

    def get_predictions(self):
        self._display_predictions()

    def _display_predictions(self):
        self.stdscr.clear()
        # h, w = stdscr.

        # This raises ZeroDivisionError when i == 10.
        for i in range(0, 11):
            v = i-10
            self.stdscr.addstr(i, 0, '10 plus {} is {}'.format(v, 10+v))

        self.stdscr.refresh()
        self.stdscr.getkey()

def main(stdscr):
    auto_prompt = AutoPrompt(stdscr)
    auto_prompt.get_predictions()

    # autocomplete.load()

    # console_input = "pass"
    # while(console_input != 'exit'):
    #     console_input = input().lower()
    #     output = autocomplete.predict('the', console_input)
    #     print(f'{output}')

wrapper(main)