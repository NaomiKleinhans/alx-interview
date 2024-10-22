#!/usr/bin/python3
import sys
import signal

# Dictionary to store counts of each status code
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

# Variable to keep track of total file size
total_file_size = 0
line_count = 0

# Function to print the current statistics


def print_stats():
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

# Signal handler to catch keyboard interrupts (CTRL + C)


def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    # Read input line by line
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        try:
            # Ensure the line format is valid
            if len(parts) < 7:
                continue

            # Extract the file size
            file_size = int(parts[-1])
            total_file_size += file_size

            # Extract the status code
            status_code = parts[-2]
            if status_code in status_codes:
                status_codes[status_code] += 1

        except (ValueError, IndexError):
            # Skip the line if it's malformed
            continue

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Handle interruption (CTRL + C)
    print_stats()
    sys.exit(0)
