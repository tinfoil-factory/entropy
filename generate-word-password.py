#!/usr/bin/python3

import secrets
import re
import sys
import math

wordlist_filename = 'agwordlist.txt'
expected_wordlist_length = 18325

def parse_input():
    if len(sys.argv) != 2:
        raise ValueError(f"Expected one argument, got {len(sys.argv)}")

    try:
         return int(sys.argv[1])
    except ValueError:
        raise ValueError(f"Expected an integer argument, got '{sys.argv[1]}'")

def load_wordlist():
    with open(wordlist_filename) as f:
        lines = f.read().splitlines()
        
    for line in lines:
        if not re.search(r'[a-z]+', line):
            raise ValueError(f"Unexpected character in word {line}")

    if len(lines) != expected_wordlist_length or len(set(lines)) != expected_wordlist_length:
        raise ValueError("Unexpected number of words in wordlist")

    return lines

try:
    password_length = parse_input()
    alphabet = load_wordlist()

    bits_of_entropy = math.log2(len(alphabet) ** password_length)
    print('entropy: %2.f bits' % bits_of_entropy, file=sys.stderr)

    print(' '.join(secrets.choice(alphabet) for i in range(password_length)))
    exit(0)
except Exception as e:
    print(e, file=sys.stderr)
    print("Usage: ./generate-word-password.py <password length>", file=sys.stderr)
    exit(1)