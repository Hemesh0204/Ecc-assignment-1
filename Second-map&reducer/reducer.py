from operator import itemgetter
import sys

ip_count_map = {}

for input_line in sys.stdin:
    input_line = input_line.strip()
    ip_address, count_str = input_line.split()
    
    try:
        count = int(count_str)
        ip_count_map[ip_address] = ip_count_map.get(ip_address, 0) + count
    except ValueError:
        continue

ordered_ip_count = sorted(ip_count_map.items(), key=itemgetter(0))
desc_sorted_ip_count = sorted(ordered_ip_count, key=lambda x: x[1], reverse=True)

for ip, total in desc_sorted_ip_count[:3]:
    print(f'{ip}\t{total}')
