#!/usr/bin/python3

import secrets
import string
import sys
import math

def parse_input():
    if len(sys.argv) != 2:
        raise ValueError(f"Expected one argument, got {len(sys.argv)}")

    try:
         return int(sys.argv[1])
    except ValueError:
        raise ValueError(f"Expected an integer argument, got '{sys.argv[1]}'")

try:
    password_length = parse_input()
    alphabet = string.ascii_letters

    bits_of_entropy = math.log2(len(alphabet) ** password_length)
    print('entropy: %2.f bits' % bits_of_entropy, file=sys.stderr)

    print(''.join(secrets.choice(alphabet) for i in range(password_length)))
    exit(0)
except Exception as e:
    print(e, file=sys.stderr)
    print("Usage: ./generate-letter-password.py <password length>", file=sys.stderr)
    exit(1)