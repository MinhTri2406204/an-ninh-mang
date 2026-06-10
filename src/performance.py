import time
import csv
import os

window_start=time.time()

flow_count=0


if not os.path.exists("/home/ids/IDS_Project/logs/throughput.csv"):

    with open(
        "/home/ids/IDS_Project/logs/throughput.csv",
        "w"
    ) as f:

        writer=csv.writer(f)

        writer.writerow([
            "time",
            "flow_per_sec"
        ])


def throughput():

    global flow_count,window_start

    flow_count +=1

    now=time.time()

    elapsed=now-window_start

    # cửa sổ 5 giây
    if elapsed>=5:

        th=flow_count/elapsed

        with open(
            "/home/ids/IDS_Project/logs/throughput.csv",
            "a"
        ) as f:

            writer=csv.writer(f)

            writer.writerow([
                now,
                th
            ])

        flow_count=0

        window_start=now

        return th

    return None
