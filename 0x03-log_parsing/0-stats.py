#!/usr/bin/python3
"""
Log parsing
"""

import sys
import re


def print_stats(stats: dict, file_size: int) -> None:
    """Prints the current statistics."""
    print("File size: {}".format(file_size))
    for k in sorted(stats.keys()):
        if stats[k] > 0:
            print("{}: {}".format(k, stats[k]))


if __name__ == "__main__":
    regex = re.compile(
        r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'
    )

    count = 0
    file_size = 0
    stats = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.match(line)
            if match:
                count += 1
                status_code = match.group(3)
                size = int(match.group(4))

                # Update file size
                file_size += size

                # Update status code counts
                if status_code in stats:
                    stats[status_code] += 1

                # Print stats every 10 lines
                if count % 10 == 0:
                    print_stats(stats, file_size)

    except KeyboardInterrupt:
        print_stats(stats, file_size)
        raise
    finally:
        print_stats(stats, file_size)
