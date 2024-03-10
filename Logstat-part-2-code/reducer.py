from operator import itemgetter
import sys

ip_counts = {}

for raw_line in sys.stdin:
    clean_line = raw_line.strip()
    ip_address, count_str = clean_line.split('\t')
    try:
        count = int(count_str)
        ip_counts[ip_address] = ip_counts.get(ip_address, 0) + count
    except ValueError:
        continue

ordered_ip_counts = sorted(ip_counts.items(), key=itemgetter(0))

for address, total in ordered_ip_counts:
    print(f'{address}\t{total}')
