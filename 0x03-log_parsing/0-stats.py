#!/usr/bin/python3

import sys

# Initialize variables
total_size = 0
status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for idx, line in enumerate(sys.stdin, start=1):
        # Parse the line
        parts = line.split()
        if len(parts) < 7:
            continue
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        # Update total file size
        total_size += file_size

        # Update status code count
        if status_code in status_code_count:
            status_code_count[status_code] += 1

        # Check if 10 lines have been processed
        if idx % 10 == 0:
            print(f"Total file size: {total_size}")
            for code in sorted(status_code_count.keys()):
                if status_code_count[code] > 0:
                    print(f"{code}: {status_code_count[code]}")
except KeyboardInterrupt:
    print(f"Total file size: {total_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")
