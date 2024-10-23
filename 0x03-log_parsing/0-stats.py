#!/usr/bin/python3
import sys

# Initialize variables
total_size = 0
status_counts = {}
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
line_count = 0


def print_stats():
    """Print accumulated metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


try:
    for line in sys.stdin:
        line_count += 1
        try:
            # Split the line by spaces and extract relevant parts
            parts = line.split()
            if len(parts) < 7:
                continue

            # Extract status code and file size
            status_code = parts[-2]
            file_size = parts[-1]

            # Update file size if it's a number
            total_size += int(file_size)

            # Update status code count if it's valid
            if status_code in valid_codes:
                if status_code not in status_counts:
                    status_counts[status_code] = 0
                status_counts[status_code] += 1

        except (IndexError, ValueError):
            # Skip lines with invalid formatting or data
            continue

        # Print stats after every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print_stats()
    raise

# Ensure to print the final stats when the input ends
print_stats()
