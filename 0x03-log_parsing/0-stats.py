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
            # Split line by spaces to extract the necessary parts
            parts = line.split()

            # Validate that the line has the correct number of parts
            if len(parts) < 7:
                continue

            # Extract the status code and file size from the line
            status_code = parts[-2]
            file_size = parts[-1]

            # Add to total file size (ensure file size is a valid integer)
            total_size += int(file_size)

            # Update the count for the valid status code
            if status_code in status_counts:
                status_counts[status_code] += 1

        except (ValueError, IndexError):
            # Skip the line if there's an issue parsing it (e.g., invalid file size)
            continue

        # Print stats after every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Print stats before exiting when interrupted (CTRL + C)
    print_stats()
    raise

# Ensure to print final stats when input ends
print_stats()
