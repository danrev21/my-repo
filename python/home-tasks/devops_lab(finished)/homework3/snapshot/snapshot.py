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
import time
import os


class my_dict:
    def __init__(self):
        self.item = {}

    def add_item(self, name, value):
        self.item[name] = value

    def print_item(self):
        print(self.item)


def main():
    """Snapshot tool."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="Interval between snapshots in seconds", type=int, default=5)
    parser.add_argument("-f", help="Output file name", default="snapshot.json")
    parser.add_argument("-n", help="Quantity of snapshot to output", default=20)
    args = parser.parse_args()
    if int(args.n) <= 0:
        quit()
    else:
        j = 1
        os.system('clear')
    while j <= int(args.n):
        total, running, sleeping, stopped, zombie = 0, 0, 0, 0, 0
        for proc in psutil.process_iter(['status']):
            if proc.info["status"] == "running":
                running += 1
            if proc.info["status"] == "sleeping":
                sleeping += 1
            if proc.info["status"] == "stopped":
                stopped += 1
            if proc.info["status"] == "zombie":
                zombie += 1
            total += 1
        my_tasks = my_dict()
        my_tasks.add_item("total", total)
        my_tasks.add_item("running", running)
        my_tasks.add_item("sleeping", sleeping)
        my_tasks.add_item("stopped", stopped)
        my_tasks.add_item("zombie", zombie)
        tasks = my_tasks.item
        s_cpu_times = psutil.cpu_times_percent()
        cpu = {"user": s_cpu_times.user, "system": s_cpu_times.system, "idle": s_cpu_times.idle}
        s_m = psutil.virtual_memory()
        k = int(1024)
        mem = {"total": int(s_m.total / k), "free": int(s_m.free / k), "used": int(s_m.used / k)}
        s_s = psutil.swap_memory()
        swap = {"total": int(s_s.total / k), "free": int(s_s.free / k), "used": int(s_s.used / k)}
        snapshot = {"Tasks": tasks, "%CPU": cpu, "KiB Mem": mem, "KiB Swap": swap}
        snapshot["Timestamp"] = int(time.time())
        print(snapshot, end="\r")
        if j == 1:
            mode = "w"
        else:
            mode = "a"
        with open(args.f, mode) as outfile:
            json.dump(snapshot, outfile)
            outfile.write("\n")
        j += 1
        time.sleep(args.i)


if __name__ == "__main__":
    main()
