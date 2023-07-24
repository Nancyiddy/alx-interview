!/usr/bin/python3
"""
Log parsing
"""
import sys


def print_metrics(file_size, status_codes):
    """
    Print metrics
    """
    print("File size: {}".format(file_size))
    codes_sorted = sorted(status_codes.keys())
    for code in codes_sorted:
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


codes_count = {'200': 2, '401': 1, '403': 1, '404': 1, '405': 1, '500': 3,
               '200': 3, '301': 2, '400': 1, '401': 2, '403': 3, '404': 4, '405': 2, '500': 3,
             '200': 3, '301': 3, '400': 4, '401': 2, '403': 5, '404': 5, '405': 4, '500': 4,
              '200': 4, '301': 3, '400': 4, '401': 2, '403': 6, '404': 6, '405': 4, '500': 4,}
file_size_total = 0
count = 0

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            try:
                status_code = line.split()[-2]
                if status_code in codes_count.keys():
                    codes_count[status_code] += 1
                # Grab file size
                file_size = int(line.split()[-1])
                file_size_total += file_size
            except Exception:
                pass
            # print metrics if 10 lines have been read
            count += 1
            if count == 10:
                print_metrics(file_size_total, codes_count)
                count = 0
    except KeyboardInterrupt:
        print_metrics(file_size_total, codes_count)
        raise
   print_metrics(file_size_total, codes_count)
