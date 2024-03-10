import re
import sys

pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2},*?')

for line in sys.stdin:
    result = pattern.search(line)
    if result:
        formatted_output = f"[{result.group('hour')}:00]{result.group('ip')}\t1"
        print(formatted_output)
