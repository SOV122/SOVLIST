#!/usr/bin/env python3

import string
import random
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

def generate_meaningful_passwords(base_words, min_length, max_length, include_numbers, include_special_chars, num_passwords):
    characters = ''
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    passwords = set()

    while len(passwords) < num_passwords:
        base_word = random.choice(base_words)
        base_word_length = len(base_word)

        for length in range(min_length, max_length + 1):
            if length <= base_word_length:
                password = base_word[:length]
            else:
                additional_length = length - base_word_length
                additional_chars = ''.join(random.choice(characters) for _ in range(additional_length))
                split_point = random.randint(0, base_word_length)
                password = base_word[:split_point] + additional_chars + base_word[split_point:]
                
                if len(password) > length:
                    password = password[:length]

            passwords.add(password)

            if len(passwords) >= num_passwords:
                break
        if len(passwords) >= num_passwords:
            break

    return passwords

def save_passwords(passwords, filename):
    with open(filename, 'w') as file:
        for password in sorted(passwords):
            file.write(password + '\n')

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    os.system('clear')
    print(BANNER)
    
    base_words = input("Enter base words separated by spaces: ").split()
    include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'
    min_length = int(input("Enter minimum length of passwords: ").strip())
    max_length = int(input("Enter maximum length of passwords: ").strip())
    num_passwords = int(input("Enter number of passwords to generate: ").strip())

    if min_length > max_length:
        print("Error: Minimum length cannot be greater than maximum length.")
        return

    passwords = generate_meaningful_passwords(base_words, min_length, max_length, include_numbers, include_special_chars, num_passwords)
    
    output_filename = input("Enter the name for the output file (e.g., wordlist.txt): ").strip()
    output_file = os.path.join(script_dir, output_filename)

    save_passwords(passwords, output_file)

    print(f"Wordlist saved to '{output_file}' with {len(passwords)} entries.")

if __name__ == "__main__":
    main()
