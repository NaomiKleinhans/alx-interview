#!/usr/bin/python3
"""
Function to validate UTF-8 encoding
"""


def validUTF8(data):
    num_bytes = 0

    # Masks for checking the format of UTF-8 bytes
    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        # Check if it's a starting byte
        if num_bytes == 0:
            # Determine the number of bytes in the sequence
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # 1 byte (ASCII) or invalid
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if the byte is a valid continuation byte
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
