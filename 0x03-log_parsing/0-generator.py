#!/usr/bin/python3
"""
A script that generates random HTTP request logs.
"""

import random
import sys
import datetime
from time import sleep

if __name__ == '__main__':
    for i in range(10000):
        sleep(random.random())
        sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET {} {}\" {} {}\n".format(
            random.randint(1, 255),  # Random IP octet 1
            random.randint(1, 255),  # Random IP octet 2
            random.randint(1, 255),  # Random IP octet 3
            random.randint(1, 255),  # Random IP octet 4
            datetime.datetime.now(),  # Current timestamp
            '/projects/1216',  # URL path
            'HTTP/1.1',  # HTTP version
            # Status code
            random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
            random.randint(1, 1024)  # File size
        ))
        sys.stdout.flush()
