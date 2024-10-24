#!/usr/bin/python3
import sys
import signal

# Initialize global variables
total_size = 0
status_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0


def print_stats():
    """Prints the accumulated statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def process_line(line):
    """Processes a single line and updates the global variables."""
    global total_size, status_counts, line_count
    try:
        parts = line.split()
        if len(parts) < 9:
            return

        file_size = int(parts[-1])
        status_code = parts[-2]

        # Update total size
        total_size += file_size

        # Update status code count if it's a valid code
        if status_code in status_counts:
            status_counts[status_code] += 1

        # Increment line counter
        line_count += 1

    except Exception:
        # Skip lines that don't match the format or cause errors
        pass


def signal_handler(sig, frame):
    """Handles keyboard interruption to print statistics."""
    print_stats()
    sys.exit(0)


# Setup signal handler for CTRL + C (SIGINT)
signal.signal(signal.SIGINT, signal_handler)

# Main loop to read stdin line by line
try:
    for line in sys.stdin:
        process_line(line)
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    # On CTRL + C, print the final stats before exiting
    print_stats()
    sys.exit(0)

# After reading all lines, print the final statistics
print_stats()
