import sys
import argparse
from operator import itemgetter
from collections import defaultdict

def parse_arguments():
    parser = argparse.ArgumentParser(description='Process IP addresses and counts.')
    parser.add_argument('--timerange', help='Specify a timerange in the format "hh-hh". For example, --timerange 03-04')
    return parser.parse_args()

def trim_time(time_string):
    return time_string.strip()

def main():
    args = parse_arguments()
    timerange_filter = args.timerange

    ip_counts = {}

    for raw_line in sys.stdin:
        raw_line = raw_line.strip()
        ip_address, count_str = raw_line.split()
        try:
            count = int(count_str)
            ip_counts[ip_address] = ip_counts.get(ip_address, 0) + count
        except ValueError:
            continue

    sorted_ip_counts = sorted(ip_counts.items(), key=lambda x: -x[1])

    refined_counts = {}
    for ip, count in sorted_ip_counts:
        refined_counts.setdefault(ip, 0)
        refined_counts[ip] += int(count)

    refined_sorted = list(sorted(refined_counts.items(), key=lambda item: item[1], reverse=True))

    structured_data = []

    for item in refined_sorted:
        time_ip_split = item[0].strip().rsplit(']', 1)
        try:
            time_frame, ip = time_ip_split[0] + "]", time_ip_split[1]
        except:
            continue
        data_dict = {
            "time": time_frame,
            "data": [
                {"ip": ip},
                {"count": item[1]}
            ]
        }
        structured_data.append(data_dict)

    aggregate_data = defaultdict(lambda: defaultdict(int))
    for data in structured_data:
        time = trim_time(data['time'])
        ip = data['data'][0]['ip']
        count = int(data['data'][1]['count'])
        aggregate_data[time][ip] += count

    final_result = []
    for time, ips in aggregate_data.items():
        if timerange_filter:
            start, end = map(int, timerange_filter.split('-'))
            current_hour = int(time.split(':')[0][1:])
            if not (start <= current_hour < end):
                continue

        top_ips = sorted(ips.items(), key=lambda x: x[1], reverse=True)[:3]
        for ip, count in top_ips:
            result_entry = {
                "time": time,
                "data": [
                    {"ip": ip},
                    {"count": "{:,}".format(count)}
                ]
            }
            final_result.append(result_entry)

    sorted_final_result = sorted(final_result, key=lambda x: x['time'])

    for entry in sorted_final_result:
        print(f"{entry['time']} hour {entry['data'][0]['ip']} : {entry['data'][1]['count']}")
    sys.stdout.flush()

if __name__ == "__main__":
    main()
