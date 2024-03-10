import re
import sys

ip_regex = re.compile(r'(?P<address>\d+\.\d+\.\d+\.\d+).*?\d{4}:(?P<time_hour>\d{2}):\d{2},*?')

for input_line in sys.stdin:
    regex_match = ip_regex.search(input_line)
    if regex_match:
        formatted_output = f"[{regex_match.group('time_hour')}:00]{regex_match.group('address')}\t1"
        print(formatted_output)
