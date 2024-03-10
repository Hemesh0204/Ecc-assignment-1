import re
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--time_range', type=str)
args = parser.parse_args()

start_time, end_time = map(int, args.time_range.split('-'))

print(start_time, end_time)

pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2},*?')
for input_line in sys.stdin:
    search_result = pattern.search(input_line)
    if search_result:
        hour = int(search_result.group('hour'))
        if start_time <= hour <= end_time:
            print(search_result.group('ip'), 1)
