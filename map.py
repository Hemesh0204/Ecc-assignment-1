import re
import sys

regex = re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?"\w+(?P<subdir>.*?)')

for index in sys.stdin:
    ans = regex.search(index)
    if ans:
        print('%s\t%s' % (ans.group('ip'), 1))
