import re
import sys

pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+).*?"\w+(?P<subdir>.*?)')

for line in sys.stdin:
    match = pattern.search(line)
    if match:
        ip_address = match.group('ip')
        print(f'{ip_address}\t1')
