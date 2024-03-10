from operator import itemgetter
import sys
from collections import defaultdict

ip_count = defaultdict(int)

for line in sys.stdin:
    line = line.strip()
    parts = line.split('\t')
    if len(parts) == 2:
        ip, num_str = parts
        try:
            num = int(num_str)
            ip_count[ip] += num
        except ValueError:
            continue


sorted_ip_count = sorted(ip_count.items(), key=itemgetter(1), reverse=True)

aggregated_data = defaultdict(int)
for ip, count in sorted_ip_count:
    aggregated_data[ip] += count


output_data = []
for ip, count in aggregated_data.items():
    
    time_ip_split = ip.rsplit(']', 1)
    if len(time_ip_split) == 2:
        time, actual_ip = time_ip_split[0]+"]", time_ip_split[1]
        output_data.append({"time": time, "ip": actual_ip, "count": count})


output_data.sort(key=lambda x: (x['time'], -x['count']))
time_grouped_data = defaultdict(list)

for data in output_data:
    time_grouped_data[data['time']].append(data)


final_output = []
for time, data_list in time_grouped_data.items():
    for data in data_list[:3]:
        final_output.append(f"{data['time']} hour {data['ip']} : {data['count']:,}")


for line in final_output:
    print(line)

sys.stdout.flush()
