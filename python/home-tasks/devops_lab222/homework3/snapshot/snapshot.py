"""
Make snapshot

{"Tasks": {"total": 440, "running": 1, "sleeping": 354, "stopped": 1, "zombie": 0},
"%CPU": {"user": 14.4, "system": 2.2, "idle": 82.7},
"KiB Mem": {"total": 16280636, "free": 335140, "used": 11621308},
"KiB Swap": {"total": 16280636, "free": 335140, "used": 11621308},
"Timestamp": 1624400255}
"""
import argparse
import psutil
import json
import os
import time


class SystemStatus:
    def create_json_file(self, file_name):
        proccess_list = psutil.pids()
        total = len(proccess_list)
        running_count = 0
        sleeping_count = 0
        stopped_count = 0
        zombie_count = 0
        for i in proccess_list:
            p = psutil.Process(i)
            if p.status() == 'running':
                running_count += 1
            elif p.status() == 'sleeping':
                sleeping_count += 1
            elif p.status() == 'stopped':
                stopped_count += 1
            elif p.status() == 'zombie':
                zombie_count += 1
        cpu_user = psutil.cpu_times_percent().user
        cpu_system = psutil.cpu_times_percent().system
        cpu_idle = psutil.cpu_times_percent().idle
        mem_total = psutil.virtual_memory().total // 1024
        mem_free = psutil.virtual_memory().free // 1024
        mem_used = psutil.virtual_memory().used // 1024
        swap_total = psutil.swap_memory().total // 1024
        swap_free = psutil.swap_memory().free // 1024
        swap_used = psutil.swap_memory().used // 1024
        timestamp = int(time.time())
        json_data_output = {
            "Tasks": {"total": total, "running": running_count, "sleeping": sleeping_count,
                      "stopped": stopped_count, "zombie": zombie_count},
            "%CPU": {"user": cpu_user, "system": cpu_system, "idle": cpu_idle},
            "KiB Mem": {"total": mem_total, "free": mem_free, "used": mem_used},
            "KiB Swap": {"total": swap_total, "free": swap_free, "used": swap_used},
            "Timestamp": timestamp
        }

        with open(file_name, "a") as file:
            json.dump(json_data_output, file)
            file.close()
        print(json_data_output, end="\r")


def main():
    """Snapshot tool."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="Interval between snapshots in seconds", type=int, default=30)
    parser.add_argument("-f", help="Output file name", default="snapshot.json")
    parser.add_argument("-n", help="Quantity of snapshot to output", default=20)
    args = parser.parse_args()
    f = open(args.f, 'w')
    f.close()
    vars = {}
    for i in range(args.n):
        os.system('clear')
        vars[f"var{i}"] = SystemStatus()
        vars[f"var{i}"].create_json_file(file_name=args.f)
        file = open(args.f, 'a')
        file.write('\n')
        file.close()
        time.sleep(args.i)


if __name__ == "__main__":
    main()
