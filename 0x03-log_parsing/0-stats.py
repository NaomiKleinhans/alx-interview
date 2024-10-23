#!/usr/bin/python3
import sys

# Initialize variables
total_size = 0
status_counts = {'200': 0, '301': 0, '400': 0,
                 '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
line_count = 0


def print_stats():
    """Print the current statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


try:
    for line in sys.stdin:
        line_count += 1
        try:
            # Strip and split the line to extract parts
            parts = line.split()

            # Check if the line contains the expected number of parts
            if len(parts) < 7:
                continue

            # Extract the status code and file size from the log
            status_code = parts[-2]
            file_size = parts[-1]

            # Ensure file size is a valid number
            total_size += int(file_size)

            # Ensure status code is valid and update its count
            if status_code in status_counts:
                status_counts[status_code] += 1

        except (IndexError, ValueError):
            # Skip lines with invalid formatting or data
            continue

        # Print stats after every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Print stats before exiting on keyboard interruption
    print_stats()
    raise

# Ensure to print final stats after all input is processed
print_stats()
