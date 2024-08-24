#!/usr/bin/env python3

import itertools
import string
import os

BANNER = """
███████╗ ██████╗ ██╗   ██╗██╗     ██╗███████╗████████╗
██╔════╝██╔═══██╗██║   ██║██║     ██║██╔════╝╚══██╔══╝
███████╗██║   ██║██║   ██║██║     ██║███████╗   ██║   
╚════██║██║   ██║╚██╗ ██╔╝██║     ██║╚════██║   ██║   
███████║╚██████╔╝ ╚████╔╝ ███████╗██║███████║   ██║   
╚══════╝ ╚═════╝   ╚═══╝  ╚══════╝╚═╝╚══════╝   ╚═╝   

Made by SOV
"""

def generate_wordlist(base_words, numbers=True, special_chars=True, length=8, count=1000000):
    characters = string.ascii_lowercase
    if numbers:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    wordlist = set(base_words)
    all_combinations = itertools.product(characters, repeat=length)
    
    for combination in all_combinations:
        if len(wordlist) >= count:
            break
        wordlist.add(''.join(combination))

    return wordlist

def save_wordlist(wordlist, filename):
    with open(filename, 'w') as file:
        for word in sorted(wordlist):
            file.write(word + '\n')

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(script_dir, 'wordlist.txt')

    os.system('clear')
    print(BANNER)
    
    base_words = input("Enter base words separated by spaces: ").split()
    include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'
    length = int(input("Enter exact length of passwords: ").strip())
    count = int(input("Enter number of passwords to generate: ").strip())

    wordlist = generate_wordlist(base_words, numbers=include_numbers, special_chars=include_special_chars, length=length, count=count)
    save_wordlist(wordlist, output_file)

    print(f"Wordlist saved to '{output_file}' with {len(wordlist)} entries.")

if __name__ == "__main__":
    main()
