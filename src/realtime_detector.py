from scapy.all import sniff

from nfstream import NFStreamer

from threading import Thread

from queue import Queue

from packet_capture import packet_stream

from flow_builder import build_flow

from session_analyzer import analyze

from inference_engine import predict

from alert_engine import send_alert

from metrics import system_usage

from profiler import Profile

from performance import throughput

import time

packet_queue=Queue()

flow_queue=Queue()

session_queue=Queue()


def capture(packet_queue):
    print("[INFO] NFStreamer bat dau lang nghe tren ens33...")

#    streamer = NFStreamer(source="ens33", promiscuous_mode=True)

    for flow_dict in packet_stream("ens33"):
          src_ip = flow_dict.get("src_ip", "")
          dst_ip = flow_dict.get("dst_ip", "")

          if (dst_ip.startswith("239.") or 
              dst_ip.startswith("224.") or 
              dst_ip == "255.255.255.255"):
              continue

          if dst_ip.startswith("ff") or dst_ip.startswith("FF"):
            continue

          vmware_infrastructure_ips = ["192.168.88.1", "192.168.88.2", "192.168.88.254"]
          if src_ip in vmware_infrastructure_ips or dst_ip in vmware_infrastructure_ips:
              continue

          if not (src_ip.startswith("192.168.88.") and dst_ip.startswith("192.168.88.")):
            continue

          packet_queue.put(flow_dict)

def flow_worker():

    while True:

        packet=packet_queue.get()

        p=Profile("flow")

        flow=build_flow(
            packet
        )

        flow_queue.put(
            flow
        )

        latency=p.stop()

        print(
           f"FLOW={latency:.2f}ms"
        )

def session_worker():

    while True:

        x=flow_queue.get()

        p=Profile("session")

        x=analyze(
            x
        )

        session_queue.put(
            x
        )

        latency=p.stop()

        print(f"SESSION={latency:.2f}ms")

def ai_worker():

    while True:

        x=session_queue.get()

        p=Profile("inference")

        label,conf=predict(
             x
        )

        latency=p.stop()

        th=throughput()

        if th is not None:

            print(
            f"Flow/s={th:.2f}"
            )

        usage=system_usage()

        import csv,time

        with open(
        "/home/ids/IDS_Project/logs/resource.csv",
        "a"
        ) as f:

            writer=csv.writer(f)

            writer.writerow([

                time.time(),

                usage["cpu"],

                usage["ram"]

            ])

        print(
        f"Latency:{latency:.2f}ms"
        )

        send_alert(
            label,
            conf,
            x
        )

Thread(
target=capture,
args=(packet_queue,),
daemon=True
).start()

for _ in range(4):

    Thread(
    target=flow_worker,
    daemon=True
    ).start()


for _ in range(2):

    Thread(
    target=session_worker,
    daemon=True
    ).start()


Thread(
target=ai_worker,
daemon=True
).start()


while True:

    time.sleep(1)

