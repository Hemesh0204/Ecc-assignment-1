import re
import sys

ip_pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+).*?\d{4}:(?P<time>\d{2}):\d{2},*?')

for input_line in sys.stdin:
    found_match = ip_pattern.search(input_line)
    if found_match:
        output = f"[{found_match.group('time')}:00]{found_match.group('ip')}\t1"
        print(output)
