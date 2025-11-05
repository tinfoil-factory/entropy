#!/usr/bin/python3

import base64
import hashlib
import hmac
import sys
import time

def parse_input():
    if len(sys.argv) != 2:
        raise ValueError(f"Expected one argument, got {len(sys.argv)}")

    return sys.argv[1]

def compute_totp(secret: str):
    # https://datatracker.ietf.org/doc/html/rfc4226

    encoded_secret = base64.b32decode(secret)
    encoded_time = int(time.time() / 30).to_bytes(8, byteorder='big')

    hmac_result = hmac.new(encoded_secret, encoded_time, hashlib.sha1).digest()

    offset = hmac_result[19] & 0xf
    bin_code = ((hmac_result[offset] & 0x7f) << 24
            | (hmac_result[offset + 1] & 0xff) << 16
            | (hmac_result[offset + 2] & 0xff) << 8
            | (hmac_result[offset + 3] & 0xff))

    return '{:06d}'.format(bin_code % 1_000_000)

input_secret = parse_input()
print(compute_totp(input_secret))
