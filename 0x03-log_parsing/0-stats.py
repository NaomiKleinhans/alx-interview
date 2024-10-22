#!/usr/bin/python3
"""
Log parsing
"""

import sys
import re


def print_stats(stats: dict, file_size: int) -> None:
    """
    Helper function to print statistics.
    """
    print("File size: {}".format(file_size))
    for code in sorted(stats):
        if stats[code] > 0:
            print("{}: {}".format(code, stats[code]))


if __name__ == '__main__':
    # Regex to match the log format
    regex = re.compile(
        r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET (.*?) HTTP/1.1" (\d{3}) (\d+)'
    )

    line_count = 0
    total_file_size = 0
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {code: 0 for code in status_codes}

    try:
        for line in sys.stdin:
            line_count += 1
            line = line.strip()  # Remove leading/trailing whitespace
            match = regex.fullmatch(line)

            if match:
                status_code = match.group(4)  # Get the status code
                file_size = int(match.group(5))  # Get the file size

                # Update total file size
                total_file_size += file_size

                # Update status code frequency
                if status_code in stats:
                    stats[status_code] += 1

                # Print stats every 10 lines
                if line_count % 10 == 0:
                    print_stats(stats, total_file_size)

    except KeyboardInterrupt:
        print_stats(stats, total_file_size)
        raise
    finally:
        print_stats(stats, total_file_size)
