#!/usr/bin/env python3

# auto-prompt.py
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

import autocomplete

def main():
    autocomplete.load()

    console_input = "pass"
    while(console_input != 'exit'):
        console_input = input().lower()
        output = autocomplete.predict('the', console_input)
        print(f'{output}')

if __name__ == "__main__":
    main()