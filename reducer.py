from operator import itemgetter
import sys

ip_count_map = {}

for line in sys.stdin:
    line = line.strip()
    ip_address, count_str = line.split('\t')
    try:
        count = int(count_str)
        ip_count_map[ip_address] = ip_count_map.get(ip_address, 0) + count
    except ValueError:
        continue

sorted_ip_count_map = sorted(ip_count_map.items(), key=itemgetter(0))

for ip_address, total_count in sorted_ip_count_map:
    print(f'{ip_address}\t{total_count}')
